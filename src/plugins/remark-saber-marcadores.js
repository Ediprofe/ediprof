/**
 * Plugin de remark para procesar marcadores de retroalimentación en talleres Saber
 *
 * Convierte:
 *   ==texto== → <mark class="saber-highlight">texto</mark> (resaltado amarillo)
 *   ~~texto~~ → <del class="saber-tachado">texto</del> (tachado rojo)
 *
 * Nota: Usamos clases específicas "saber-highlight" y "saber-tachado"
 * para evitar conflictos con otros estilos del proyecto.
 *
 * Solo aplica a archivos en /saber/
 */
import { visit } from 'unist-util-visit';

// Regex para marcadores
const HIGHLIGHT_REGEX = /==([^=]+)==/g;
const STRIKETHROUGH_REGEX = /~~([^~]+)~~/g;

export function remarkSaberMarcadores() {
  return (tree, file) => {
    const filePath = file.history?.[0] || file.path || '';

    // Solo procesar archivos de saber
    if (!filePath.includes('/saber/')) {
      return;
    }

    visit(tree, 'text', (node, index, parent) => {
      if (!node.value || !parent) return;

      const text = node.value;

      // Verificar si tiene marcadores
      if (!text.includes('==') && !text.includes('~~')) {
        return;
      }

      // Procesar el texto y crear nodos
      const newNodes = processMarkers(text);

      // Solo reemplazar si hubo cambios
      if (newNodes.length > 1 || (newNodes.length === 1 && newNodes[0].type !== 'text')) {
        parent.children.splice(index, 1, ...newNodes);
        return index + newNodes.length;
      }
    });
  };
}

/**
 * Procesa una cadena de texto y retorna un array de nodos
 * (texto plano + HTML para marcadores)
 */
function processMarkers(text) {
  const nodes = [];
  let lastIndex = 0;
  let working = text;

  // Combinar ambos patrones para procesar en orden de aparición
  const combinedRegex = /(==([^=]+)==)|(~~([^~]+)~~)/g;
  let match;

  while ((match = combinedRegex.exec(text)) !== null) {
    // Agregar texto antes del marcador
    if (match.index > lastIndex) {
      nodes.push({
        type: 'text',
        value: text.substring(lastIndex, match.index)
      });
    }

    // Determinar tipo de marcador y crear HTML
    if (match[1]) {
      // ==resaltado==
      nodes.push({
        type: 'html',
        value: `<mark class="saber-highlight">${escapeHtml(match[2])}</mark>`
      });
    } else if (match[3]) {
      // ~~tachado~~
      nodes.push({
        type: 'html',
        value: `<del class="saber-tachado">${escapeHtml(match[4])}</del>`
      });
    }

    lastIndex = combinedRegex.lastIndex;
  }

  // Agregar texto restante
  if (lastIndex < text.length) {
    nodes.push({
      type: 'text',
      value: text.substring(lastIndex)
    });
  }

  // Si no hubo marcadores, retornar el texto original
  if (nodes.length === 0) {
    return [{ type: 'text', value: text }];
  }

  return nodes;
}

/**
 * Escapa caracteres HTML para prevenir XSS
 */
function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
