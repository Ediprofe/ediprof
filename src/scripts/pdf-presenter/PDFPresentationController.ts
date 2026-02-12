/**
 * PDFPresentationController - Adaptación del PresentationController para PDF.js
 * 
 * Diferencias clave con el PresentationController original:
 * - El canvas está posicionado dentro del contenedor scrollable del PDF
 * - Las coordenadas son relativas al contenido scrollable, no al viewport
 * - El canvas se posiciona como position:sticky para seguir el viewport
 *   pero las coordenadas de dibujo usan el scroll del contenedor
 * - Wheel events se reenvían al contenedor para permitir scroll con herramientas activas
 */

import { StrokeManager } from '../presentation/StrokeManager';
import { WindowManager } from '../presentation/WindowManager';
import { TextHighlighter } from '../presentation/TextHighlighter';
import { TOOL_COLORS, UI_COLORS, TIMING } from '../presentation/config';
import type { LaserPoint, ToolMode, LaserStroke } from '../presentation/types';
import { PDFInputHandler } from './PDFInputHandler';

export class PDFPresentationController {
  private strokeManager: StrokeManager;
  private renderer: PDFCanvasRenderer;
  private inputHandler: PDFInputHandler;
  private windowManager: WindowManager;
  private textHighlighter: TextHighlighter;

  private currentTool: ToolMode = 'hand';
  private currentColor: string = TOOL_COLORS.red;
  private systemRunning = false;
  private currentStroke: LaserStroke | null = null;
  private clipboard: LaserStroke[] = [];
  private isDragging = false;
  private lastDragPoint: LaserPoint | null = null;
  
  private resizeObserver: ResizeObserver | null = null;
  private onExitCallback: (() => void) | undefined;
  private canvas: HTMLCanvasElement;
  private pdfContainer: HTMLElement;

  constructor(pdfContainer: HTMLElement, onExit?: () => void) {
    this.pdfContainer = pdfContainer;
    this.onExitCallback = onExit;

    // 1. Setup Canvas - fixed overlay on top of the PDF container
    // We append to document.body with position:fixed so the canvas
    // always covers the visible area of the PDF container,
    // regardless of scroll position or DOM order.
    this.canvas = document.createElement('canvas');
    this.canvas.id = 'pdf-presentation-canvas';
    this.canvas.className = 'pdf-presentation-canvas';
    document.body.appendChild(this.canvas);

    // 2. Initialize Components
    this.strokeManager = new StrokeManager(() => this.requestRender());
    
    this.renderer = new PDFCanvasRenderer(
      this.canvas,
      this.pdfContainer,
      () => this.strokeManager.getStrokes(),
      () => this.strokeManager.selectionBox,
      () => this.strokeManager.isSelecting
    );
    
    this.inputHandler = new PDFInputHandler(
      this.canvas,
      this.pdfContainer,
      (p: LaserPoint, mt: boolean, sh: boolean) => this.handleStart(p, mt, sh),
      (p: LaserPoint, mt: boolean, sh: boolean) => this.handleMove(p, mt, sh),
      () => this.handleStop()
    );
    
    // 3. UI Manager
    this.windowManager = new WindowManager({
      onToolChange: (t) => this.setTool(t as ToolMode),
      onColorChange: (c) => this.setColor(c),
      onUndo: () => this.handleUndo(),
      onClear: () => this.handleClear(),
      onDeleteSelected: () => this.strokeManager.deleteSelected(),
      onBoardChange: (t) => this.windowManager.setBoardState(t),
      onClose: () => this.stop(),
      onCopy: () => this.handleCopy(),
      onPaste: () => this.handlePaste()
    });
    
    // 4. Text Highlighter (disabled for PDF - no editable DOM)
    this.textHighlighter = new TextHighlighter();
    
    this.start();
  }
  
