/**
 * Modo Presentación para Ediprofe
 *
 * Este módulo proporciona herramientas de anotación en pantalla:
 * - Puntero láser (efecto temporal)
 * - Lápiz (dibujo permanente)
 * - Flechas y rectángulos
 * - Selector de colores
 *
 * OPTIMIZACIÓN RENDIMIENTO:
 * El canvas ahora es position: fixed (tamaño viewport) para evitar crear superficies gigantes.
 * Para simular que se dibuja sobre el documento, usamos coordenadas absolutas (PageX/Y)
 * y aplicamos una traslación al contexto del canvas basada en el scroll actual.
 */

interface LaserPoint {
  x: number;
  y: number;
}

interface LaserStroke {
  points: LaserPoint[];
  isDead: boolean;
  isPermanent?: boolean;
  color: string;
  type?: 'line' | 'arrow' | 'rect' | 'highlighter';
  isSelected?: boolean;
  minX?: number;
  maxX?: number;
  minY?: number;
  maxY?: number;
}

class LaserPointer {
  private canvas: HTMLCanvasElement;
  public ctx: CanvasRenderingContext2D;
  private strokes: LaserStroke[] = [];
  private currentStroke: LaserStroke | null = null;
  public isInputActive = false;
  private systemRunning = false;
  private toolMode: 'laser' | 'pen' | 'arrow' | 'rect' | 'highlighter' | 'select' = 'laser';
  private currentColor: string = '#EF4444'; // Red default
  private selectionBox: { x: number, y: number, w: number, h: number } | null = null;
  private isSelecting = false;
  private rafId: number | null = null;
  private lastGlobalActivityTime: number = Date.now();
  private duration = 3000;
  private isBlockedByGesture = false;
  private resizeObserver: ResizeObserver | null = null;

  constructor(canvas: HTMLCanvasElement) {
    this.canvas = canvas;
    this.ctx = this.canvas.getContext('2d', { alpha: true })!;
    this.init();
  }



  // Event handlers bound properties for cleanup
  private boundResize = () => this.resize();
  private boundStart = (e: MouseEvent | TouchEvent) => this.handleStart(e);
  private boundMove = (e: MouseEvent | TouchEvent) => this.handleMove(e);
  private boundStop = () => this.handleStop();

  private init() {
    window.addEventListener('resize', this.boundResize);
    
    // Watch for content size changes (e.g. accordions opening)
    this.resizeObserver = new ResizeObserver(() => this.resize());
    this.resizeObserver.observe(document.body);

    this.resize();

    this.canvas.addEventListener('mousedown', this.boundStart, { passive: false });
    window.addEventListener('mousemove', this.boundMove, { passive: false });
    window.addEventListener('mouseup', this.boundStop);
    
    this.canvas.addEventListener('touchstart', this.boundStart, { passive: false });
    window.addEventListener('touchmove', this.boundMove, { passive: false });
    window.addEventListener('touchend', this.boundStop);

    // CRITICAL: Repaint on scroll to keep drawings in sync with document
    window.addEventListener('scroll', this.boundDrawOnScroll, { passive: true });
  }

  private boundDrawOnScroll = () => {
      if (this.systemRunning) requestAnimationFrame(() => this.draw());
  };

  public destroy() {
    this.stopSystem();
    window.removeEventListener('resize', this.boundResize);
    this.resizeObserver?.disconnect();
    this.canvas.removeEventListener('mousedown', this.boundStart);
    window.removeEventListener('mousemove', this.boundMove);
    window.removeEventListener('mouseup', this.boundStop);
    this.canvas.removeEventListener('touchstart', this.boundStart);
    window.removeEventListener('touchmove', this.boundMove);
    window.removeEventListener('touchend', this.boundStop);
    window.removeEventListener('scroll', this.boundDrawOnScroll);
  }

  private getPos(e: MouseEvent | TouchEvent) {
    // Get viewport coordinates
    const clientX = 'clientX' in e ? e.clientX : e.touches[0].clientX;
    const clientY = 'clientY' in e ? e.clientY : e.touches[0].clientY;
    
    // Convert to Document Absolute coordinates (PageX/Y)
    // We store points in absolute coordinates so they "stick" to the content
    return {
      x: clientX + window.scrollX,
      y: clientY + window.scrollY,
    };
  }



  private handleStart(e: MouseEvent | TouchEvent) {
    // If block is stuck, reset it if 1 finger
    if (this.isBlockedByGesture && 'touches' in e && e.touches.length === 1) {
         this.isBlockedByGesture = false;
    }

    if (!this.isInputActive || this.isBlockedByGesture) return;
    if ('touches' in e && e.touches.length > 1) {
      this.isBlockedByGesture = true;
      this.handleStop();
      return;
    }

    if ('touches' in e) {
      // Prevent scrolling while drawing
       if (e.cancelable) e.preventDefault(); 
    }
    
    const { x, y } = this.getPos(e);
    this.lastGlobalActivityTime = Date.now();

    if (this.toolMode === 'select') {
      this.isSelecting = true;
      this.selectionBox = { x, y, w: 0, h: 0 };
      // Deselect all on new selection start unless shift is held (simple behavior for now: clear selection)
      this.strokes.forEach(s => s.isSelected = false);
      this.draw();
      return;
    }

    this.currentStroke = {
      points: [{ x, y }],
      isDead: false,
      isPermanent: this.toolMode === 'pen' || this.toolMode === 'arrow' || this.toolMode === 'rect' || this.toolMode === 'highlighter',
      color: this.toolMode === 'laser' ? '#FF0055' : this.currentColor,
      type: this.toolMode === 'arrow' ? 'arrow' : this.toolMode === 'rect' ? 'rect' : this.toolMode === 'highlighter' ? 'highlighter' : 'line',
    };
    this.strokes.push(this.currentStroke);
  }

