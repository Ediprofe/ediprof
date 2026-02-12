/**
 * PDFInputHandler - Manejador de input específico para el visor de PDF
 * 
 * Diferencia clave con InputHandler original:
 * - Las coordenadas son relativas al contenido scrollable del contenedor del PDF
 * - Usa scrollLeft/Top del contenedor en lugar de window.scrollX/Y
 * - Resta la posición del contenedor (getBoundingClientRect) para compensar
 *   elementos como la toolbar que desplazan el contenedor
 * - Reenvía eventos de scroll (wheel) al contenedor para no bloquear el scroll
 */

import type { LaserPoint } from '../presentation/types';

export class PDFInputHandler {
  private canvas: HTMLCanvasElement;
  private pdfContainer: HTMLElement;
  private isInputActive = false;
  private isBlockedByGesture = false;
  private isDrawing = false;
  
  // Callbacks
  private onStart: (p: LaserPoint, isMultiTouch: boolean, isShift: boolean) => void;
  private onMove: (p: LaserPoint, isMultiTouch: boolean, isShift: boolean) => void;
  private onStop: () => void;
  
  constructor(
    canvas: HTMLCanvasElement,
    pdfContainer: HTMLElement,
    onStart: (p: LaserPoint, isMultiTouch: boolean, isShift: boolean) => void,
    onMove: (p: LaserPoint, isMultiTouch: boolean, isShift: boolean) => void,
    onStop: () => void
  ) {
    this.canvas = canvas;
    this.pdfContainer = pdfContainer;
    this.onStart = onStart;
    this.onMove = onMove;
    this.onStop = onStop;
    
    this.init();
  }

  private init() {
    // Mouse events: start on canvas, move/stop on window (for drawing outside canvas)
    this.canvas.addEventListener('mousedown', this.boundStart, { passive: false });
    window.addEventListener('mousemove', this.boundMove, { passive: false });
    window.addEventListener('mouseup', this.boundStop);
    
    // Touch events
    this.canvas.addEventListener('touchstart', this.boundStart, { passive: false });
    window.addEventListener('touchmove', this.boundMove, { passive: false });
    window.addEventListener('touchend', this.boundStop);
    window.addEventListener('touchcancel', this.boundStop);
    window.addEventListener('blur', this.boundStop);
    
    // CRITICAL: Forward wheel events to the PDF container so scrolling works
    // even when the canvas is on top capturing pointer events
    this.canvas.addEventListener('wheel', this.boundWheel, { passive: false });
  }

  public destroy() {
    this.canvas.removeEventListener('mousedown', this.boundStart);
    window.removeEventListener('mousemove', this.boundMove);
    window.removeEventListener('mouseup', this.boundStop);
    this.canvas.removeEventListener('touchstart', this.boundStart);
    window.removeEventListener('touchmove', this.boundMove);
    window.removeEventListener('touchend', this.boundStop);
    window.removeEventListener('touchcancel', this.boundStop);
    window.removeEventListener('blur', this.boundStop);
    this.canvas.removeEventListener('wheel', this.boundWheel);
  }

  public setInputActive(active: boolean) {
    this.isInputActive = active;
    // CRITICAL: Prevent scrolling/zooming only when drawing
    this.canvas.style.pointerEvents = active ? 'auto' : 'none';
    // Allow panning + pinch zoom even when active
    this.canvas.style.touchAction = active ? 'pan-x pan-y pinch-zoom' : 'auto';
  }

  /**
   * Convert mouse/touch coordinates to PDF document coordinates.
   * 
   * The key formula:
   *   docX = (clientX - containerRect.left) + container.scrollLeft
   *   docY = (clientY - containerRect.top) + container.scrollTop
   * 
   * - clientX/Y: position relative to browser viewport
   * - containerRect.left/top: where the container starts in the viewport
   *   (this accounts for the toolbar height, margins, etc.)
   * - scrollLeft/Top: how much the container has scrolled
   */
  private getPos(e: MouseEvent | TouchEvent): LaserPoint {
    const clientX = 'clientX' in e ? e.clientX : e.touches[0].clientX;
    const clientY = 'clientY' in e ? e.clientY : e.touches[0].clientY;
    
    const containerRect = this.pdfContainer.getBoundingClientRect();
    
    const x = (clientX - containerRect.left) + this.pdfContainer.scrollLeft;
    const y = (clientY - containerRect.top) + this.pdfContainer.scrollTop;
    
    return { x, y };
  }

