/**
 * TextHighlighter - Resaltado de texto del DOM
 * 
 * Detecta la selección de texto y muestra un popup para resaltar
 * el texto seleccionado en la página.
 * 
 * Utiliza un enfoque seguro que no modifica el DOM directamente,
 * sino que usa elementos overlay para mostrar el resaltado.
 */

// Colores de resaltado disponibles (más transparentes para texto)
export const HIGHLIGHT_COLORS = [
  { name: 'Amarillo', hex: '#FBBF24', rgba: 'rgba(251, 191, 36, 0.4)' },
  { name: 'Verde', hex: '#34D399', rgba: 'rgba(52, 211, 153, 0.4)' },
  { name: 'Azul', hex: '#60A5FA', rgba: 'rgba(96, 165, 250, 0.4)' },
  { name: 'Rosa', hex: '#F472B6', rgba: 'rgba(244, 114, 182, 0.4)' },
  { name: 'Naranja', hex: '#FB923C', rgba: 'rgba(251, 146, 60, 0.4)' },
];

interface SimpleRect {
  left: number;
  top: number;
  width: number;
  height: number;
}

interface HighlightRect {
  id: string;
  rects: SimpleRect[];
  color: string;
  text: string;
}

export class TextHighlighter {
  private popup: HTMLElement | null = null;
  private selectedRange: Range | null = null;
  private boundHandleSelectionChange: () => void;
  private boundHandleMouseUp: (e: MouseEvent) => void;
  private isActive = false;
  
  // Sistema de resaltados como overlays (no modifica el DOM del contenido)
  private highlights: HighlightRect[] = [];
  private overlayContainer: HTMLElement | null = null;
  private highlightIdCounter = 0;
  
  // Sistema de deshacer
  private undoStack: HighlightRect[][] = [];

  constructor() {
    this.boundHandleSelectionChange = this.debounce(() => this.handleSelectionChange(), 200);
    this.boundHandleMouseUp = (e) => this.handleMouseUp(e);
  }

  /**
   * Activa el sistema de resaltado
   */
  public activate() {
    if (this.isActive) return;
    this.isActive = true;

    // Inyectar estilos (si no existen)
    this.injectStyles();
    
    // Crear contenedor de overlays (si no existe)
    this.createOverlayContainer();

    // Escuchar cambios en la selección
    document.addEventListener('selectionchange', this.boundHandleSelectionChange);
    document.addEventListener('mouseup', this.boundHandleMouseUp);
    
    // Re-renderizar overlays existentes
    this.renderOverlays();
  }

  /**
   * Pausa la detección de selecciones pero MANTIENE los resaltados visibles
   * Usar cuando se cambia de herramienta
   */
  public pause() {
    if (!this.isActive) return;
    this.isActive = false;

    document.removeEventListener('selectionchange', this.boundHandleSelectionChange);
    document.removeEventListener('mouseup', this.boundHandleMouseUp);

    this.hidePopup();
    
    // Los overlays y resaltados se MANTIENEN visibles
  }

  /**
   * Desactiva COMPLETAMENTE el sistema de resaltado y limpia todo
   * Usar cuando se cierra el modo clase
   */
  public deactivate() {
    // Primero pausar si estaba activo
    if (this.isActive) {
      this.pause();
    }
    
    // Remover el contenedor de overlays
    if (this.overlayContainer) {
      this.overlayContainer.remove();
      this.overlayContainer = null;
    }
    
    // Remover estilos
    this.removeStyles();
    
    // Limpiar estado (sin guardar undo ya que estamos cerrando)
    this.highlights = [];
    this.undoStack = [];
  }

  /**
   * Deshace el último resaltado
   */
  public undo(): boolean {
    if (this.undoStack.length === 0) return false;
    
    // Restaurar estado anterior
    this.highlights = this.undoStack.pop() || [];
    this.renderOverlays();
    return true;
  }

  /**
   * Limpia todos los resaltados
   */
  public clearAll() {
    // Solo guardar undo si hay algo que limpiar
    if (this.highlights.length > 0) {
      this.saveUndoState();
    }
    
    this.highlights = [];
    this.renderOverlays();
  }

  /**
   * Crea el contenedor de overlays
   */
  private createOverlayContainer() {
    if (this.overlayContainer) return;
    
    this.overlayContainer = document.createElement('div');
    this.overlayContainer.id = 'pm-highlight-overlays';
    this.overlayContainer.className = 'pm-highlight-overlay-container';
    document.body.appendChild(this.overlayContainer);
  }