  private start() {
    if (this.systemRunning) return;
    this.systemRunning = true;
    
    this.windowManager.init();
    this.renderer.start();
    
    // Resize Observer for the PDF container - with debounce
    let resizeTimeout: ReturnType<typeof setTimeout>;
    this.resizeObserver = new ResizeObserver(() => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(() => this.renderer.resize(), 100);
    });
    this.resizeObserver.observe(this.pdfContainer);
    
    // Listen to the PDF container's scroll, not window scroll
    this.pdfContainer.addEventListener('scroll', this.boundScroll, { passive: true });
    
    this.renderer.resize();
  }
  
  public stop() {
    this.systemRunning = false;
    this.strokeManager.clearAll();
    this.renderer.stop();
    this.windowManager.destroy();
    this.inputHandler.destroy();
    
    this.resizeObserver?.disconnect();
    this.pdfContainer.removeEventListener('scroll', this.boundScroll);
    
    this.canvas.remove();
    
    this.onExitCallback?.();
  }
  
  private boundScroll = () => {
    this.renderer.requestRender();
  };
  
  private requestRender() {
    this.renderer.requestRender();
  }
  
  private setTool(tool: ToolMode) {
    this.currentTool = tool;
    this.inputHandler.setInputActive(tool !== 'hand');
    this.windowManager.setToolActive(tool);
    
    const canvas = document.getElementById('pdf-presentation-canvas');
    if (canvas) canvas.classList.toggle('active', tool !== 'hand');
    
    if (tool === 'laser' || tool === 'guide') {
      this.clearDeadLaserStrokes();
    }
  }
  
  private setColor(color: string) {
    this.currentColor = color;
    this.windowManager.setActiveColor(color);
    
    if (this.currentTool === 'hand' || this.currentTool === 'laser' || this.currentTool === 'guide' || this.currentTool === 'select') {
      this.setTool('pen');
    }
  }
  
  private handleUndo() {
    this.strokeManager.undo();
  }
  
  private handleClear() {
    this.strokeManager.clearAll();
  }
  
  private handleStart(p: LaserPoint, isMultiTouch: boolean, isShift: boolean) {
    if (this.currentTool === 'text') {
      const input = document.createElement('textarea');
      
      // Position relative to the container's viewport
      const containerRect = this.pdfContainer.getBoundingClientRect();
      const viewportX = p.x - this.pdfContainer.scrollLeft;
      const viewportY = p.y - this.pdfContainer.scrollTop;
      
      input.style.position = 'fixed';
      input.style.left = `${containerRect.left + viewportX}px`;
      input.style.top = `${containerRect.top + viewportY - 20}px`;
      input.style.background = 'transparent';
      input.style.border = '1px dashed rgba(255,255,255,0.3)';
      input.style.outline = 'none';
      input.style.color = this.currentColor;
      input.style.font = 'bold 32px "Space Grotesk", sans-serif';
      input.style.lineHeight = '1.2';
      input.style.textShadow = `0 0 15px ${this.currentColor}`;
      input.style.zIndex = '2147483647';
      input.style.padding = '0';
      input.style.margin = '0';
      input.style.overflow = 'hidden';
      input.style.resize = 'none';
      input.style.whiteSpace = 'pre';
      input.style.minWidth = '50px';
      input.style.width = '20px';
      input.style.height = '40px';
      
      document.body.appendChild(input);
      
      const resizeInput = () => {
        input.style.width = '0px';
        input.style.height = '0px';
        const newW = input.scrollWidth + 20;
        const newH = input.scrollHeight;
        const maxWidth = window.innerWidth - (containerRect.left + viewportX) - 20;
        input.style.width = Math.min(newW, Math.max(maxWidth, 100)) + 'px';
        input.style.height = newH + 'px';
      };

      const commitText = () => {
        const text = input.value;
        if (text && text.trim().length > 0) {
          const stroke: LaserStroke = {
            points: [{ x: p.x, y: p.y }],
            isDead: false,
            isPermanent: true,
            color: this.currentColor,
            type: 'text',
            text: text,
            isSelected: false
          };
          this.strokeManager.addStroke(stroke);
          this.renderer.setLastActivityTime(Date.now());
        }
        input.remove();
      };

      input.addEventListener('input', resizeInput);
      
      input.addEventListener('keydown', (e) => {
        e.stopPropagation();
        if (e.key === 'Enter' && !e.shiftKey) {
          e.preventDefault();
          commitText();
        } else if (e.key === 'Escape') {
          input.remove();
        }
        requestAnimationFrame(resizeInput);
      });

      input.addEventListener('blur', commitText);
      
      requestAnimationFrame(() => {
        input.focus();
        resizeInput();
      });
      
      return;
    }

    if (this.currentTool === 'select') {
      const selected = this.strokeManager.getSelectedStrokes();
      if (selected.length > 0) {
        const hit = selected.some(s => {
          const sMinX = s.minX ?? -Infinity;
          const sMaxX = s.maxX ?? Infinity;
          const sMinY = s.minY ?? -Infinity;
          const sMaxY = s.maxY ?? Infinity;
          const margin = 10;
          return p.x >= sMinX - margin && p.x <= sMaxX + margin &&
                 p.y >= sMinY - margin && p.y <= sMaxY + margin;
        });

        if (hit) {
          this.isDragging = true;
          this.lastDragPoint = p;
          return;
        }
      }

      this.strokeManager.isSelecting = true;
      this.strokeManager.selectionBox = { x: p.x, y: p.y, w: 0, h: 0 };
      this.strokeManager.deselectAll();
      
      return;
    }
  
    this.currentStroke = {
      points: [p],
      isDead: false,
      isPermanent: this.currentTool !== 'laser' && this.currentTool !== 'guide',
      color: this.currentTool === 'laser'
        ? UI_COLORS.laser
        : (this.currentTool === 'guide' ? UI_COLORS.guide : this.currentColor),
      type: this.currentTool,
      isSelected: false
    };
    
    this.strokeManager.addStroke(this.currentStroke);
    
    if (this.currentTool === 'laser' || this.currentTool === 'guide') {
      this.renderer.setLastActivityTime(Date.now());
    }
  }
  
  private handleMove(p: LaserPoint, isMultiTouch: boolean, isShift: boolean) {
    if (this.currentTool === 'select') {
      if (this.isDragging && this.lastDragPoint) {
        const dx = p.x - this.lastDragPoint.x;
        const dy = p.y - this.lastDragPoint.y;
        
        const selected = this.strokeManager.getSelectedStrokes();
        selected.forEach(s => {
          s.points.forEach(pt => {
            pt.x += dx;
            pt.y += dy;
          });
          if (s.minX !== undefined) s.minX += dx;
          if (s.maxX !== undefined) s.maxX += dx;
          if (s.minY !== undefined) s.minY += dy;
          if (s.maxY !== undefined) s.maxY += dy;
        });
        
        this.lastDragPoint = p;
        return;
      }

      if (this.strokeManager.isSelecting && this.strokeManager.selectionBox) {
        this.strokeManager.selectionBox.w = p.x - this.strokeManager.selectionBox.x;
        this.strokeManager.selectionBox.h = p.y - this.strokeManager.selectionBox.y;
      }
      return;
    }
  
    if (this.currentStroke) {
      const isDrawToolWithShift = (this.currentStroke.type === 'pen' || this.currentStroke.type === 'highlighter') && isShift;

      if (this.currentStroke.type === 'arrow' || this.currentStroke.type === 'rect' || isDrawToolWithShift) {
        let targetP = p;

        if (isShift) {
          const startP = this.currentStroke.points[0];
          const dx = p.x - startP.x;
          const dy = p.y - startP.y;
          const absDx = Math.abs(dx);
          const absDy = Math.abs(dy);

          if (absDy < absDx * 0.5) {
            targetP = { x: p.x, y: startP.y };
          } else if (absDx < absDy * 0.5) {
            targetP = { x: startP.x, y: p.y };
          } else {
            const signX = Math.sign(dx);
            const signY = Math.sign(dy);
            const len = Math.max(absDx, absDy);
            targetP = { x: startP.x + len * signX, y: startP.y + len * signY };
          }
        }

        this.currentStroke.points = [this.currentStroke.points[0], targetP];
      } else if (this.currentTool === 'guide') {
        const startP = this.currentStroke.points[0];
        this.currentStroke.points.push({ x: p.x, y: startP.y });
      } else {
        this.currentStroke.points.push(p);
      }
      
      if (this.currentTool === 'laser' || this.currentTool === 'guide') {
        this.renderer.setLastActivityTime(Date.now());
      }
    }
  }
  
  private handleStop() {
    if (this.isDragging) {
      this.isDragging = false;
      this.lastDragPoint = null;
      return;
    }

    if (this.currentTool === 'select' && this.strokeManager.isSelecting && this.strokeManager.selectionBox) {
      this.strokeManager.computeSelection(this.strokeManager.selectionBox);
      this.strokeManager.isSelecting = false;
      this.strokeManager.selectionBox = null;
      return;
    }
    
    if (this.currentStroke) {
      let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
      this.currentStroke.points.forEach(pt => {
        if (pt.x < minX) minX = pt.x;
        if (pt.x > maxX) maxX = pt.x;
        if (pt.y < minY) minY = pt.y;
        if (pt.y > maxY) maxY = pt.y;
      });
      this.currentStroke.minX = minX;
      this.currentStroke.maxX = maxX;
      this.currentStroke.minY = minY;
      this.currentStroke.maxY = maxY;
      
      if (this.currentTool === 'laser' || this.currentTool === 'guide') {
        this.currentStroke.createdAt = Date.now();
      }
      
      this.currentStroke = null;
      
      if (this.currentTool === 'laser' || this.currentTool === 'guide') {
        this.renderer.setLastActivityTime(Date.now());
      }
    }
  }

  private clearDeadLaserStrokes() {
    const now = Date.now();
    
    const strokes = this.strokeManager.getStrokes();
    const aliveStrokes = strokes.filter(s => {
      if (s.isPermanent) return true;
      if (!s.createdAt) return true;
      
      const age = now - s.createdAt;
      const alpha = Math.max(0, 1 - age / TIMING.laserFadeDuration);
      return alpha > 0.01;
    });
    
    if (aliveStrokes.length !== strokes.length) {
      this.strokeManager.setStrokes(aliveStrokes);
    }
  }

  private handleCopy() {
    const selected = this.strokeManager.getSelectedStrokes();
    if (selected.length > 0) {
      this.clipboard = JSON.parse(JSON.stringify(selected));
    }
  }

  private handlePaste() {
    if (this.clipboard.length === 0) return;

    this.strokeManager.deselectAll();

    const toPaste: LaserStroke[] = JSON.parse(JSON.stringify(this.clipboard));
    const offset = 20;

    toPaste.forEach(stroke => {
      stroke.points.forEach(p => {
        p.x += offset;
        p.y += offset;
      });

      if (stroke.minX !== undefined) stroke.minX += offset;
      if (stroke.maxX !== undefined) stroke.maxX += offset;
      if (stroke.minY !== undefined) stroke.minY += offset;
      if (stroke.maxY !== undefined) stroke.maxY += offset;

      stroke.isSelected = true;
      this.strokeManager.addStroke(stroke);
    });

    this.clipboard = JSON.parse(JSON.stringify(toPaste));
    
    if (this.currentTool !== 'select') {
      this.setTool('select');
    }
  }

  public exportToImage(): string {
    return this.renderer.exportToImage();
  }
}