  private handleMove(e: MouseEvent | TouchEvent) {
    // START CRITICAL FIX: Allow move if selecting OR if currentStroke exists
    if (!this.isInputActive || this.isBlockedByGesture) return;
    if (!this.currentStroke && !this.isSelecting) return;
    // END CRITICAL FIX
    if ('touches' in e && e.touches.length > 1) {
      this.handleStop();
      return;
    }
    
    if ('touches' in e && e.cancelable) {
       e.preventDefault(); 
    }

    const { x, y } = this.getPos(e);
    this.lastGlobalActivityTime = Date.now();

    if (this.toolMode === 'select') {
      if (this.isSelecting && this.selectionBox) {
         this.selectionBox.w = x - this.selectionBox.x;
         this.selectionBox.h = y - this.selectionBox.y;
         this.draw();
      }
      return;
    }

    if (this.currentStroke.type === 'arrow' || this.currentStroke.type === 'rect') {
      this.currentStroke.points = [this.currentStroke.points[0], { x, y }];
    } else {
      this.currentStroke.points.push({ x, y });
      // Don't shift logic here for simple strokes, keeps history better for selection
      // if (this.currentStroke.points.length > 800) this.currentStroke.points.shift();
    }
  }

  private handleStop() {
    if (this.toolMode === 'select' && this.isSelecting && this.selectionBox) {
        // Finalize selection
        this.computeSelection();
        this.isSelecting = false;
        this.selectionBox = null;
        this.draw();
        return;
    }

    if (this.currentStroke) {
        // Cache BBox for selection efficiency
        let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
        this.currentStroke.points.forEach(p => {
             if (p.x < minX) minX = p.x;
             if (p.x > maxX) maxX = p.x;
             if (p.y < minY) minY = p.y;
             if (p.y > maxY) maxY = p.y;
        });
        this.currentStroke.minX = minX;
        this.currentStroke.maxX = maxX;
        this.currentStroke.minY = minY;
        this.currentStroke.maxY = maxY;
    }

    this.currentStroke = null;
    this.isBlockedByGesture = false; 
    this.lastGlobalActivityTime = Date.now();
  }

  private computeSelection() {
      if (!this.selectionBox) return;
      
      // Normalize rect
      const rx = Math.min(this.selectionBox.x, this.selectionBox.x + this.selectionBox.w);
      const ry = Math.min(this.selectionBox.y, this.selectionBox.y + this.selectionBox.h);
      const rw = Math.abs(this.selectionBox.w);
      const rh = Math.abs(this.selectionBox.h);

      this.strokes.forEach(s => {
          if (!s.isPermanent) return; // Don't select laser
          
          // Fast BBox check
          // If stroke bbox intersects selection rect
          const sMinX = s.minX ?? -Infinity;
          const sMaxX = s.maxX ?? Infinity;
          const sMinY = s.minY ?? -Infinity;
          const sMaxY = s.maxY ?? Infinity;

          const intersects = !(sMaxX < rx || sMinX > rx + rw || sMaxY < ry || sMinY > ry + rh);
           
          if (intersects) {
              s.isSelected = true;
          }
      });
  }

  public setGestureBlock(state: boolean) {
    this.isBlockedByGesture = state;
    if (state) this.currentStroke = null;
  }

  public resize() {
    const dpr = window.devicePixelRatio || 1;
    // PERFORMANCE FIX: Use Viewport size (fixed), not Document size.
    // Huge canvases (e.g. 4000px height) cause massive lag on tablets/lower-end GPUs.
    const width = window.innerWidth;
    const height = window.innerHeight;

    if (this.canvas.width !== width * dpr || this.canvas.height !== height * dpr) {
        this.canvas.width = width * dpr;
        this.canvas.height = height * dpr;
        // CSS dimensions match viewport
        this.canvas.style.width = width + 'px';
        this.canvas.style.height = height + 'px';
        
        // Context scaling handled in draw() now to account for scroll translation per frame
        // this.ctx.scale(dpr, dpr); <-- Removed, done in draw()
        this.draw(); 
    }
  }

  public startSystem() {
    if (this.systemRunning) return;
    this.systemRunning = true;
    this.startLoop();
  }

  public stopSystem() {
    this.systemRunning = false;
    this.isInputActive = false;
    this.clearAll();
    if (this.rafId) cancelAnimationFrame(this.rafId);
    this.rafId = null;
  }

