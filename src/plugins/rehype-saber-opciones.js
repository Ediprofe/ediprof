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
 * Crea la estructura HTML para una opción de respuesta
 */
function createOptionElement(letra, contentNodes) {
  const cleanNodes = [];
  let firstTextProcessed = false;

  for (const node of contentNodes) {
    if (node.type === 'text' && !firstTextProcessed) {
      const cleaned = node.value.replace(/^[A-D]\.\s*/, '').trim();
      if (cleaned) {
        cleanNodes.push({ type: 'text', value: cleaned });
      }
      firstTextProcessed = true;
    } else if (node.type === 'text') {
      const trimmed = node.value.trim();
      if (trimmed) {
        cleanNodes.push({ type: 'text', value: trimmed });
      }
    } else {
      cleanNodes.push(node);
    }
  }

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
