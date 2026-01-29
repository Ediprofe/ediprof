/**
 * Plugin de rehype para transformar opciones de respuesta en talleres Saber
 *
 * Transforma párrafos con formato "A. texto\nB. texto\nC. texto\nD. texto"
 * en una estructura HTML con clases para estilizado.
 *
 * SOLO procesa opciones que NO tienen marcadores de retroalimentación
 * (las opciones con <mark> o <del> están dentro de <details> y se dejan como texto).
 */
import { visit } from 'unist-util-visit';

// Controlar logs solo en desarrollo
const DEBUG = process.env.NODE_ENV === 'development';
const log = (...args) => DEBUG && console.log('[rehypeSaberOpciones]', ...args);

/**
 * Verifica si un nodo contiene elementos <mark> o <del> (retroalimentación)
 */
function containsMarkers(node) {
  if (!node) return false;

  if (node.type === 'element') {
    if (node.tagName === 'mark' || node.tagName === 'del') {
      return true;
    }
  }

  if (node.children) {
    return node.children.some(containsMarkers);
  }

  return false;
}

/**
 * Extrae texto plano de un nodo (recursivamente)
 */
function extractText(node) {
  if (node.type === 'text') return node.value;
  if (node.children) return node.children.map(extractText).join('');
  return '';
}

/**
 * Clona nodos hijos preservando estructura HTML
 */
function cloneChildren(children) {
  return children.map(child => {
    if (child.type === 'text') {
      return { type: 'text', value: child.value };
    }
    if (child.type === 'element') {
      return {
        type: 'element',
        tagName: child.tagName,
        properties: { ...child.properties },
        children: cloneChildren(child.children || [])
      };
    }
    return { ...child };
  });
}

/**
 * Consume los primeros N caracteres del árbol de nodos.
 * Retorna una nueva lista de nodos con esos caracteres eliminados.
 */
function consumeCharacters(nodes, limit) {
  let consumed = 0;

  function processList(list) {
    const keptNodes = [];

    for (const node of list) {
      if (consumed >= limit) {
        // Ya consumimos todo lo necesario, mantenemos el resto intacto
        keptNodes.push(node);
        continue;
      }

      if (node.type === 'text') {
        const text = node.value;
        const len = text.length;
        const needed = limit - consumed;

        if (len <= needed) {
          // Este nodo está totalmente dentro del rango a eliminar
          consumed += len;
          // No lo agregamos a keptNodes (se elimina)
        } else {
          // Consumimos parcialmente este nodo
          const newText = text.slice(needed);
          consumed += needed;
          keptNodes.push({ ...node, value: newText });
        }
      } else if (node.children) {
        // Es un elemento contenedor (b, strong, em, etc.)
        // Procesamos sus hijos recursivamente
        const newChildren = processList(node.children);

        // Si después de limpiar hijos, el nodo quedó vacío, ¿lo guardamos?
        // Si tiene hijos, lo guardamos.
        if (newChildren.length > 0) {
          keptNodes.push({ ...node, children: newChildren });
        }
      } else {
        // Otros nodos (comentarios, etc), se mantienen
        keptNodes.push(node);
      }
    }
    return keptNodes;
  }

  return processList(nodes);
}

/**
 * Crea la estructura HTML para una opción de respuesta
 */
function createOptionElement(letra, contentNodes) {
  // 1. Obtener texto completo para determinar la longitud exacta del prefijo
  const fullText = contentNodes.map(extractText).join('');
  const match = fullText.match(/^\s*[A-D]\.\s*/);

  let cleanNodes = contentNodes;

  if (match) {
    const prefixLength = match[0].length;
    // Usar la función utilitaria para consumir exactamente esos caracteres del árbol
    cleanNodes = consumeCharacters(contentNodes, prefixLength);
  }

  // Si después de limpiar nos queda un array vacío o solo espacios, hay que tener cuidado.
  // Pero generalmente quedará el contenido real (texto, imágenes, etc).

  return {
    type: 'element',
    tagName: 'div',
    properties: { className: ['opcion-item'] },
    children: [
      {
        type: 'element',
        tagName: 'span',
        properties: { className: ['opcion-letra'] },
        children: [{ type: 'text', value: letra }]
      },
      {
        type: 'element',
        tagName: 'span',
        properties: { className: ['opcion-texto'] },
        children: cleanNodes
      }
    ]
  };
}

export function rehypeSaberOpciones() {
  return (tree, file) => {
    const filePath = file.history?.[0] || file.path || '';

    // Solo procesar archivos de saber
    if (!filePath.includes('/saber/')) {
      return;
    }

    log('Procesando:', filePath.split('/').slice(-3).join('/'));

    // Paso 1: Agregar clases a elementos <del> y <mark> existentes
    visit(tree, 'element', (node) => {
      if (node.tagName === 'del') {
        node.properties = node.properties || {};
        const existing = node.properties.className || [];
        const classes = Array.isArray(existing) ? existing : [];
        if (!classes.includes('saber-tachado')) {
          node.properties.className = [...classes, 'saber-tachado'];
        }
      }
      if (node.tagName === 'mark') {
        node.properties = node.properties || {};
        const existing = node.properties.className || [];
        const classes = Array.isArray(existing) ? existing : [];
        if (!classes.includes('saber-highlight')) {
          node.properties.className = [...classes, 'saber-highlight'];
        }
      }
    });

    // Paso 2: Encontrar párrafos con opciones (sin marcadores de retroalimentación)
    const replacements = [];
    let skippedWithMarkers = 0;
    let foundPlain = 0;

    visit(tree, 'element', (node, index, parent) => {
      if (node.tagName !== 'p' || !parent || typeof index !== 'number') {
        return;
      }

      // Buscar patrón: párrafo con 4 líneas separadas por <br>
      const parts = [];
      let currentPart = [];

      for (const child of node.children) {
        if (child.type === 'element' && child.tagName === 'br') {
          if (currentPart.length > 0) {
            parts.push(currentPart);
            currentPart = [];
          }
        } else {
          currentPart.push(child);
        }
      }
      if (currentPart.length > 0) {
        parts.push(currentPart);
      }

      // Debe tener exactamente 4 partes
      if (parts.length !== 4) return;

      // Verificar que cada parte empiece con A., B., C., D.
      const opciones = [];
      const letras = ['A', 'B', 'C', 'D'];
      let hasMarkers = false;

      for (let i = 0; i < 4; i++) {
        const text = parts[i].map(extractText).join('').trim();
        const expectedPattern = new RegExp(`^${letras[i]}\\.\\s`);

        if (!expectedPattern.test(text)) {
          return;
        }

        // Verificar si ESTA parte tiene marcadores
        if (parts[i].some(containsMarkers)) {
          hasMarkers = true;
        }

        opciones.push({
          letra: letras[i],
          nodes: cloneChildren(parts[i])
        });
      }

      // Si tiene marcadores, es retroalimentación dentro de <details> - NO procesar
      if (hasMarkers) {
        skippedWithMarkers++;
        return;
      }

      foundPlain++;
      replacements.push({ parent, index, opciones });
    });

    log(`Saltados con marcadores (retroalimentación): ${skippedWithMarkers}`);
    log(`Transformados (opciones limpias): ${foundPlain}`);

    // Paso 3: Reemplazar en orden inverso
    for (const { parent, index, opciones } of replacements.reverse()) {
      const container = {
        type: 'element',
        tagName: 'div',
        properties: { className: ['opciones-grid'] },
        children: opciones.map(({ letra, nodes }) =>
          createOptionElement(letra, nodes)
        )
      };

      parent.children[index] = container;
    }
  };
}