  public setDrawingEnabled(enabled: boolean) {
    this.isInputActive = enabled;
    // CRITICAL: Only block interaction with the underlying page if we are actually drawing (pen/laser/shapes)
    // If enabled is false (Hand mode), we allow clicks to pass through to the page (pointer-events: none)
    this.canvas.style.pointerEvents = enabled ? 'auto' : 'none';
    
    // CRITICAL FIX: Prevent browser default gestures (scrolling/zoom) ONLY when drawing
    this.canvas.style.touchAction = enabled ? 'none' : 'auto';
  }

  public setMode(mode: 'laser' | 'pen' | 'arrow' | 'rect' | 'highlighter' | 'select') {
    this.toolMode = mode;
  }

  public setColor(color: string) {
    this.currentColor = color;
  }

  public undo() {
    if (this.strokes.length === 0) return;

    // Check the last stroke added
    const lastStroke = this.strokes[this.strokes.length - 1];

    if (!lastStroke.isPermanent) {
      // SCENARIO 1: The user used the Laser.
      this.strokes = this.strokes.filter(s => s.isPermanent);
    } else {
      // SCENARIO 2: Permanent stroke.
      this.strokes.pop();
    }
    
    this.lastGlobalActivityTime = Date.now();
    this.draw();
  }

  public deleteSelected() {
     const initialCount = this.strokes.length;
     this.strokes = this.strokes.filter(s => !s.isSelected);
     if (this.strokes.length !== initialCount) {
         this.draw();
     }
  }


  public clearAll() {
    this.strokes = [];
    this.lastGlobalActivityTime = 0;
    this.clearCanvas();
  }

  private startLoop() {
    const loop = () => {
      if (!this.systemRunning) return;
      this.update();
      this.draw();
      this.rafId = requestAnimationFrame(loop);
    };
    this.rafId = requestAnimationFrame(loop);
  }

  private update() {
    const now = Date.now();
    const timeSinceLastActivity = this.currentStroke ? 0 : now - this.lastGlobalActivityTime;
    if (timeSinceLastActivity > this.duration) {
      this.strokes = this.strokes.filter((s) => s.isPermanent);
    }
  }

