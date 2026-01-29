/**
 * Plugin de remark para procesar marcadores de retroalimentación en talleres Saber
 * ==texto== → <mark class="highlight">texto</mark> (resaltado amarillo)
 * ~~texto~~ → <del class="tachado">texto</del> (tachado rojo)
 * 
 * Este plugin se ejecuta en la fase de remark (antes de convertir a HTML)
 * Solo aplica a archivos en /saber/
 */
import { visit } from 'unist-util-visit';

export function remarkSaberMarcadores() {
  return (tree, file) => {
    const filePath = file.history?.[0] || file.path || '';
    
    // Solo procesar archivos de saber
    if (!filePath.includes('/saber/')) {
      return;
    }

    console.log('[remarkSaberMarcadores] Procesando marcadores en:', filePath);

    visit(tree, 'text', (node, index, parent) => {
      if (!node.value || !parent) return;

      const text = node.value;
      
      // Verificar si tiene marcadores
      if (!text.includes('==') && !text.includes('~~')) {
        return;
      }

      // Procesar el texto y crear nodos HTML
      const newNodes = [];
      let remaining = text;
      let lastIndex = 0;

      // Regex para encontrar ==texto== o ~~texto~~
      const regex = /(==([^=]+)==)|(~~([^~]+)~~)/g;
      let match;

      while ((match = regex.exec(text)) !== null) {
        // Agregar texto antes del marcador
        if (match.index > lastIndex) {
          newNodes.push({
            type: 'text',
            value: text.substring(lastIndex, match.index)
          });
        }

        // Determinar tipo de marcador
        if (match[1]) {
          // ==resaltado==
          newNodes.push({
            type: 'html',
            value: `<mark class="highlight">${match[2]}</mark>`
          });
        } else if (match[3]) {
          // ~~tachado~~
          newNodes.push({
            type: 'html',
            value: `<del class="tachado">${match[4]}</del>`
          });
        }

        lastIndex = regex.lastIndex;
      }

      // Agregar texto restante
      if (lastIndex < text.length) {
        newNodes.push({
          type: 'text',
          value: text.substring(lastIndex)
        });
      }

      // Reemplazar el nodo original con los nuevos nodos
      if (newNodes.length > 0) {
        parent.children.splice(index, 1, ...newNodes);
        return index + newNodes.length;
      }
    });

    console.log('[remarkSaberMarcadores] ✅ Marcadores procesados\n');
  };
}
