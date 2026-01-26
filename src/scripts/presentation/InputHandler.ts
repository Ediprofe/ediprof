import type { LaserPoint, ToolMode } from './types';

export class InputHandler {
  private canvas: HTMLCanvasElement;
  private isInputActive = false;
  private isBlockedByGesture = false;
  
  // Callbacks
  private onStart: (p: LaserPoint, isMultiTouch: boolean) => void;
  private onMove: (p: LaserPoint, isMultiTouch: boolean) => void;
  private onStop: () => void;
  
  // Config
  // We need to know current tool mode to allow selection movement without "drawing"
  // but simpler is: Handler sends events, Controller decides what to do.
  
  constructor(
    canvas: HTMLCanvasElement,
    onStart: (p: LaserPoint, isMultiTouch: boolean) => void,
    onMove: (p: LaserPoint, isMultiTouch: boolean) => void,
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
    this.canvas.style.touchAction = active ? 'none' : 'auto';
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
      if ('touches' in e && e.touches.length > 0) {
        const t = e.touches[0] as any; // Cast to any to access touchType
        if (t.touchType === 'stylus') isStylus = true;
      }

      if (!this.isInputActive || this.isBlockedByGesture) return;
      
      // Allow multi-touch ONLY if it's not a stylus (stylus is precise)
      // or if we have strict multi-touch logic. 
      // Actually, if stylus is present, we should probably ignore "palm" touches?
      // simple logic: if stylus, trust it.
      if (isMultiTouch && !isStylus) {
          this.isBlockedByGesture = true;
          this.onStop();
          return;
      }

      if ('touches' in e && e.cancelable) {
          e.preventDefault(); 
      }
      
      const pos = this.getPos(e);
      this.onStart(pos, isMultiTouch);
  };

  private boundMove = (e: MouseEvent | TouchEvent) => {
      const isMultiTouch = 'touches' in e && e.touches.length > 1;

      // Check for Apple Pencil or Stylus
      let isStylus = false;
      if ('touches' in e && e.touches.length > 0) {
        const t = e.touches[0] as any;
        if (t.touchType === 'stylus' || t.touchType === 'direct') { 
            if (t.touchType === 'stylus') isStylus = true;
        }
      }

      if (!this.isInputActive || this.isBlockedByGesture) return;
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
           this.onMove(pos, isMultiTouch && !isStylus);
      }
  };

  private boundStop = () => {
      this.isBlockedByGesture = false; 
      this.onStop();
  };
}