  public clearCanvas() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
  }

  private draw() {
    this.clearCanvas();
    /*
    if (this.strokes.length === 0) return; // Removed optimization to ensure clearCanvas runs on scroll
    */
    const now = Date.now();
    const idleTime = this.currentStroke ? 0 : now - this.lastGlobalActivityTime;
    const globalAlpha = Math.max(0, 1 - idleTime / this.duration);

    // PERFORMANCE & SYNC LOGIC:
    // 1. Reset transform to Identity to clear full viewport
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // 2. Apply Transform: Scale (DPI) + Translate (-Scroll)
    // This projects our Absolute World Coordinates (points) onto the Fixed Viewport Canvas
    const dpr = window.devicePixelRatio || 1;
    const scrollX = window.scrollX;
    const scrollY = window.scrollY;
    
    // Matrix: [scaleX, skewY, skewX, scaleY, translateX, translateY]
    // We translate by -scroll * dpr because the coordinate system is scaled
    this.ctx.setTransform(dpr, 0, 0, dpr, -scrollX * dpr, -scrollY * dpr);

    // Scale for stroke width consistency
    const scale = window.visualViewport?.scale || 1;
    // Effective scale factor for widths
    const s = 1 / scale; 

    if (this.strokes.length > 0) {
      this.strokes.forEach((stroke) => {
        // Selection highlight
        if (stroke.isSelected) {
            // Draw a bounding box or glow around it
            // Simplified: Draw it again with a broad transparent blue stroke underneath
            const selColor = 'rgba(59, 130, 246, 0.5)'; // Blue 50%
            // Only for pen/highlighter. For Arrow/Rect we might need logic, but simpler to just re-render slightly larger
            if(stroke.type !== 'rect' && stroke.type !== 'arrow') {
                this.renderStroke(stroke.points, selColor, (stroke.type === 'highlighter' ? 30 : 10) * s, 0, 'source-over');
            }
        }

        if (stroke.points.length < 2) return;
        const alpha = stroke.isPermanent ? (stroke.type === 'highlighter' ? 0.4 : 1.0) : globalAlpha;
        if (alpha <= 0) return;

        if (stroke.isPermanent) {
          const rgb = this.hexToRgb(stroke.color);
          const colorStr = `rgba(${rgb}, ${alpha})`;

          if (stroke.type === 'arrow') {
             if (stroke.isSelected) this.renderArrow(stroke.points[0], stroke.points[1], 'rgba(59, 130, 246, 0.5)', 12 * s);
            this.renderArrow(stroke.points[0], stroke.points[1], colorStr, 4 * s);
          } else if (stroke.type === 'rect') {
             if (stroke.isSelected) this.renderRect(stroke.points[0], stroke.points[1], 'rgba(59, 130, 246, 0.5)', 12 * s);
            this.renderRect(stroke.points[0], stroke.points[1], colorStr, 4 * s);
          } else if (stroke.type === 'highlighter') {
            this.renderStroke(stroke.points, colorStr, 24 * s, 0, 'source-over');
          } else {
            this.renderStroke(stroke.points, colorStr, 4 * s, 0, 'source-over');
          }
        } else {
          // Laser
          this.renderStroke(stroke.points, `rgba(255, 0, 0, ${alpha * 0.3})`, 25 * s, 30 * s, 'lighter');
          this.renderStroke(stroke.points, `rgba(255, 0, 0, ${alpha * 0.8})`, 8 * s, 10 * s, 'lighter');
          this.renderStroke(stroke.points, `rgba(255, 255, 255, ${alpha * 0.95})`, 3 * s, 0, 'source-over');
        }
      });
    }

    // Draw active Selection Box
    if (this.isSelecting && this.selectionBox) {
        this.ctx.globalCompositeOperation = 'source-over';
        this.ctx.strokeStyle = '#3b82f6'; // Bright Blue
        this.ctx.lineWidth = 2 * s; // Thicker line
        
        // Draw Solid Rectangle (not dotted, user requested "rectangulo no un cuadrado" - logic is fine, styling preference)
        // User complained about "ningun nada punteado", so let's make it solid and clear.
        // Also "debe ser un rectangulo no un cuadrado" -> our logic supports rects, maybe visual feedback was small.
        
        this.ctx.strokeRect(this.selectionBox.x, this.selectionBox.y, this.selectionBox.w, this.selectionBox.h);
        
        this.ctx.fillStyle = 'rgba(59, 130, 246, 0.2)'; // More visible fill
        this.ctx.fillRect(this.selectionBox.x, this.selectionBox.y, this.selectionBox.w, this.selectionBox.h);
    }
  }

  private hexToRgb(hex: string): string {
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    return `${r}, ${g}, ${b}`;
  }

  private renderStroke(pts: LaserPoint[], color: string, width: number, blur: number, composite: string) {
    this.ctx.globalCompositeOperation = composite as GlobalCompositeOperation;
    this.ctx.beginPath();
    this.ctx.strokeStyle = color;
    this.ctx.lineWidth = width;
    this.ctx.lineCap = 'round';
    this.ctx.lineJoin = 'round';
    this.ctx.shadowBlur = blur;
    this.ctx.shadowColor = color;
    this.ctx.moveTo(pts[0].x, pts[0].y);
    for (let i = 1; i < pts.length - 1; i++) {
      const midX = (pts[i].x + pts[i + 1].x) / 2;
      const midY = (pts[i].y + pts[i + 1].y) / 2;
      this.ctx.quadraticCurveTo(pts[i].x, pts[i].y, midX, midY);
    }
    this.ctx.stroke();
  }

  private renderArrow(from: LaserPoint, to: LaserPoint, color: string, width: number) {
    const headlen = 15;
    const angle = Math.atan2(to.y - from.y, to.x - from.x);

    this.ctx.globalCompositeOperation = 'source-over';
    this.ctx.beginPath();
    this.ctx.strokeStyle = color;
    this.ctx.lineWidth = width;
    this.ctx.lineCap = 'round';
    this.ctx.lineJoin = 'round';
    this.ctx.shadowBlur = 0;

    this.ctx.moveTo(from.x, from.y);
    this.ctx.lineTo(to.x, to.y);
    this.ctx.moveTo(to.x, to.y);
    this.ctx.lineTo(to.x - headlen * Math.cos(angle - Math.PI / 6), to.y - headlen * Math.sin(angle - Math.PI / 6));
    this.ctx.moveTo(to.x, to.y);
    this.ctx.lineTo(to.x - headlen * Math.cos(angle + Math.PI / 6), to.y - headlen * Math.sin(angle + Math.PI / 6));

    this.ctx.stroke();
  }

  private renderRect(from: LaserPoint, to: LaserPoint, color: string, width: number) {
    this.ctx.globalCompositeOperation = 'source-over';
    this.ctx.beginPath();
    this.ctx.strokeStyle = color;
    this.ctx.lineWidth = width;
    this.ctx.lineCap = 'round';
    this.ctx.lineJoin = 'round';
    this.ctx.shadowBlur = 0;

    const x = Math.min(from.x, to.x);
    const y = Math.min(from.y, to.y);
    const w = Math.abs(to.x - from.x);
    const h = Math.abs(to.y - from.y);

    this.ctx.strokeRect(x, y, w, h);
  }
}

// Estado global del modo presentación
let isInitialized = false;
let laserPointer: LaserPointer | null = null;
let currentTool: 'hand' | 'laser' | 'pen' | 'arrow' | 'rect' | 'highlighter' | 'select' = 'hand';
let currentBoard: 'none' | 'white' | 'black' = 'none';

