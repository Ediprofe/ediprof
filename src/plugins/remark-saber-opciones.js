/**
 * Plugin de remark para transformar opciones de respuesta en talleres Saber
 * Convierte automáticamente:
 *   A. texto
 *   B. texto  
 *   C. texto
 *   D. texto
 * 
 * En HTML con clases para estilizar
 */

import { visit } from 'unist-util-visit';

export function remarkSaberOpciones() {
  return (tree, file) => {
    // Debug: verificar si el plugin se ejecuta
    const filePath = file.history[0] || '';
    const isSaber = filePath.includes('/saber/');
    
    console.log('[remarkSaberOpciones] Procesando:', filePath);
    console.log('[remarkSaberOpciones] Es archivo saber?', isSaber);

    // Solo aplicar en archivos de saber
    if (!isSaber) {
      console.log('[remarkSaberOpciones] Saltando - no es saber');
      return;
    }

    const nodesToReplace = [];
    let paragraphCount = 0;
    
    visit(tree, (node, index, parent) => {
      if (!parent || index === null) return;
      if (node.type !== 'paragraph') return;

      paragraphCount++;

      // Verificar si este párrafo empieza con "A."
      const firstChild = node.children?.[0];
      if (!firstChild || firstChild.type !== 'text') return;
      
      const text = firstChild.value.trim();
      
      // Debug: mostrar primeros caracteres de cada párrafo
      if (paragraphCount <= 10) {
        console.log(`[remarkSaberOpciones] Párrafo ${paragraphCount}:`, text.substring(0, 50));
      }
      
      if (!text.match(/^A\.\s/)) return;

      console.log('[remarkSaberOpciones] ¡Encontré opción A!', text.substring(0, 50));

      // Buscar los siguientes 3 párrafos (B, C, D)
      const opciones = [{ node, index, text }];
      
      for (let i = 1; i <= 3; i++) {
        const letra = String.fromCharCode(65 + i); // B, C, D
        const nextNode = parent.children[index + i];
        
        if (!nextNode || nextNode.type !== 'paragraph') {
          console.log(`[remarkSaberOpciones] No encontré párrafo para ${letra}`);
          break;
        }
        
        const nextFirstChild = nextNode.children?.[0];
        if (!nextFirstChild || nextFirstChild.type !== 'text') {
          console.log(`[remarkSaberOpciones] ${letra} no tiene texto`);
          break;
        }
        
        const nextText = nextFirstChild.value.trim();
        if (!nextText.match(new RegExp(`^${letra}\\.\\s`))) {
          console.log(`[remarkSaberOpciones] ${letra} no coincide:`, nextText.substring(0, 30));
          break;
        }
        
        console.log(`[remarkSaberOpciones] ¡Encontré opción ${letra}!`);
        opciones.push({ node: nextNode, index: index + i, text: nextText });
      }

      // Si encontramos las 4 opciones, marcar para reemplazo
      if (opciones.length === 4) {
        console.log('[remarkSaberOpciones] ¡Grupo completo de opciones encontrado!');
        nodesToReplace.push({ parent, startIndex: index, opciones });
      } else {
        console.log('[remarkSaberOpciones] Grupo incompleto:', opciones.length, 'opciones');
      }
    });

    console.log('[remarkSaberOpciones] Total de grupos a reemplazar:', nodesToReplace.length);

    // Reemplazar en orden inverso para no afectar índices
    nodesToReplace.reverse().forEach(({ parent, startIndex, opciones }) => {
      // Crear el HTML
      let html = '\n<div class="opciones-container">\n';
      
      opciones.forEach((opcion, i) => {
        const letra = String.fromCharCode(65 + i); // A, B, C, D
        const texto = opcion.text.replace(/^[A-D]\.\s+/, '');
        
        html += '<div class="opcion-item">\n';
        html += `<span class="opcion-letra">${letra}</span>\n`;
        html += `<span class="opcion-texto">${texto}</span>\n`;
        html += '</div>\n';
      });
      
      html += '</div>\n';

      console.log('[remarkSaberOpciones] HTML generado:', html.substring(0, 100));

      // Crear nodo HTML
      const htmlNode = {
        type: 'html',
        value: html
      };

      // Reemplazar los 4 párrafos con el contenedor HTML
      parent.children.splice(startIndex, 4, htmlNode);
    });
  };
}