/**
 * PDFCanvasRenderer - Renderer optimizado para el contenedor del PDF
 * 
 * Estrategia de posicionamiento:
 * - El canvas usa position: sticky + top: 0 dentro del contenedor scrollable
 *   Esto hace que el canvas siempre esté visible en el viewport del contenedor
 * - El canvas tiene el tamaño del viewport del contenedor (clientWidth × clientHeight)
 * - Los strokes se almacenan en coordenadas del documento scrollable
 * - Al renderizar, aplicamos una transformación que convierte coordenadas de documento
 *   a coordenadas del viewport, restando scrollLeft/scrollTop
 * 
 * Esto logra que:
 * 1. Las anotaciones queden "pegadas" al contenido del PDF
 * 2. El canvas no sea innecesariamente grande (solo viewport visible)
 * 3. El rendimiento sea óptimo
 */
class PDFCanvasRenderer {
  private canvas: HTMLCanvasElement;
  private pdfContainer: HTMLElement;
  private ctx: CanvasRenderingContext2D;
  private isSystemRunning = false;
  private rafId: number | null = null;

  private getStrokes: () => LaserStroke[];
  private getSelectionBox: () => { x: number; y: number; w: number; h: number } | null;
  private isSelecting: () => boolean;

  private lastGlobalActivityTime = 0;