function createDockHTML(): string {
  return `
    <div id="presentation-board" class="presentation-board"></div>
    <canvas id="presentation-canvas" class="presentation-canvas"></canvas>
    <div class="presentation-dock-wrapper" id="presentation-dock">
      <div class="presentation-glass-dock">
        <div class="dock-section tools">
          <button id="pm-hand-btn" class="dock-btn tool-trigger active" title="Puntero (H)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m3 3 7.07 16.97 2.51-7.39 7.39-2.51L3 3z"></path><path d="m13 13 6 6"></path></svg>
            <span>Puntero</span>
          </button>
           <button id="pm-select-btn" class="dock-btn tool-trigger" title="Seleccionar (S)">
             <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg>
            <span>Selecc.</span>
          </button>
          <button id="pm-arrow-btn" class="dock-btn tool-trigger" title="Flecha (A)">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            <span>Flecha</span>
          </button>
          <button id="pm-rect-btn" class="dock-btn tool-trigger" title="Rect (R)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"></rect></svg>
            <span>Rect</span>
          </button>
          <button id="pm-laser-btn" class="dock-btn tool-trigger" title="Láser (L)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m13.4 2 3.5 3.5-3.5 3.5-3.5-3.5z"></path><path d="M7.4 15.6 2 21"></path><path d="m15.5 15.5 4-4"></path><path d="M14 17h5"></path><path d="M17 14v5"></path><path d="m7.4 9.4 6.2 6.2"></path></svg>
            <span>Láser</span>
          </button>
          <button id="pm-pen-btn" class="dock-btn tool-trigger" title="Lápiz (P)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"></path><path d="m15 5 4 4"></path></svg>
            <span>Lápiz</span>
          </button>
          <button id="pm-highlighter-btn" class="dock-btn tool-trigger" title="Resaltador (M)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m9 11-6 6v3h9l3-3"/><path d="m22 12-4.6 4.6a2 2 0 0 1-2.8 0l-5.2-5.2a2 2 0 0 1 0-2.8L14 4"/></svg>
            <span>Resaltar</span>
          </button>
        </div>
        <div class="dock-divider"></div>
        <div id="pm-colors" class="dock-section colors">
          <button class="color-dot" data-color="#FFFFFF" title="Blanco (1)" style="background: #FFFFFF;"></button>
          <button class="color-dot" data-color="#FFD700" title="Amarillo (2)" style="background: #FFD700;"></button>
          <button class="color-dot active" data-color="#EF4444" title="Rojo (3)" style="background: #EF4444;"></button>
          <button class="color-dot" data-color="#3B82F6" title="Azul (4)" style="background: #3B82F6;"></button>
          <button class="color-dot" data-color="#111111" title="Negro (5)" style="background: #111111; border: 1px solid rgba(255,255,255,0.4)"></button>
          <button class="color-dot" data-color="#00FF99" title="Neon Green (6)" style="background: #00FF99; border: 1px solid rgba(255,255,255,0.2)"></button>
        </div>
        <div class="dock-divider"></div>
        <div class="dock-section actions">
          <button id="pm-undo-btn" class="dock-btn" title="Deshacer (Ctrl+Z)">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7v6h6"></path><path d="M21 17a9 9 0 0 0-9-9 9 9 0 0 0-6 2.3L3 13"></path></svg>
          </button>
          <button id="pm-clear-btn" class="dock-btn" title="Limpiar (C)">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"></path><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"></path><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg>
          </button>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </button>
        </div>
        <div class="dock-divider"></div>
        <div class="dock-section boards">
          <button id="pm-board-white" class="dock-btn" title="Pizarra Blanca (W)">
             <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><line x1="3" x2="21" y1="9" y2="9"/><line x1="9" x2="9" y1="21" y2="9"/></svg>
          </button>
          <button id="pm-board-black" class="dock-btn" title="Pizarra Negra (B)">
             <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/></svg>
          </button>
        </div>
      </div>
    </div>
  `;
}