  /**
   * Forward wheel events to the PDF container for scrolling.
   * This allows the user to scroll through the PDF even when 
   * a drawing tool is active and the canvas has pointer-events: auto.
   */
  private boundWheel = (e: WheelEvent) => {
    // Allow native browser zoom (Cmd/Ctrl + wheel)
    if (e.ctrlKey || e.metaKey) {
      return;
    }

    // Don't scroll while actively drawing
    if (this.isDrawing) {
      e.preventDefault();
      return;
    }
    
    // Forward the scroll to the PDF container
    e.preventDefault();
    this.pdfContainer.scrollBy({
      top: e.deltaY,
      left: e.deltaX,
      behavior: 'auto' // instant scroll for responsiveness
    });
  };

  private handleScrollbarAccess = (e: MouseEvent) => {
    if (!this.isInputActive || this.isDrawing) return;

    const rect = this.canvas.getBoundingClientRect();
    const edgeZone = 20;
    const nearRightEdge = e.clientX >= rect.right - edgeZone;
    const nearBottomEdge = e.clientY >= rect.bottom - edgeZone;
    const shouldPassThrough = nearRightEdge || nearBottomEdge;

    if (shouldPassThrough && this.canvas.style.pointerEvents !== 'none') {
      this.canvas.style.pointerEvents = 'none';
    } else if (!shouldPassThrough && this.canvas.style.pointerEvents === 'none') {
      this.canvas.style.pointerEvents = 'auto';
    }
  };

  private boundStart = (e: MouseEvent | TouchEvent) => {
    if (this.isBlockedByGesture && 'touches' in e && e.touches.length === 1) {
      this.isBlockedByGesture = false;
    }
    
    const isMultiTouch = 'touches' in e && e.touches.length > 1;
    
    let isStylus = false;
    let touchType = 'direct';
    
    if ('touches' in e && e.touches.length > 0) {
      const t = e.touches[0] as any;
      if (t.touchType) {
        touchType = t.touchType;
        if (t.touchType === 'stylus') isStylus = true;
      }
    }

    if (!this.isInputActive || this.isBlockedByGesture) return;

    if (!('touches' in e)) {
      const me = e as MouseEvent;
      const rect = this.canvas.getBoundingClientRect();
      const edgeZone = 20;
      if (me.clientX >= rect.right - edgeZone || me.clientY >= rect.bottom - edgeZone) {
        return;
      }
    }
    
    const supportsTouchType = 'touches' in e && e.touches.length > 0 && 'touchType' in (e.touches[0] as any);
    
    if (supportsTouchType && !isStylus) {
      // Finger touch on device that supports touchType → let it scroll
      return;
    }

    if (isMultiTouch && !isStylus) {
      this.isBlockedByGesture = true;
      this.onStop();
      return;
    }

    if ('touches' in e && e.cancelable) {
      e.preventDefault();
    }
    
    this.isDrawing = true;
    const pos = this.getPos(e);
    const isShift = 'shiftKey' in e ? (e as MouseEvent).shiftKey : false;
    this.onStart(pos, isMultiTouch, isShift);
  };

  private boundMove = (e: MouseEvent | TouchEvent) => {
    if (!('touches' in e)) {
      this.handleScrollbarAccess(e as MouseEvent);
    }

    const isMultiTouch = 'touches' in e && e.touches.length > 1;

    let isStylus = false;
    if ('touches' in e && e.touches.length > 0) {
      const t = e.touches[0] as any;
      if (t.touchType === 'stylus') isStylus = true;
    }
    
    const supportsTouchType = 'touches' in e && e.touches.length > 0 && 'touchType' in (e.touches[0] as any);

    if (!this.isInputActive || this.isBlockedByGesture) return;
    
    if (supportsTouchType && !isStylus) {
      return;
    }

    if (isMultiTouch && !isStylus) {
      this.onStop();
      return;
    }
    
    if ('touches' in e && e.cancelable) {
      e.preventDefault();
    }
    
    if ('touches' in e || (e as MouseEvent).buttons === 1) {
      const pos = this.getPos(e);
      const isShift = 'shiftKey' in e ? (e as MouseEvent).shiftKey : false;
      this.onMove(pos, isMultiTouch && !isStylus, isShift);
    }
  };

  private boundStop = () => {
    this.isBlockedByGesture = false;
    this.isDrawing = false;
    this.onStop();
  };
}
