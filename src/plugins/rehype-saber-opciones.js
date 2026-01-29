/**
 * Plugin de rehype para transformar opciones de respuesta en talleres Saber
 * Las opciones vienen como un <p> con texto separado por <br>
 * SOLO procesa opciones FUERA de <details> (las de dentro se muestran como lista simple)
 */
import { visit } from 'unist-util-visit';

export function rehypeSaberOpciones() {
  return (tree, file) => {
    const filePath = file.history?.[0] || file.path || '';
    
    console.log('[rehypeSaberOpciones] Procesando archivo:', filePath);
    
    if (!filePath.includes('/saber/')) {
      console.log('[rehypeSaberOpciones] ❌ No es saber, saltando');
      return;
    }
    
    console.log('[rehypeSaberOpciones] ✅ Es archivo saber, buscando párrafos con opciones...');

    // Paso 1: Marcar todos los nodos dentro de <details>
    const nodesInsideDetails = new Set();
    
    visit(tree, 'element', (node) => {
      if (node.tagName === 'details') {
        // Marcar todos los descendientes
        visit(node, () => {
          nodesInsideDetails.add(node);
        });
      }
    });

    console.log(`[rehypeSaberOpciones] Nodos dentro de details: ${nodesInsideDetails.size}`);

    const nodesToReplace = [];

    // Función auxiliar para extraer texto de un nodo (incluyendo HTML inline)
    function extractText(node) {
      if (node.type === 'text') {
        return node.value;
      }
      if (node.type === 'element') {
        return node.children.map(extractText).join('');
      }
      return '';
    }

    // Función auxiliar para clonar nodos hijos (preservando HTML inline)
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
        return child;
      });
    }

    // Paso 2: Buscar párrafos con opciones (solo fuera de details)
    visit(tree, 'element', (node, index, parent) => {
      // Buscar párrafos <p>
      if (node.tagName !== 'p' || !parent || typeof index !== 'number') {
        return;
      }

      // Saltar si está dentro de <details>
      if (nodesInsideDetails.has(node)) {
        return;
      }

      // Extraer partes del párrafo separadas por <br>
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
      // Agregar la última parte
      if (currentPart.length > 0) {
        parts.push(currentPart);
      }

      // Verificar que tengamos exactamente 4 partes
      if (parts.length !== 4) {
        return;
      }

      // Verificar que cada parte empiece con A., B., C., D.
      const opciones = [];
      let hasMarkup = false; // Flag para detectar si tiene marcadores (está en details)
      
      for (let i = 0; i < 4; i++) {
        const letra = String.fromCharCode(65 + i); // A, B, C, D
        const part = parts[i];
        
        // Verificar si tiene elementos <mark> o <del> (indica que está en details)
        for (const node of part) {
          if (node.type === 'element' && (node.tagName === 'mark' || node.tagName === 'del')) {
            hasMarkup = true;
            break;
          }
        }
        
        // Extraer el texto completo de la parte
        const fullText = part.map(extractText).join('').trim();
        
        if (!fullText.match(new RegExp(`^${letra}\\.\\s`))) {
          return; // No coincide con la letra esperada
        }
        
        // Guardar los nodos originales (preservando HTML inline como <mark>, <del>, etc.)
        opciones.push({ 
          text: fullText,
          nodes: part
        });
      }

      // Si tiene marcadores, NO procesar (dejar como párrafo normal)
      if (hasMarkup) {
        console.log('[rehypeSaberOpciones] ⏭️  Saltando opciones con marcadores (dentro de details)');
        return;
      }

      // Si llegamos aquí, encontramos un grupo válido
      console.log('[rehypeSaberOpciones] 🎉 Grupo completo encontrado (fuera de details)!', opciones.map(o => o.text.substring(0, 30)));
      nodesToReplace.push({ parent, index, opciones });
    });

    console.log(`[rehypeSaberOpciones] Grupos a reemplazar: ${nodesToReplace.length}`);

    // Reemplazar en orden inverso
    nodesToReplace.reverse().forEach(({ parent, index, opciones }) => {
      const container = {
        type: 'element',
        tagName: 'div',
        properties: { className: ['opciones-grid'] },
        children: opciones.map((opcion, i) => {
          const letra = String.fromCharCode(65 + i);
          
          // Clonar los nodos originales
          const textoNodes = cloneChildren(opcion.nodes);
          
          // Limpiar espacios en blanco y remover letra de TODOS los nodos de texto
          for (let j = 0; j < textoNodes.length; j++) {
            if (textoNodes[j].type === 'text') {
              // Limpiar espacios en blanco al inicio y final
              textoNodes[j].value = textoNodes[j].value.trim();
              
              // Remover la letra si está presente (A., B., C., D.)
              textoNodes[j].value = textoNodes[j].value.replace(/^[A-D]\.\s+/, '');
              
              // Si el nodo quedó vacío, marcarlo para eliminación
              if (!textoNodes[j].value) {
                textoNodes[j]._remove = true;
              }
            }
          }
          
          // Filtrar nodos vacíos
          const cleanNodes = textoNodes.filter(n => !n._remove);
          
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
        })
      };

      parent.children[index] = container;
    });
    
    console.log('[rehypeSaberOpciones] ✅ Procesamiento completado\n');
  };
}