function createStyles(): string {
  return `
    <style id="presentation-mode-styles">
      .presentation-canvas {
        position: fixed; /* FIXED again for performance */
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 999999998;
        pointer-events: none;
        will-change: transform;
        touch-action: none;
      }
      .presentation-board {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 999999997; /* Behind canvas */
        pointer-events: none;
        opacity: 0;
        background-color: transparent;
        transition: opacity 0.3s ease, background-color 0.3s ease;
      }
      /* Whiteboard Grid */
      .presentation-board.white {
        opacity: 1;
        pointer-events: auto; /* Catch clicks */
        background-color: #ffffff;
        background-image: 
          linear-gradient(#e5e7eb 1px, transparent 1px),
          linear-gradient(90deg, #e5e7eb 1px, transparent 1px);
        background-size: 40px 40px;
      }
      /* Blackboard Grid */
      .presentation-board.black {
        opacity: 1;
        pointer-events: auto;
        background-color: #1a1a1a;
        background-image: 
          linear-gradient(#333 1px, transparent 1px),
          linear-gradient(90deg, #333 1px, transparent 1px);
        background-size: 40px 40px;
      }
      .presentation-canvas.active {
        pointer-events: auto;
        cursor: crosshair;
      }
      .presentation-dock-wrapper {
        position: fixed;
        /* Reset positioning for JS control via Visual Viewport API */
        top: 0;
        left: 0;
        width: auto;
        display: flex;
        justify-content: center;
        z-index: 999999999;
        /* Remove CSS animation and transforms, we handle them in JS now */
        transform-origin: 0 0;
        will-change: transform;
      }
      
      /* ... keep existing glass dock styles ... */
      .presentation-glass-dock {
        background: rgba(15, 23, 42, 0.9);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 8px 16px;
        border-radius: 24px;
        display: flex;
        align-items: center;
        gap: 10px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
      }
      .dock-section {
        display: flex;
        align-items: center;
        gap: 8px;
      }
      .dock-divider {
        width: 1px;
        height: 24px;
        background: rgba(255, 255, 255, 0.15);
        margin: 0 4px;
      }
      .dock-btn {
        background: transparent;
        border: 1px solid transparent;
        color: rgba(255, 255, 255, 0.7);
        padding: 0 10px;
        height: 40px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.2s;
        gap: 8px;
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 0.8rem;
        font-weight: 500;
      }
      .dock-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        color: white;
      }
      .dock-btn-close:hover {
        background: rgba(239, 68, 68, 0.3);
        color: #fca5a5;
      }
      .tool-trigger.active {
        background: #2563eb;
        color: white;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
      }
      #pm-laser-btn.active {
        background: #ef4444;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
      }
      #pm-pen-btn.active {
        background: #eab308;
        box-shadow: 0 4px 12px rgba(234, 179, 8, 0.3);
      }
      #pm-arrow-btn.active {
        background: #10b981;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
      }
      #pm-rect-btn.active {
        background: #6366f1;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
      }
      #pm-select-btn.active {
        background: #8b5cf6;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
      }
      #pm-highlighter-btn.active {
        background: #facc15;
        color: #000;
        box-shadow: 0 4px 12px rgba(250, 204, 21, 0.3);
      }
      .colors { gap: 8px; }
      .color-dot {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        border: 2px solid rgba(255, 255, 255, 0.2);
        cursor: pointer;
        transition: all 0.2s;
        padding: 0;
      }
      .color-dot:hover {
        transform: scale(1.15);
        border-color: rgba(255, 255, 255, 0.5);
      }
      .color-dot.active {
        border-color: white;
        transform: scale(1.25);
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
      }
      @media (max-width: 768px) {
        .dock-btn span { display: none; }
        .dock-btn { padding: 0 4px; height: 32px; }
        .presentation-glass-dock { 
          padding: 4px 6px; 
          gap: 1px; 
          /* Scale down more on mobile */
          transform: scale(0.75);
          transform-origin: bottom center;
        }
        .color-dot { width: 16px; height: 16px; }
        .dock-divider { margin: 0 2px; height: 16px; }
        .dock-section { gap: 2px; }
        /* Hide complex diagram tools on mobile to prioritize space */
        #pm-arrow-btn, #pm-rect-btn { display: none; }
      }

      /* Animación suave al activar/desactivar */
      .lesson-content,
      .content-article {
        transition: all 0.3s ease-out;
      }
    </style>
  `;
}

function setTool(tool: 'hand' | 'laser' | 'pen' | 'arrow' | 'rect' | 'highlighter' | 'select') {
  if (!laserPointer) return;

  currentTool = tool;
  laserPointer.setDrawingEnabled(tool !== 'hand');
  if (tool !== 'hand') {
    laserPointer.setMode(tool as 'laser' | 'pen' | 'arrow' | 'rect' | 'highlighter' | 'select');
  }

  const canvas = document.getElementById('presentation-canvas');
  canvas?.classList.toggle('active', tool !== 'hand');

  // Actualizar estados de botones
  document.getElementById('pm-hand-btn')?.classList.toggle('active', tool === 'hand');
  document.getElementById('pm-select-btn')?.classList.toggle('active', tool === 'select');
  document.getElementById('pm-laser-btn')?.classList.toggle('active', tool === 'laser');
  document.getElementById('pm-pen-btn')?.classList.toggle('active', tool === 'pen');
  document.getElementById('pm-arrow-btn')?.classList.toggle('active', tool === 'arrow');
  document.getElementById('pm-rect-btn')?.classList.toggle('active', tool === 'rect');
  document.getElementById('pm-highlighter-btn')?.classList.toggle('active', tool === 'highlighter');
}

function toggleBoard(type: 'white' | 'black') {
  const board = document.getElementById('presentation-board');
  const whiteBtn = document.getElementById('pm-board-white');
  const blackBtn = document.getElementById('pm-board-black');
  
  if (!board) return;

  // Toggle off if clicking same board
  if (currentBoard === type) {
    currentBoard = 'none';
    board.className = 'presentation-board';
    whiteBtn?.classList.remove('active');
    blackBtn?.classList.remove('active');
  } else {
    currentBoard = type;
    board.className = `presentation-board ${type}`;
    
    // Update UI buttons
    whiteBtn?.classList.toggle('active', type === 'white');
    blackBtn?.classList.toggle('active', type === 'black');
    
    // UX: Auto-switch color for contrast
    if (type === 'white') {
        document.body.style.overflow = 'hidden'; // Lock scroll for board mode
        // Switch to black pen if current is white or very light
        const color = '#111111';
        laserPointer?.setColor(color);
        // ... update UI ...
        document.querySelectorAll('#pm-colors .color-dot').forEach((d) => {
          if (d.getAttribute('data-color') === color) d.classList.add('active');
          else d.classList.remove('active');
        });
    } else if (type === 'black') {
        document.body.style.overflow = 'hidden'; // Lock scroll for board mode
        // Switch to white pen
        const color = '#FFFFFF';
        laserPointer?.setColor(color);
         document.querySelectorAll('#pm-colors .color-dot').forEach((d) => {
          if (d.getAttribute('data-color') === color) d.classList.add('active');
          else d.classList.remove('active');
        });
    } else {
        document.body.style.overflow = ''; // Unlock scroll
    }
  }
}


