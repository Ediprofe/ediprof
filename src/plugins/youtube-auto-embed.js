import { visit } from 'unist-util-visit';

/**
 * Plugin de remark para embeber videos de YouTube automáticamente.
 * 
 * Maneja dos casos:
 * 1. Blockquotes con formato "🎬 **Video:**" - embebe YouTube, deja otros links normales
 * 2. Links de YouTube sueltos en párrafos - los convierte en iframes
 */
export function youtubeAutoEmbed() {
  const youtubeRegex = /(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})/;

  /**
   * Genera el HTML del iframe de YouTube
   */
  function createYoutubeEmbed(videoId) {
    return `
<div class="video-container">
  <iframe 
    src="https://www.youtube-nocookie.com/embed/${videoId}"
    title="Video educativo"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen
    loading="lazy">
  </iframe>
</div>`;
  }

  /**
   * Verifica si un blockquote tiene el patrón de video "🎬 **Video:**"
   */
  function isVideoBlockquote(node) {
    if (node.type !== 'blockquote') return false;

    // Buscar en el primer párrafo del blockquote
    const firstParagraph = node.children?.find(c => c.type === 'paragraph');
    if (!firstParagraph) return false;

    // Buscar el patrón "🎬" seguido de "Video:"
    let hasVideoEmoji = false;
    let hasVideoText = false;

    for (const child of firstParagraph.children || []) {
      if (child.type === 'text' && child.value.includes('🎬')) {
        hasVideoEmoji = true;
      }
      if (child.type === 'strong') {
        const strongText = child.children?.find(c => c.type === 'text');
        if (strongText?.value?.includes('Video')) {
          hasVideoText = true;
        }
      }
    }

    return hasVideoEmoji && hasVideoText;
  }

  /**
   * Procesa un blockquote de video y lo transforma
   */
  function processVideoBlockquote(node) {
    const newChildren = [];
    let hasYoutubeEmbed = false;

    for (const paragraph of node.children) {
      if (paragraph.type !== 'paragraph') continue;

      for (const child of paragraph.children || []) {
        // Si es un link, verificar si es de YouTube
        if (child.type === 'link') {
          const match = child.url.match(youtubeRegex);

          if (match && !hasYoutubeEmbed) {
            // Es YouTube - embeber como iframe
            const videoId = match[1];
            newChildren.push({
              type: 'html',
              value: createYoutubeEmbed(videoId)
            });
            hasYoutubeEmbed = true;
          } else {
            // No es YouTube o ya hay un embed - mantener como link normal
            const linkText = child.children?.find(c => c.type === 'text')?.value || 'Ver video';
            newChildren.push({
              type: 'html',
              value: `<p class="video-link"><a href="${child.url}" target="_blank" rel="noopener noreferrer">${linkText}</a></p>`
            });
          }
        }
      }
    }

    return newChildren;
  }

  return (tree) => {
    visit(tree, (node, index, parent) => {
      if (!parent || index === undefined) return;

      // CASO 1: Blockquote con formato "🎬 **Video:**"
      if (isVideoBlockquote(node)) {
        const newNodes = processVideoBlockquote(node);
        if (newNodes.length > 0) {
          // Envolver todo en un contenedor de video-section
          const wrapper = {
            type: 'html',
            value: '<div class="video-section">'
          };
          const wrapperEnd = {
            type: 'html',
            value: '</div>'
          };
          parent.children.splice(index, 1, wrapper, ...newNodes, wrapperEnd);
          return index + newNodes.length + 2;
        }
        return;
      }

      // CASO 2: Párrafos que contienen solo un link de YouTube (comportamiento original)
      if (node.type === 'paragraph' && node.children?.length === 1) {
        const child = node.children[0];
        if (child.type === 'link') {
          const match = child.url.match(youtubeRegex);

          if (match) {
            const videoId = match[1];
            parent.children[index] = {
              type: 'html',
              value: createYoutubeEmbed(videoId)
            };
          }
        }
      }
    });
  };
}
