import type { LaserPoint, ToolMode } from './types';

export class InputHandler {
  private canvas: HTMLCanvasElement;
  private isInputActive = false;
  private isBlockedByGesture = false;
  
  // Callbacks
  private onStart: (p: LaserPoint, isMultiTouch: boolean, isShift: boolean) => void;
  private onMove: (p: LaserPoint, isMultiTouch: boolean, isShift: boolean) => void;
  private onStop: () => void;
  
  // Config
  // We need to know current tool mode to allow selection movement without "drawing"
  // but simpler is: Handler sends events, Controller decides what to do.
  
  constructor(
    canvas: HTMLCanvasElement,
    onStart: (p: LaserPoint, isMultiTouch: boolean, isShift: boolean) => void,
    onMove: (p: LaserPoint, isMultiTouch: boolean, isShift: boolean) => void,
    onStop: () => void
  ) {
    this.canvas = canvas;
    this.onStart = onStart;
    this.onMove = onMove;
    this.onStop = onStop;
    
    this.init();
  }

  private init() {
    this.canvas.addEventListener('mousedown', this.boundStart, { passive: false });
    window.addEventListener('mousemove', this.boundMove, { passive: false });
    window.addEventListener('mouseup', this.boundStop);
    
    this.canvas.addEventListener('touchstart', this.boundStart, { passive: false });
    window.addEventListener('touchmove', this.boundMove, { passive: false });
    window.addEventListener('touchend', this.boundStop);
  }

  public destroy() {
    this.canvas.removeEventListener('mousedown', this.boundStart);
    window.removeEventListener('mousemove', this.boundMove);
    window.removeEventListener('mouseup', this.boundStop);
    this.canvas.removeEventListener('touchstart', this.boundStart);
    window.removeEventListener('touchmove', this.boundMove);
    window.removeEventListener('touchend', this.boundStop);
  }

  public setInputActive(active: boolean) {
    this.isInputActive = active;
    // CRITICAL: Prevent scrolling/zooming only when drawing
    this.canvas.style.pointerEvents = active ? 'auto' : 'none';
    // Allow panning with finger (scrolling) even when active, unless we intercept it in handlers
    this.canvas.style.touchAction = active ? 'pan-x pan-y' : 'auto';
  }

  private getPos(e: MouseEvent | TouchEvent): LaserPoint {
    const clientX = 'clientX' in e ? e.clientX : e.touches[0].clientX;
    const clientY = 'clientY' in e ? e.clientY : e.touches[0].clientY;
    
    // Convert to Document Absolute coordinates (PageX/Y)
    return {
      x: clientX + window.scrollX,
      y: clientY + window.scrollY,
    };
  }

  private boundStart = (e: MouseEvent | TouchEvent) => {
      if (this.isBlockedByGesture && 'touches' in e && e.touches.length === 1) {
         this.isBlockedByGesture = false;
      }
      
      const isMultiTouch = 'touches' in e && e.touches.length > 1;
      
      // Check for Apple Pencil (Stylus)
      let isStylus = false;
      let touchType = 'direct';
      
      if ('touches' in e && e.touches.length > 0) {
        const t = e.touches[0] as any; // Cast to any to access touchType
        if (t.touchType) {
            touchType = t.touchType;
            if (t.touchType === 'stylus') isStylus = true;
        }
      }

      if (!this.isInputActive || this.isBlockedByGesture) return;
      
      // LOGIC: Finger should SCROLL, Stylus should DRAW
      // If we are in a drawing mode (InputActive=true), we want to ignore finger touches
      // so the browser handles them (scrolling).
      // Exception: If the user explicitly wants to draw with finger?
      // For now, let's enforce: Stylus = Draw, Finger = Scroll (if supported)
      // If touchType is not supported (desktop/some android), we assume everything is a draw intention
      // unless it is multitouch.
      
      const supportsTouchType = 'touches' in e && e.touches.length > 0 && 'touchType' in (e.touches[0] as any);
      
      if (supportsTouchType && !isStylus) {
          // It is a finger (direct) on a device that distinguishes them.
          // Let it scroll. DO NOT capture.
            return;
      }

      // If it is Multitouch and not stylus, we already return above? 
      // strict multi-touch logic handles pinch-zoom
      if (isMultiTouch && !isStylus) {
          this.isBlockedByGesture = true;
          this.onStop();
          return;
      }

      // Capture for drawing
      if ('touches' in e && e.cancelable) {
          e.preventDefault(); 
      }
      
      const pos = this.getPos(e);
      const isShift = 'shiftKey' in e ? (e as MouseEvent).shiftKey : false;
      this.onStart(pos, isMultiTouch, isShift);
  };

  private boundMove = (e: MouseEvent | TouchEvent) => {
      const isMultiTouch = 'touches' in e && e.touches.length > 1;

      // Check for Apple Pencil or Stylus
      let isStylus = false;
      if ('touches' in e && e.touches.length > 0) {
        const t = e.touches[0] as any;
        if (t.touchType === 'stylus') isStylus = true;
      }
      
      const supportsTouchType = 'touches' in e && e.touches.length > 0 && 'touchType' in (e.touches[0] as any);

      if (!this.isInputActive || this.isBlockedByGesture) return;
      
      // LOGIC: Finger should SCROLL, Stylus should DRAW
      if (supportsTouchType && !isStylus) {
          return; // Allow scroll
      }

      if (isMultiTouch && !isStylus) {
          this.onStop();
          return;
      }
      
      if ('touches' in e && e.cancelable) {
          e.preventDefault(); 
      }
      
      // Optimization: Could throttle here if needed
      if ('touches' in e || (e as MouseEvent).buttons === 1) {
          // Only send move if touching or mouse down
           const pos = this.getPos(e);
           const isShift = 'shiftKey' in e ? (e as MouseEvent).shiftKey : false;
           this.onMove(pos, isMultiTouch && !isStylus, isShift);
      }
  };

  private boundStop = () => {
      this.isBlockedByGesture = false; 
      this.onStop();
  };
}
