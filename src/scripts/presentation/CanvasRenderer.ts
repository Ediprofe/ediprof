import type { LaserPoint, LaserStroke } from './types';
import { TIMING, UI_COLORS, SIZES } from './config';

export class CanvasRenderer {
  private canvas: HTMLCanvasElement;
  private ctx: CanvasRenderingContext2D;
  private rafId: number | null = null;
  private isSystemRunning = false;

  // Dependencies overridden by controller
  private getStrokes: () => LaserStroke[];
  private getSelectionBox: () => { x: number; y: number; w: number; h: number } | null;
  private isSelecting: () => boolean;

  private lastGlobalActivityTime = 0;

  constructor(
    canvas: HTMLCanvasElement, 
    strokeProvider: () => LaserStroke[],
    selectionBoxProvider: () => { x: number, y: number, w: number, h: number } | null,
    isSelectingProvider: () => boolean
  ) {
    this.canvas = canvas;
    this.ctx = this.canvas.getContext('2d', { alpha: true })!;
    this.getStrokes = strokeProvider;
    this.getSelectionBox = selectionBoxProvider;
    this.isSelecting = isSelectingProvider;
  }

  public setLastActivityTime(time: number) {
    this.lastGlobalActivityTime = time;
  }

  public resize() {
    const dpr = window.devicePixelRatio || 1;
    // PERFORMANCE FIX: Use Viewport size (fixed)
    const width = window.innerWidth;
    const height = window.innerHeight;

    if (this.canvas.width !== width * dpr || this.canvas.height !== height * dpr) {
        this.canvas.width = width * dpr;
        this.canvas.height = height * dpr;
        this.canvas.style.width = width + 'px';
        this.canvas.style.height = height + 'px';
        
        this.draw(); 
    }
  }