  /**
   * Maneja cambios en la selección de texto
   */
  private handleSelectionChange() {
    // Solo mostrar popup en mouseup, no durante la selección
  }

  /**
   * Maneja mouseup para mostrar popup de resaltado
   */
  private handleMouseUp(e: MouseEvent) {
    if (!this.isActive) return;
    
    // Verificar si el click fue en el popup
    if (this.popup && this.popup.contains(e.target as Node)) {
      return;
    }
    
    // Verificar si el click fue en un overlay de resaltado
    const target = e.target as HTMLElement;
    if (target.classList.contains('pm-highlight-overlay')) {
      const highlightId = target.getAttribute('data-highlight-id');
      if (highlightId) {
        this.showRemovePopup(highlightId, e.clientX, e.clientY);
        return;
      }
    }

    const selection = window.getSelection();
    
    if (!selection || selection.isCollapsed || selection.toString().trim().length === 0) {
      this.hidePopup();
      this.selectedRange = null;
      return;
    }

    // Guardar el rango seleccionado
    this.selectedRange = selection.getRangeAt(0).cloneRange();
    
    // Mostrar popup cerca de la selección
    this.showPopup(selection);
  }

  /**
   * Muestra el popup de resaltado
   */
  private showPopup(selection: Selection) {
    this.hidePopup();

    const range = selection.getRangeAt(0);
    const rect = range.getBoundingClientRect();

    // Crear popup
    this.popup = document.createElement('div');
    this.popup.id = 'pm-highlight-popup';
    this.popup.className = 'pm-highlight-popup';

    // Contenido del popup
    this.popup.innerHTML = `
      <div class="pm-highlight-popup-title">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="m9 11-6 6v3h9l3-3"/>
          <path d="m22 12-4.6 4.6a2 2 0 0 1-2.8 0l-5.2-5.2a2 2 0 0 1 0-2.8L14 4"/>
        </svg>
        <span>Resaltar</span>
      </div>
      <div class="pm-highlight-colors">
        ${HIGHLIGHT_COLORS.map((c) => `
          <button 
            class="pm-highlight-color-btn" 
            data-color="${c.rgba}" 
            data-hex="${c.hex}"
            title="${c.name}"
            style="background: ${c.hex};"
          ></button>
        `).join('')}
      </div>
    `;

    // Posicionar el popup arriba de la selección
    const scrollY = window.scrollY;
    const scrollX = window.scrollX;
    
    let top = rect.top + scrollY - 70;
    let left = rect.left + scrollX + (rect.width / 2) - 100;

    if (top < scrollY + 10) {
      top = rect.bottom + scrollY + 10;
    }
    if (left < 10) left = 10;
    if (left + 200 > window.innerWidth) left = window.innerWidth - 210;

    this.popup.style.top = `${top}px`;
    this.popup.style.left = `${left}px`;

    // Agregar al DOM
    document.body.appendChild(this.popup);

    // Event listeners para los botones de color
    this.popup.querySelectorAll('.pm-highlight-color-btn').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const color = (btn as HTMLElement).getAttribute('data-color');
        if (color && this.selectedRange) {
          this.applyHighlight(this.selectedRange, color);
          this.hidePopup();
          // Limpiar selección
          window.getSelection()?.removeAllRanges();
        }
      });
    });

    // Animar entrada
    requestAnimationFrame(() => {
      if (this.popup) {
        this.popup.classList.add('visible');
      }
    });
  }

  /**
   * Muestra popup para quitar resaltado
   */
  private showRemovePopup(highlightId: string, x: number, y: number) {
    this.hidePopup();
    
    const highlight = this.highlights.find(h => h.id === highlightId);
    if (!highlight) return;
    
    // Crear popup
    this.popup = document.createElement('div');
    this.popup.id = 'pm-highlight-popup';
    this.popup.className = 'pm-highlight-popup';
    
    this.popup.innerHTML = `
      <div class="pm-highlight-popup-title">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="m9 11-6 6v3h9l3-3"/>
          <path d="m22 12-4.6 4.6a2 2 0 0 1-2.8 0l-5.2-5.2a2 2 0 0 1 0-2.8L14 4"/>
        </svg>
        <span>Resaltado</span>
      </div>
      <div class="pm-highlight-actions">
        <button class="pm-highlight-remove-btn" title="Quitar resaltado">
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M3 6h18"/>
            <path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/>
            <path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/>
          </svg>
          <span>Quitar</span>
        </button>
        <div class="pm-highlight-colors-mini">
          ${HIGHLIGHT_COLORS.map((c) => `
            <button 
              class="pm-highlight-color-btn-mini" 
              data-color="${c.rgba}" 
              title="Cambiar a ${c.name}"
              style="background: ${c.hex};"
            ></button>
          `).join('')}
        </div>
      </div>
    `;
    
    // Posicionar el popup
    const scrollY = window.scrollY;
    const scrollX = window.scrollX;
    
    let top = y + scrollY - 80;
    let left = x + scrollX - 100;
    
    if (top < scrollY + 10) {
      top = y + scrollY + 10;
    }
    if (left < 10) left = 10;
    if (left + 200 > window.innerWidth) left = window.innerWidth - 210;
    
    this.popup.style.top = `${top}px`;
    this.popup.style.left = `${left}px`;
    
    document.body.appendChild(this.popup);
    
    // Event listener para quitar resaltado
    this.popup.querySelector('.pm-highlight-remove-btn')?.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      this.removeHighlight(highlightId);
      this.hidePopup();
    });
    
    // Event listeners para cambiar color
    this.popup.querySelectorAll('.pm-highlight-color-btn-mini').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const color = (btn as HTMLElement).getAttribute('data-color');
        if (color) {
          this.changeHighlightColor(highlightId, color);
          this.hidePopup();
        }
      });
    });
    
    // Animar entrada
    requestAnimationFrame(() => {
      if (this.popup) {
        this.popup.classList.add('visible');
      }
    });
    
    // Cerrar popup al hacer click fuera
    const closeOnClickOutside = (e: MouseEvent) => {
      if (this.popup && !this.popup.contains(e.target as Node)) {
        this.hidePopup();
        document.removeEventListener('mousedown', closeOnClickOutside, true);
      }
    };
    
    setTimeout(() => {
      document.addEventListener('mousedown', closeOnClickOutside, true);
    }, 10);
  }

  /**
   * Oculta el popup
   */
  private hidePopup() {
    if (this.popup) {
      this.popup.remove();
      this.popup = null;
    }
  }

  /**
   * Guarda el estado actual para poder deshacer
   */
  private saveUndoState() {
    // Copiar el array de highlights
    this.undoStack.push(JSON.parse(JSON.stringify(this.highlights)));
    
    // Limitar el tamaño del stack de undo
    if (this.undoStack.length > 50) {
      this.undoStack.shift();
    }
  }

  /**
   * Aplica el resaltado al texto seleccionado
   */
  private applyHighlight(range: Range, color: string) {
    if (range.collapsed) return;

    // Guardar estado para undo
    this.saveUndoState();

    // Obtener los rects de la selección (coordenadas de viewport)
    const clientRects = Array.from(range.getClientRects());
    if (clientRects.length === 0) return;
    
    // Convertir a coordenadas de DOCUMENTO (absolutas)
    // Sumamos el scroll actual para obtener posición fija en el documento
    const scrollX = window.scrollX;
    const scrollY = window.scrollY;
    
    const documentRects = clientRects.map(r => ({
      left: r.left + scrollX,
      top: r.top + scrollY,
      width: r.width,
      height: r.height
    }));

    // Crear nuevo highlight con coordenadas de documento
    const highlight: HighlightRect = {
      id: `highlight-${++this.highlightIdCounter}`,
      rects: documentRects,
      color: color,
      text: range.toString()
    };

    this.highlights.push(highlight);
    this.renderOverlays();
  }

  /**
   * Elimina un resaltado
   */
  private removeHighlight(highlightId: string) {
    // Guardar estado para undo
    this.saveUndoState();
    
    this.highlights = this.highlights.filter(h => h.id !== highlightId);
    this.renderOverlays();
  }

  /**
   * Cambia el color de un resaltado
   */
  private changeHighlightColor(highlightId: string, newColor: string) {
    const highlight = this.highlights.find(h => h.id === highlightId);
    if (highlight) {
      // Guardar estado para undo
      this.saveUndoState();
      highlight.color = newColor;
      this.renderOverlays();
    }
  }

  /**
   * Renderiza todos los overlays de resaltado
   */
  private renderOverlays() {
    if (!this.overlayContainer) return;
    
    // Limpiar overlays existentes
    this.overlayContainer.innerHTML = '';
    
    // Los rects ya están en coordenadas de documento (absolutas)
    // No necesitamos sumar scroll porque el container es position: absolute
    this.highlights.forEach(highlight => {
      highlight.rects.forEach((rect) => {
        const overlay = document.createElement('div');
        overlay.className = 'pm-highlight-overlay';
        overlay.setAttribute('data-highlight-id', highlight.id);
        overlay.style.backgroundColor = highlight.color;
        overlay.style.left = `${rect.left}px`;
        overlay.style.top = `${rect.top}px`;
        overlay.style.width = `${rect.width}px`;
        overlay.style.height = `${rect.height}px`;
        
        this.overlayContainer!.appendChild(overlay);
      });
    });
  }


  /**
   * Inyecta los estilos del popup y overlays
   */
  private injectStyles() {
    if (document.getElementById('pm-highlight-styles')) return;

    const style = document.createElement('style');
    style.id = 'pm-highlight-styles';
    style.textContent = `
      /* Contenedor de overlays */
      .pm-highlight-overlay-container {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 999999990;
      }
      
      /* Overlay de resaltado individual */
      .pm-highlight-overlay {
        position: absolute;
        pointer-events: auto;
        cursor: pointer;
        border-radius: 2px;
        transition: filter 0.15s ease;
        mix-blend-mode: multiply;
      }
      
      .pm-highlight-overlay:hover {
        filter: brightness(1.1);
      }

      /* Popup de resaltado */
      .pm-highlight-popup {
        position: absolute;
        z-index: 2147483647;
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 8px 12px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        opacity: 0;
        transform: translateY(5px);
        transition: opacity 0.15s ease, transform 0.15s ease;
        pointer-events: auto;
      }

      .pm-highlight-popup.visible {
        opacity: 1;
        transform: translateY(0);
      }

      .pm-highlight-popup-title {
        display: flex;
        align-items: center;
        gap: 6px;
        color: rgba(255, 255, 255, 0.8);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 12px;
        font-weight: 500;
        margin-bottom: 8px;
        padding-bottom: 6px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      }

      .pm-highlight-popup-title svg {
        color: #FBBF24;
      }

      .pm-highlight-colors {
        display: flex;
        gap: 6px;
      }

      .pm-highlight-color-btn {
        width: 24px;
        height: 24px;
        border-radius: 50%;
        border: 2px solid rgba(255, 255, 255, 0.2);
        cursor: pointer;
        transition: transform 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease;
      }

      .pm-highlight-color-btn:hover {
        transform: scale(1.15);
        border-color: rgba(255, 255, 255, 0.6);
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
      }

      .pm-highlight-color-btn:active {
        transform: scale(1.05);
      }
      
      /* Estilos para el popup de acciones (quitar/cambiar color) */
      .pm-highlight-actions {
        display: flex;
        align-items: center;
        gap: 10px;
      }
      
      .pm-highlight-remove-btn {
        display: flex;
        align-items: center;
        gap: 4px;
        background: rgba(239, 68, 68, 0.2);
        border: 1px solid rgba(239, 68, 68, 0.4);
        color: #f87171;
        padding: 6px 10px;
        border-radius: 8px;
        font-size: 12px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        cursor: pointer;
        transition: all 0.15s ease;
      }
      
      .pm-highlight-remove-btn:hover {
        background: rgba(239, 68, 68, 0.3);
        border-color: rgba(239, 68, 68, 0.6);
      }
      
      .pm-highlight-colors-mini {
        display: flex;
        gap: 4px;
      }
      
      .pm-highlight-color-btn-mini {
        width: 18px;
        height: 18px;
        border-radius: 50%;
        border: 2px solid rgba(255, 255, 255, 0.2);
        cursor: pointer;
        transition: transform 0.15s ease, border-color 0.15s ease;
      }
      
      .pm-highlight-color-btn-mini:hover {
        transform: scale(1.15);
        border-color: rgba(255, 255, 255, 0.6);
      }
    `;

    document.head.appendChild(style);
  }

  /**
   * Elimina los estilos inyectados
   */
  private removeStyles() {
    const style = document.getElementById('pm-highlight-styles');
    if (style) style.remove();
  }

  /**
   * Debounce utility
   */
  private debounce<T extends (...args: unknown[]) => void>(fn: T, delay: number): (...args: Parameters<T>) => void {
    let timeoutId: ReturnType<typeof setTimeout>;
    return (...args: Parameters<T>) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => fn(...args), delay);
    };
  }
}