  constructor(
    canvas: HTMLCanvasElement,
    pdfContainer: HTMLElement,
    strokeProvider: () => LaserStroke[],
    selectionBoxProvider: () => { x: number, y: number, w: number, h: number } | null,
    isSelectingProvider: () => boolean
  ) {
    this.canvas = canvas;
    this.pdfContainer = pdfContainer;
    this.ctx = this.canvas.getContext('2d', { alpha: true })!;
    this.getStrokes = strokeProvider;
    this.getSelectionBox = selectionBoxProvider;
    this.isSelecting = isSelectingProvider;
  }

  public setLastActivityTime(time: number) {
    this.lastGlobalActivityTime = time;
    this.requestRender();
  }

  public resize() {
    const dpr = window.devicePixelRatio || 1;
    // Canvas covers only the visible viewport of the container
    const width = this.pdfContainer.clientWidth;
    const height = this.pdfContainer.clientHeight;

    this.canvas.width = width * dpr;
    this.canvas.height = height * dpr;
    this.canvas.style.width = width + 'px';
    this.canvas.style.height = height + 'px';
    
    // Position the canvas exactly over the PDF container
    this.updateCanvasPosition();
    
    this.requestRender();
  }

  /**
   * Update the fixed-position canvas to align with the PDF container's
   * current bounding rect. Called on resize and when needed.
   */
  private updateCanvasPosition() {
    const rect = this.pdfContainer.getBoundingClientRect();
    this.canvas.style.position = 'fixed';
    this.canvas.style.top = `${rect.top}px`;
    this.canvas.style.left = `${rect.left}px`;
    this.canvas.style.zIndex = '999999998';
  }

