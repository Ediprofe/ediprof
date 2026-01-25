/**
 * Modo Presentación para Ediprofe
 *
 * Este módulo proporciona herramientas de anotación en pantalla:
 * - Puntero láser (efecto temporal)
 * - Lápiz (dibujo permanente)
 * - Flechas y rectángulos
 * - Selector de colores
 *
 * Se carga dinámicamente solo cuando el usuario activa el modo presentación.
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
  type?: 'line' | 'arrow' | 'rect';
}

class LaserPointer {
  private canvas: HTMLCanvasElement;
  public ctx: CanvasRenderingContext2D;
  private strokes: LaserStroke[] = [];
  private currentStroke: LaserStroke | null = null;
  public isInputActive = false;
  private systemRunning = false;
  private toolMode: 'laser' | 'pen' | 'arrow' | 'rect' = 'laser';
  private currentColor: string = '#EF4444'; // Rojo por defecto
  private rafId: number | null = null;
  private lastGlobalActivityTime: number = Date.now();
  private duration = 3000;
  private isBlockedByGesture = false;

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
    this.resize();

    this.canvas.addEventListener('mousedown', this.boundStart, { passive: false });
    window.addEventListener('mousemove', this.boundMove, { passive: false });
    window.addEventListener('mouseup', this.boundStop);
    
    this.canvas.addEventListener('touchstart', this.boundStart, { passive: false });
    window.addEventListener('touchmove', this.boundMove, { passive: false });
    window.addEventListener('touchend', this.boundStop);
  }

  public destroy() {
    this.stopSystem();
    window.removeEventListener('resize', this.boundResize);
    this.canvas.removeEventListener('mousedown', this.boundStart);
    window.removeEventListener('mousemove', this.boundMove);
    window.removeEventListener('mouseup', this.boundStop);
    this.canvas.removeEventListener('touchstart', this.boundStart);
    window.removeEventListener('touchmove', this.boundMove);
    window.removeEventListener('touchend', this.boundStop);
  }

  private getPos(e: MouseEvent | TouchEvent) {
    const rect = this.canvas.getBoundingClientRect();
    const scaleX = this.canvas.width / rect.width;
    const scaleY = this.canvas.height / rect.height;
    const clientX = 'clientX' in e ? e.clientX : e.touches[0].clientX;
    const clientY = 'clientY' in e ? e.clientY : e.touches[0].clientY;
    return {
      x: (clientX - rect.left) * scaleX,
      y: (clientY - rect.top) * scaleY,
    };
  }



  private handleStart(e: MouseEvent | TouchEvent) {
    if (!this.isInputActive || this.isBlockedByGesture) return;
    if ('touches' in e && e.touches.length > 1) {
      this.isBlockedByGesture = true;
      this.handleStop();
      return;
    }

    if ('touches' in e) e.preventDefault();
    const { x, y } = this.getPos(e);
    this.lastGlobalActivityTime = Date.now();
    this.currentStroke = {
      points: [{ x, y }],
      isDead: false,
      isPermanent: this.toolMode === 'pen' || this.toolMode === 'arrow' || this.toolMode === 'rect',
      color: this.toolMode === 'laser' ? '#EF4444' : this.currentColor,
      type: this.toolMode === 'arrow' ? 'arrow' : this.toolMode === 'rect' ? 'rect' : 'line',
    };
    this.strokes.push(this.currentStroke);
  }

  private handleMove(e: MouseEvent | TouchEvent) {
    if (!this.isInputActive || !this.currentStroke || this.isBlockedByGesture) return;
    if ('touches' in e && e.touches.length > 1) {
      this.handleStop();
      return;
    }

    const { x, y } = this.getPos(e);
    this.lastGlobalActivityTime = Date.now();

    if (this.currentStroke.type === 'arrow' || this.currentStroke.type === 'rect') {
      this.currentStroke.points = [this.currentStroke.points[0], { x, y }];
    } else {
      this.currentStroke.points.push({ x, y });
      if (this.currentStroke.points.length > 800) this.currentStroke.points.shift();
    }
  }

  private handleStop() {
    this.currentStroke = null;
    this.lastGlobalActivityTime = Date.now();
  }

  public setGestureBlock(state: boolean) {
    this.isBlockedByGesture = state;
    if (state) this.currentStroke = null;
  }

  public resize() {
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
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
  }

  public setMode(mode: 'laser' | 'pen' | 'arrow' | 'rect') {
    this.toolMode = mode;
  }

  public setColor(color: string) {
    this.currentColor = color;
  }

  public undo() {
    this.strokes.pop();
    this.lastGlobalActivityTime = Date.now();
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
    if (this.strokes.length === 0) return;

    const now = Date.now();
    const idleTime = this.currentStroke ? 0 : now - this.lastGlobalActivityTime;
    const globalAlpha = Math.max(0, 1 - idleTime / this.duration);

    this.strokes.forEach((stroke) => {
      if (stroke.points.length < 2) return;
      const alpha = stroke.isPermanent ? 1.0 : globalAlpha;
      if (alpha <= 0) return;

      if (stroke.isPermanent) {
        const rgb = this.hexToRgb(stroke.color);
        const colorStr = `rgba(${rgb}, ${alpha})`;

        if (stroke.type === 'arrow') {
          this.renderArrow(stroke.points[0], stroke.points[1], colorStr, 4);
        } else if (stroke.type === 'rect') {
          this.renderRect(stroke.points[0], stroke.points[1], colorStr, 4);
        } else {
          this.renderStroke(stroke.points, colorStr, 4, 3, 'source-over');
          this.renderStroke(stroke.points, `rgba(255, 255, 255, ${alpha * 0.4})`, 1.5, 0, 'source-over');
        }
      } else {
        this.renderStroke(stroke.points, `rgba(255, 0, 0, ${alpha * 0.3})`, 25, 30, 'lighter');
        this.renderStroke(stroke.points, `rgba(255, 0, 0, ${alpha * 0.8})`, 8, 10, 'lighter');
        this.renderStroke(stroke.points, `rgba(255, 255, 255, ${alpha * 0.95})`, 3, 0, 'source-over');
      }
    });
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
let currentTool: 'hand' | 'laser' | 'pen' | 'arrow' | 'rect' = 'hand';

function createDockHTML(): string {
  return `
    <canvas id="presentation-canvas" class="presentation-canvas"></canvas>
    <div class="presentation-dock-wrapper" id="presentation-dock">
      <div class="presentation-glass-dock">
        <div class="dock-section tools">
          <button id="pm-hand-btn" class="dock-btn tool-trigger active" title="Puntero (H)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m3 3 7.07 16.97 2.51-7.39 7.39-2.51L3 3z"></path><path d="m13 13 6 6"></path></svg>
            <span>Puntero</span>
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
        </div>
        <div class="dock-divider"></div>
        <div id="pm-colors" class="dock-section colors">
          <button class="color-dot" data-color="#FFFFFF" title="Blanco (1)" style="background: #FFFFFF;"></button>
          <button class="color-dot" data-color="#FEF015" title="Amarillo (2)" style="background: #FEF015;"></button>
          <button class="color-dot active" data-color="#EF4444" title="Rojo (3)" style="background: #EF4444;"></button>
          <button class="color-dot" data-color="#3B82F6" title="Azul (4)" style="background: #3B82F6;"></button>
          <button class="color-dot" data-color="#111111" title="Negro (5)" style="background: #111111; border: 1px solid rgba(255,255,255,0.2)"></button>
        </div>
        <div class="dock-divider"></div>
        <div class="dock-section actions">
          <button id="pm-undo-btn" class="dock-btn" title="Deshacer (Ctrl+Z)">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7v6h6"></path><path d="M21 17a9 9 0 0 0-9-9 9 9 0 0 0-6 2.3L3 13"></path></svg>
          </button>
          <button id="pm-clear-btn" class="dock-btn" title="Limpiar (C)">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"></path><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"></path><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg>
          </button>
          <button id="pm-close-btn" class="dock-btn dock-btn-close" title="Cerrar (Esc)">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
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
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 999999998;
        pointer-events: none;
        will-change: transform;
      }
      .presentation-canvas.active {
        pointer-events: auto;
        cursor: crosshair;
      }
      .presentation-dock-wrapper {
        position: fixed;
        bottom: 2rem;
        left: 50%;
        transform: translateX(-50%);
        width: auto;
        display: flex;
        justify-content: center;
        z-index: 999999999;
        animation: slideUp 0.3s ease-out;
      }
      @keyframes slideUp {
        from { transform: translateX(-50%) translateY(100px); opacity: 0; }
        to { transform: translateX(-50%) translateY(0); opacity: 1; }
      }
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
        .dock-btn { padding: 0 8px; }
        .presentation-glass-dock { padding: 8px 12px; gap: 6px; }
      }

      /* Animación suave al activar/desactivar */
      .lesson-content,
      .content-article {
        transition: all 0.3s ease-out;
      }
    </style>
  `;
}

function setTool(tool: 'hand' | 'laser' | 'pen' | 'arrow' | 'rect') {
  if (!laserPointer) return;

  currentTool = tool;
  laserPointer.setDrawingEnabled(tool !== 'hand');
  if (tool !== 'hand') {
    laserPointer.setMode(tool as 'laser' | 'pen' | 'arrow' | 'rect');
  }

  const canvas = document.getElementById('presentation-canvas');
  canvas?.classList.toggle('active', tool !== 'hand');

  // Actualizar estados de botones
  document.getElementById('pm-hand-btn')?.classList.toggle('active', tool === 'hand');
  document.getElementById('pm-laser-btn')?.classList.toggle('active', tool === 'laser');
  document.getElementById('pm-pen-btn')?.classList.toggle('active', tool === 'pen');
  document.getElementById('pm-arrow-btn')?.classList.toggle('active', tool === 'arrow');
  document.getElementById('pm-rect-btn')?.classList.toggle('active', tool === 'rect');
}

function setupEventListeners() {
  document.getElementById('pm-hand-btn')?.addEventListener('click', () => setTool('hand'));
  document.getElementById('pm-laser-btn')?.addEventListener('click', () => setTool('laser'));
  document.getElementById('pm-pen-btn')?.addEventListener('click', () => setTool('pen'));
  document.getElementById('pm-arrow-btn')?.addEventListener('click', () => setTool('arrow'));
  document.getElementById('pm-rect-btn')?.addEventListener('click', () => setTool('rect'));
  document.getElementById('pm-clear-btn')?.addEventListener('click', () => laserPointer?.clearAll());
  document.getElementById('pm-undo-btn')?.addEventListener('click', () => laserPointer?.undo());
  document.getElementById('pm-close-btn')?.addEventListener('click', () => closePresentationMode());

  // Colores
  document.querySelectorAll('#pm-colors .color-dot').forEach((dot) => {
    dot.addEventListener('click', () => {
      const color = dot.getAttribute('data-color') || '#FFFFFF';
      laserPointer?.setColor(color);
      document.querySelectorAll('#pm-colors .color-dot').forEach((d) => d.classList.remove('active'));
      dot.classList.add('active');
      setTool('pen');
    });
  });

  // Helper para cambiar color desde teclado
  const setColorFromKey = (color: string) => {
    laserPointer?.setColor(color);
    document.querySelectorAll('#pm-colors .color-dot').forEach((d) => {
      if (d.getAttribute('data-color') === color) d.classList.add('active');
      else d.classList.remove('active');
    });
    setTool('pen');
  };

  // Atajos de teclado
  const handleKeyDown = (e: KeyboardEvent) => {
    if (!isInitialized) return;

    const key = e.key.toLowerCase();
    const isMod = e.ctrlKey || e.metaKey;

    // Atajos de colores
    if (key === '1') setColorFromKey('#FFFFFF');
    else if (key === '2') setColorFromKey('#FEF015');
    else if (key === '3') setColorFromKey('#EF4444');
    else if (key === '4') setColorFromKey('#3B82F6');
    else if (key === '5') setColorFromKey('#111111');

    else if (key === 'escape') {
      closePresentationMode();
    } else if (isMod && key === 'z') {
      e.preventDefault();
      laserPointer?.undo();
    } else if (key === 'h') setTool('hand');
    else if (key === 'l') setTool('laser');
    else if (key === 'p') setTool('pen');
    else if (key === 'a') setTool('arrow');
    else if (key === 'r') setTool('rect');
    else if (key === 'c') laserPointer?.clearAll();
  };

  window.addEventListener('keydown', handleKeyDown);

  // Guardar referencia para cleanup
  (window as any).__presentationKeyHandler = handleKeyDown;
}



function closePresentationMode() {
  if (!isInitialized) return;

  laserPointer?.destroy();
  laserPointer = null;
  isInitialized = false;

  // Desactivar modo pantalla completa
  document.body.classList.remove('presentation-mode-active'); // Cleanup legacy just in case

  // Remover elementos del DOM
  document.getElementById('presentation-canvas')?.remove();
  document.getElementById('presentation-dock')?.remove();
  document.getElementById('presentation-mode-styles')?.remove();

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