function setupEventListeners() {
  document.getElementById('pm-hand-btn')?.addEventListener('click', () => setTool('hand'));
  document.getElementById('pm-select-btn')?.addEventListener('click', () => setTool('select'));
  document.getElementById('pm-laser-btn')?.addEventListener('click', () => setTool('laser'));
  document.getElementById('pm-pen-btn')?.addEventListener('click', () => setTool('pen'));
  document.getElementById('pm-arrow-btn')?.addEventListener('click', () => setTool('arrow'));
  document.getElementById('pm-rect-btn')?.addEventListener('click', () => setTool('rect'));
  document.getElementById('pm-highlighter-btn')?.addEventListener('click', () => setTool('highlighter'));
  document.getElementById('pm-clear-btn')?.addEventListener('click', () => {
    laserPointer?.clearAll();
    setTool('hand'); // UX Improvement: Auto-switch to hand after clearing
  });
  document.getElementById('pm-undo-btn')?.addEventListener('click', () => laserPointer?.undo());
  document.getElementById('pm-close-btn')?.addEventListener('click', () => closePresentationMode());
  document.getElementById('pm-board-white')?.addEventListener('click', () => toggleBoard('white'));
  document.getElementById('pm-board-black')?.addEventListener('click', () => toggleBoard('black'));

  // Colores
  document.querySelectorAll('#pm-colors .color-dot').forEach((dot) => {
    dot.addEventListener('click', () => {
      const color = dot.getAttribute('data-color') || '#FFFFFF';
      laserPointer?.setColor(color);
      document.querySelectorAll('#pm-colors .color-dot').forEach((d) => d.classList.remove('active'));
      dot.classList.add('active');
      
      // Solo cambiar a lápiz si no estamos ya usando una herramienta de dibujo (flecha, rect, resaltador)
      if (currentTool === 'hand' || currentTool === 'laser' || currentTool === 'select') {
        setTool('pen');
      }
    });
  });

  // Helper para cambiar color desde teclado
  const setColorFromKey = (color: string) => {
    laserPointer?.setColor(color);
    document.querySelectorAll('#pm-colors .color-dot').forEach((d) => {
      if (d.getAttribute('data-color') === color) d.classList.add('active');
      else d.classList.remove('active');
    });
    
    // Maintain current tool if it is a shape or highlighter
    if (currentTool === 'hand' || currentTool === 'laser' || currentTool === 'select') {
      setTool('pen');
    }
  };

  // Atajos de teclado
  const handleKeyDown = (e: KeyboardEvent) => {
    if (!isInitialized) return;

    const key = e.key.toLowerCase();
    const isMod = e.ctrlKey || e.metaKey;

    // Atajos de colores
    if (key === '1') setColorFromKey('#FFFFFF');
    else if (key === '2') setColorFromKey('#FFD700');
    else if (key === '3') setColorFromKey('#EF4444');
    else if (key === '4') setColorFromKey('#3B82F6');
    else if (key === '5') setColorFromKey('#111111');
    else if (key === '6') setColorFromKey('#00FF99');

    else if (key === 'escape') {
      closePresentationMode();
    } else if (isMod && key === 'z') {
      e.preventDefault();
      laserPointer?.undo();
    } else if (key === 'h') setTool('hand');
    else if (key === 'l') setTool('laser');
    else if (key === 'p') setTool('pen');
    else if (key === 'm') setTool('highlighter');
    else if (key === 'a') setTool('arrow');
    else if (key === 'r') setTool('rect');
    
    // Atajos de Pizarra (ignorando modificadores para evitar conflictos con Ctrl+B)
    else if (!isMod && key === 'b') toggleBoard('black');
    else if (!isMod && key === 'w') toggleBoard('white');
    
    else if (key === 'c' || key === 'delete' || key === 'backspace') {
       // Prioritize deleting selected strokes if any
       const hasSelection = laserPointer && laserPointer['strokes'].some((s:any) => s.isSelected);
       
       if (hasSelection) {
           laserPointer?.deleteSelected();
       } else {
           // Standard clear all if no selection and C pressed, or nothing if Backspace just deletes selection
           // But user asked for "delete that part", so usually C is clear all, Delete is delete selection.
           // Let's make "Clear" (C) be clear all, and "Delete/Backspace" be smart.
           if (key === 'c') {
                laserPointer?.clearAll();
                setTool('hand');
           } else {
                // If Backspace/Delete with NO selection:
                // Option A: Undo last stroke?
                // Option B: Do nothing?
                // Option C: The user previously had 'delete' mapped to clearAll.
                // Let's keep Delete/Backspace = Clear All ONLY if strokes length is small or to avoid confusion?
                // Actually, standard design: Delete deletes selection. If no selection, maybe one step undo or nothing.
                // Reverting to user request "borre esa parte".
                // Let's make Delete ONLY delete selection. 
                // BUT, I need to keep the "Clear All" functionality accessible. The user accepted C/Delete for Clearing.
                // Compromise: 
                // If Selection exists -> Delete Selection.
                // If NO selection -> Clear All (legacy/requested behavior previously).
                laserPointer?.clearAll();
                setTool('hand');
           }
       }
    }
  };

  window.addEventListener('keydown', handleKeyDown);

  // --- Visual Viewport Logic for Sticky Dock ---
  const updateDockPosition = () => {
    const dock = document.getElementById('presentation-dock');
    if (!dock || !window.visualViewport) return;

    const vv = window.visualViewport;
    
    // Scale: If zoom is 200% (scale=2), we want dock to be 50% size to look normal.
    // However, since we use transform logic, we need to be careful.
    const scale = 1 / vv.scale; 
    
    // Center horizontally: Left edge of Visual VP + half its width
    const x = vv.offsetLeft + (vv.width / 2);
    
    // Bottom vertically: Top edge of Visual VP + height - margin (e.g. 60px)
    const y = vv.offsetTop + vv.height - 60; 

    // Apply transform:
    // translate(x, y): Move to target position (relative to layout viewport top-left 0,0)
    // scale(scale): Resize to counter zoom
    // translate(-50%, -100%): Center horizontally (dock center) and anchor to bottom (dock bottom)
    // IMPORTANT: Top/Left are 0 in CSS, so this translate is absolute relative to viewport origin
    dock.style.transform = `translate(${x}px, ${y}px) scale(${scale}) translate(-50%, 0)`;
  };

  // Attach Visual Viewport listeners
  if (window.visualViewport) {
    window.visualViewport.addEventListener('resize', updateDockPosition);
    window.visualViewport.addEventListener('scroll', updateDockPosition);
    // Initial update
    requestAnimationFrame(updateDockPosition);
  } else {
    // Fallback for browsers without Visual Viewport API
    const dock = document.getElementById('presentation-dock');
    if (dock) {
      dock.style.bottom = '2rem';
      dock.style.left = '50%';
      dock.style.transform = 'translateX(-50%)';
    }
  }

  // Guardar referencia para cleanup
  (window as any).__presentationKeyHandler = handleKeyDown;
  (window as any).__presentationDockUpdater = updateDockPosition;
}



