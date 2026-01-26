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

        if (stroke.points.length < 2) return;
        
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
             if (stroke.isSelected) this.renderRect(stroke.points[0], stroke.points[1], 'rgba(59, 130, 246, 0.5)', 12 * s);
            this.renderRect(stroke.points[0], stroke.points[1], colorStr, 4 * s);
          } else if (stroke.type === 'highlighter') {
            this.renderStroke(stroke.points, colorStr, 24 * s, 0, 'source-over');
          } else {
            this.renderStroke(stroke.points, colorStr, 4 * s, 0, 'source-over');
          }
        } else {
          // Laser Effect
          this.renderStroke(stroke.points, `rgba(255, 0, 0, ${alpha * 0.3})`, 25 * s, 30 * s, 'lighter');
          this.renderStroke(stroke.points, `rgba(255, 0, 0, ${alpha * 0.8})`, 8 * s, 10 * s, 'lighter');
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
    const headlen = Math.max(width * 3.5, 25);
    const angle = Math.atan2(to.y - from.y, to.x - from.x);

    this.ctx.globalCompositeOperation = 'source-over';
    this.ctx.shadowBlur = width;
    this.ctx.shadowColor = color;

    // Shaft
    this.ctx.beginPath();
    this.ctx.strokeStyle = color;
    this.ctx.lineWidth = width;
    this.ctx.lineCap = 'round';
    this.ctx.moveTo(from.x, from.y);
    this.ctx.lineTo(to.x, to.y);
    this.ctx.stroke();

    // Head (Filled)
    this.ctx.beginPath();
    this.ctx.fillStyle = color;
    this.ctx.moveTo(to.x, to.y);
    this.ctx.lineTo(to.x - headlen * Math.cos(angle - Math.PI / 6), to.y - headlen * Math.sin(angle - Math.PI / 6));
    this.ctx.lineTo(to.x - headlen * Math.cos(angle + Math.PI / 6), to.y - headlen * Math.sin(angle + Math.PI / 6));
    this.ctx.closePath();
    this.ctx.fill();

    this.ctx.shadowBlur = 0;
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