  public start() {
    if (this.isSystemRunning) return;
    this.isSystemRunning = true;
    
    // Continuous rendering loop at 60fps - same as original CanvasRenderer
    // This is necessary because handleMove() mutates stroke points directly
    // without going through StrokeManager, so there's no callback to trigger
    // an on-demand render. The loop ensures smooth real-time drawing.
    const loop = () => {
      if (!this.isSystemRunning) return;
      this.draw();
      this.rafId = requestAnimationFrame(loop);
    };
    this.rafId = requestAnimationFrame(loop);
  }

  public stop() {
    this.isSystemRunning = false;
    if (this.rafId) {
      cancelAnimationFrame(this.rafId);
      this.rafId = null;
    }
    this.clearCanvas();
  }

  public requestRender() {
    // With the continuous loop, this is a no-op.
    // Kept for API compatibility with StrokeManager callbacks.
  }

  private clearCanvas() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
  }

  public draw() {
    // 1. Reset transform
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // 2. Apply scroll transform
    // The canvas is positioned at the top-left of the visible viewport (position:sticky)
    // Strokes are in document coordinates (scrollable content coords)
    // To render them in the correct position on the viewport-sized canvas,
    // we offset by -scrollLeft, -scrollTop
    const dpr = window.devicePixelRatio || 1;
    const scrollX = this.pdfContainer.scrollLeft;
    const scrollY = this.pdfContainer.scrollTop;
    
    this.ctx.setTransform(dpr, 0, 0, dpr, -scrollX * dpr, -scrollY * dpr);

    const scale = window.visualViewport?.scale || 1;
    const s = 1 / scale;

    const strokes = this.getStrokes();
    const now = Date.now();
    
    const idleTime = now - this.lastGlobalActivityTime;
    const globalAlpha = Math.max(0, 1 - idleTime / TIMING.laserFadeDuration);

    if (strokes.length > 0) {
      strokes.forEach((stroke) => {
        if (stroke.isSelected) {
          const selColor = 'rgba(59, 130, 246, 0.5)';
          if(stroke.type !== 'rect' && stroke.type !== 'arrow') {
            this.renderStroke(stroke.points, selColor, (stroke.type === 'highlighter' ? 30 : 10) * s, 0, 'source-over');
          }
        }

        if (stroke.type !== 'text' && stroke.points.length < 2) return;
        
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
          const rgb = this.hexToRgb(stroke.color);
          this.renderStroke(stroke.points, `rgba(${rgb}, ${alpha * 0.3})`, 25 * s, 30 * s, 'lighter');
          this.renderStroke(stroke.points, `rgba(${rgb}, ${alpha * 0.8})`, 8 * s, 10 * s, 'lighter');
          this.renderStroke(stroke.points, `rgba(255, 255, 255, ${alpha * 0.95})`, 3 * s, 0, 'source-over');
        }
      });
    }

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

    const drawGeometry = (lineWidth: number, isFill = false) => {
      this.ctx.lineWidth = lineWidth;
      this.ctx.beginPath();
      this.ctx.moveTo(from.x, from.y);
      this.ctx.lineTo(to.x, to.y);
      this.ctx.stroke();

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

    this.ctx.shadowBlur = 15;
    this.ctx.shadowColor = color;
    this.ctx.strokeStyle = color;
    this.ctx.fillStyle = color;
    drawGeometry(width + 4, true);

    this.ctx.shadowBlur = 0;
    this.ctx.strokeStyle = color;
    this.ctx.fillStyle = color;
    drawGeometry(width, true);

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

    this.ctx.shadowBlur = 15;
    this.ctx.shadowColor = color;
    this.ctx.strokeStyle = color;
    this.ctx.lineWidth = width + 4;
    this.ctx.strokeRect(x, y, w, h);

    this.ctx.shadowBlur = 0;
    this.ctx.strokeStyle = color;
    this.ctx.lineWidth = width;
    this.ctx.strokeRect(x, y, w, h);

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
    const x = Math.round(pos.x);

    lines.forEach((line, index) => {
      const y = Math.round(startY + (index * lineHeight));
      
      this.ctx.save();
      this.ctx.shadowBlur = 15;
      this.ctx.shadowColor = color;
      this.ctx.shadowOffsetX = 10000;
      this.ctx.shadowOffsetY = 0;
      this.ctx.fillStyle = color;
      this.ctx.fillText(line, x - 10000, y);
      this.ctx.restore();

      this.ctx.shadowBlur = 0;
      this.ctx.shadowOffsetX = 0;
      this.ctx.shadowOffsetY = 0;
      this.ctx.fillStyle = color;
      this.ctx.fillText(line, x, y);
    });
  }

  public exportToImage(): string {
    const tempCanvas = document.createElement('canvas');
    tempCanvas.width = this.canvas.width;
    tempCanvas.height = this.canvas.height;
    const tempCtx = tempCanvas.getContext('2d')!;
    
    tempCtx.fillStyle = '#ffffff';
    tempCtx.fillRect(0, 0, tempCanvas.width, tempCanvas.height);
    tempCtx.drawImage(this.canvas, 0, 0);
    
    return tempCanvas.toDataURL('image/png');
  }
}