function closePresentationMode() {
  if (!isInitialized) return;

  laserPointer?.destroy();
  laserPointer = null;
  isInitialized = false;

  // Clean up Viewport listeners
  if (window.visualViewport && (window as any).__presentationDockUpdater) {
    window.visualViewport.removeEventListener('resize', (window as any).__presentationDockUpdater);
    window.visualViewport.removeEventListener('scroll', (window as any).__presentationDockUpdater);
  }

  // Desactivar modo pantalla completa
  document.body.classList.remove('presentation-mode-active'); // Cleanup legacy just in case

  // Remover elementos del DOM
  document.getElementById('presentation-canvas')?.remove();
  document.getElementById('presentation-board')?.remove();
  document.getElementById('presentation-dock')?.remove();
  document.getElementById('presentation-mode-styles')?.remove();
  document.body.style.overflow = ''; // Ensure scroll is unlocked

  /* 
  if ((window as any).__presentationKeyHandler) {
      window.removeEventListener('keydown', (window as any).__presentationKeyHandler);
      // delete (window as any).__presentationKeyHandler; 
  }
  */
  // NOTA: Mantenemos el listener de teclado global para poder volver a abrirlo con Ctrl+Shift+P
  // Solamente el UI del dock consume eventos cuando está abierto.

  // Salir de Fullscreen si estamos en él (Solo si el usuario lo activó manualmente, pero por seguridad podemos dejarlo o quitarlo, mejor quitarlo para no interferir con preferencias de usuario)
  // if (document.fullscreenElement) {
  //   document.exitFullscreen().catch(err => console.error(err));
  // }

  // Quitar clase de foco
  // const container = document.querySelector('.lesson-container');
  // if (container) {
  //   container.classList.remove('mode-focus');
  // }
  
  // Mostrar botón de activación de nuevo
  const triggerBtn = document.getElementById('presentation-trigger') as HTMLElement | null;
  if (triggerBtn) {
    triggerBtn.style.display = '';
    triggerBtn.classList.remove('loading');
  }
}

/**
 * Inicializa el modo presentación.
 * Esta es la función principal que se exporta y se llama desde el botón activador.
 */
export function initPresentationMode() {
  if (isInitialized) return;

  // Ocultar botón de activación
  const triggerBtn = document.getElementById('presentation-trigger');
  if (triggerBtn) triggerBtn.style.display = 'none';

  // Inyectar estilos
  document.head.insertAdjacentHTML('beforeend', createStyles());

  // Inyectar HTML del dock y canvas
  document.body.insertAdjacentHTML('beforeend', createDockHTML());

  // Inicializar sistema de dibujo
  const canvas = document.getElementById('presentation-canvas') as HTMLCanvasElement;
  laserPointer = new LaserPointer(canvas);
  laserPointer.startSystem();

  // Configurar eventos
  setupEventListeners();

  isInitialized = true;

  // Empezar en modo puntero (hand) implícito
  // El control de pointer-events se maneja dentro de setTool('hand')
  setTool('hand');
}

// Exponer función de cierre para uso externo si es necesario
export { closePresentationMode };