  public clearCanvas() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
  }

  public startLoop() {
    if (this.isSystemRunning) return;
    this.isSystemRunning = true;
    
    const loop = () => {
      if (!this.isSystemRunning) return;
      this.draw();
      this.rafId = requestAnimationFrame(loop);
    };
    this.rafId = requestAnimationFrame(loop);
  }

  public stopLoop() {
    this.isSystemRunning = false;
    if (this.rafId) cancelAnimationFrame(this.rafId);
    this.rafId = null;
    this.clearCanvas();
  }

  public draw() {
    // 1. Reset Transform
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // 2. Apply Scroll Transform
    const dpr = window.devicePixelRatio || 1;
    const scrollX = window.scrollX;
    const scrollY = window.scrollY;
    
    // Matrix: [scaleX, skewY, skewX, scaleY, translateX, translateY]
    this.ctx.setTransform(dpr, 0, 0, dpr, -scrollX * dpr, -scrollY * dpr);

    const scale = window.visualViewport?.scale || 1;
    const s = 1 / scale; 

    const strokes = this.getStrokes();
    const now = Date.now();
    
    // Calculate global alpha for laser fading
    // Note: This logic assumes if ANY tool is active (currentStroke != null), we don't fade.
    // However, the renderer doesn't know about currentStroke state easily unless passed.
    // For now, we trust the timestamp provided by controller updates.
    // A simpler approach: Fade based on "now - lastGlobalActivityTime" passed in.
    const idleTime = now - this.lastGlobalActivityTime;
    const globalAlpha = Math.max(0, 1 - idleTime / TIMING.laserFadeDuration);

    if (strokes.length > 0) {
      strokes.forEach((stroke) => {
        // Selection highlight
        if (stroke.isSelected) {
            const selColor = 'rgba(59, 130, 246, 0.5)';
            if(stroke.type !== 'rect' && stroke.type !== 'arrow') {
                this.renderStroke(stroke.points, selColor, (stroke.type === 'highlighter' ? 30 : 10) * s, 0, 'source-over');
            }
        }

        // Text only requires 1 point
        if (stroke.type !== 'text' && stroke.points.length < 2) return;
        
        // Permanent strokes don't fade, Laser fades
        const alpha = stroke.isPermanent ? (stroke.type === 'highlighter' ? 0.4 : 1.0) : globalAlpha;
        if (alpha <= 0) return;

        if (stroke.isPermanent) {
          const rgb = this.hexToRgb(stroke.color);
          const colorStr = `rgba(${rgb}, ${alpha})`;

          if (stroke.type === 'arrow') {
             if (stroke.isSelected) this.renderArrow(stroke.points[0], stroke.points[1], 'rgba(59, 130, 246, 0.5)', 20 * s);
            this.renderArrow(stroke.points[0], stroke.points[1], colorStr, 8 * s);
          } else if (stroke.type === 'rect') {
             if (stroke.isSelected) this.renderRect(stroke.points[0], stroke.points[1], 'rgba(59, 130, 246, 0.5)', 20 * s);
            this.renderRect(stroke.points[0], stroke.points[1], colorStr, 8 * s);
          } else if (stroke.type === 'highlighter') {
            this.renderStroke(stroke.points, colorStr, 24 * s, 0, 'source-over');
          } else if (stroke.type === 'text' && stroke.text) {
             if (stroke.isSelected) this.renderText(stroke.points[0], stroke.text, 'rgba(59, 130, 246, 0.5)', 32 * s);
             this.renderText(stroke.points[0], stroke.text, colorStr, 32 * s);
          } else {
            this.renderStroke(stroke.points, colorStr, 4 * s, 0, 'source-over');
          }
        } else {
          // Laser Effect
          const rgb = this.hexToRgb(stroke.color);
          this.renderStroke(stroke.points, `rgba(${rgb}, ${alpha * 0.3})`, 25 * s, 30 * s, 'lighter');
          this.renderStroke(stroke.points, `rgba(${rgb}, ${alpha * 0.8})`, 8 * s, 10 * s, 'lighter');
          this.renderStroke(stroke.points, `rgba(255, 255, 255, ${alpha * 0.95})`, 3 * s, 0, 'source-over');
        }
      });
    }

    // Draw active Selection Box
    const selectionBox = this.getSelectionBox();
    const isSelecting = this.isSelecting();
    
    if (isSelecting && selectionBox) {
        this.ctx.globalCompositeOperation = 'source-over';
        this.ctx.strokeStyle = '#3b82f6';
        this.ctx.lineWidth = 2 * s; 
        
        this.ctx.strokeRect(selectionBox.x, selectionBox.y, selectionBox.w, selectionBox.h);
        
        this.ctx.fillStyle = 'rgba(59, 130, 246, 0.2)';
        this.ctx.fillRect(selectionBox.x, selectionBox.y, selectionBox.w, selectionBox.h);
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
    const headlen = Math.max(width * 2.5, 20);
    const angle = Math.atan2(to.y - from.y, to.x - from.x);

    // Función auxiliar para dibujar la geometría de la flecha
    // Separamos shaft (línea) y head (triángulo) para controlar mejor el estilo
    const drawGeometry = (lineWidth: number, isFill = false) => {
        this.ctx.lineWidth = lineWidth;
        
        // Shaft
        this.ctx.beginPath();
        this.ctx.moveTo(from.x, from.y);
        this.ctx.lineTo(to.x, to.y);
        this.ctx.stroke();

        // Head
        this.ctx.beginPath();
        this.ctx.moveTo(to.x, to.y);
        this.ctx.lineTo(to.x - headlen * Math.cos(angle - Math.PI / 6), to.y - headlen * Math.sin(angle - Math.PI / 6));
        this.ctx.lineTo(to.x - headlen * Math.cos(angle + Math.PI / 6), to.y - headlen * Math.sin(angle + Math.PI / 6));
        this.ctx.closePath();
        if (isFill) {
            this.ctx.fill();
        } else {
            this.ctx.stroke();
        }
    };

    this.ctx.globalCompositeOperation = 'source-over';
    this.ctx.lineCap = 'round';
    this.ctx.lineJoin = 'round';

    // 1. CAPA DE RESPLANDOR (Glow)
    // Crea el efecto de luz difusa alrededor
    this.ctx.shadowBlur = 15;
    this.ctx.shadowColor = color;
    this.ctx.strokeStyle = color;
    this.ctx.fillStyle = color;
    // Dibujamos un poco más grueso para el halo
    drawGeometry(width + 4, true);

    // 2. CAPA DE NÚCLEO (Color Sólido)
    // Define la forma nítida
    this.ctx.shadowBlur = 0; // Reset shadow
    this.ctx.strokeStyle = color;
    this.ctx.fillStyle = color;
    drawGeometry(width, true);

    // 3. CAPA DE BRILLO (Highlight)
    // Línea central blanca semitransparente para dar efecto de "tubo de neón" o energía
    this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
    this.ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
    drawGeometry(width * 0.3, true);
  }

  private renderRect(from: LaserPoint, to: LaserPoint, color: string, width: number) {
    const x = Math.min(from.x, to.x);
    const y = Math.min(from.y, to.y);
    const w = Math.abs(to.x - from.x);
    const h = Math.abs(to.y - from.y);

    this.ctx.globalCompositeOperation = 'source-over';
    this.ctx.lineCap = 'round';
    this.ctx.lineJoin = 'round';

    // 1. CAPA DE RESPLANDOR (Glow)
    this.ctx.shadowBlur = 15;
    this.ctx.shadowColor = color;
    this.ctx.strokeStyle = color;
    this.ctx.lineWidth = width + 4;
    this.ctx.strokeRect(x, y, w, h);

    // 2. CAPA DE NÚCLEO (Color Sólido)
    this.ctx.shadowBlur = 0;
    this.ctx.strokeStyle = color;
    this.ctx.lineWidth = width;
    this.ctx.strokeRect(x, y, w, h);

    // 3. CAPA DE BRILLO (Highlight)
    this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
    this.ctx.lineWidth = width * 0.3;
    this.ctx.strokeRect(x, y, w, h);
  }

  private renderText(pos: LaserPoint, text: string, color: string, size: number) {
      this.ctx.globalCompositeOperation = 'source-over';
      this.ctx.font = `bold ${size}px "Space Grotesk", sans-serif`;
      this.ctx.textAlign = 'left';
      this.ctx.textBaseline = 'top'; 
      
      const lines = text.split('\n');
      const lineHeight = size * 1.2;
      const startY = pos.y - 20;
      
      // ROUND coordinates to avoid sub-pixel blurring
      const x = Math.round(pos.x);

      lines.forEach((line, index) => {
          const y = Math.round(startY + (index * lineHeight));
          
          // PASS 1: PURE GLOW (The "CSS text-shadow" effect)
          // We draw the text far off-screen (-10000px) but cast the shadow back to the correct position.
          // This isolates the shadow so we don't muddy the text pixels or get double-draw artifacts.
          this.ctx.save();
          this.ctx.shadowBlur = 15; // Match CSS value exactly
          this.ctx.shadowColor = color;
          this.ctx.shadowOffsetX = 10000; // Offset shadow by +10000
          this.ctx.shadowOffsetY = 0;
          this.ctx.fillStyle = color;
          
          // Draw text at x - 10000. Shadow appears at x.
          this.ctx.fillText(line, x - 10000, y);
          this.ctx.restore();

          // PASS 2: SOLID TEXT (The "CSS color" effect)
          // Draw clean, sharp text on top of the glow
          this.ctx.shadowBlur = 0;
          this.ctx.shadowOffsetX = 0;
          this.ctx.shadowOffsetY = 0;
          this.ctx.fillStyle = color;
          this.ctx.fillText(line, x, y);
      });
  }
}
