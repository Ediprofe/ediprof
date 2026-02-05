import { StrokeManager } from './StrokeManager';
import { CanvasRenderer } from './CanvasRenderer';
import { InputHandler } from './InputHandler';
import { WindowManager } from './WindowManager';
import { TextHighlighter } from './TextHighlighter';
import { TOOL_COLORS, UI_COLORS } from './config';
import type { LaserPoint, ToolMode, LaserStroke } from './types';

export class PresentationController {
  private strokeManager: StrokeManager;
  private renderer: CanvasRenderer;
  private inputHandler: InputHandler;
  private windowManager: WindowManager;
  private textHighlighter: TextHighlighter;

  private currentTool: ToolMode = 'hand';
  private currentColor: string = TOOL_COLORS.red;
  private systemRunning = false;
  private currentStroke: LaserStroke | null = null;
  private clipboard: LaserStroke[] = [];
  private isDragging = false;
  private lastDragPoint: LaserPoint | null = null;
  
  // Resize Observer
  private resizeObserver: ResizeObserver | null = null;
  private onExitCallback: (() => void) | undefined;
  private canvas: HTMLCanvasElement;

  constructor(onExit?: () => void) {
     this.onExitCallback = onExit;

     // 1. Setup Canvas
     this.canvas = document.createElement('canvas');
     this.canvas.id = 'presentation-canvas';
     this.canvas.className = 'presentation-canvas';
     document.body.appendChild(this.canvas);

     // 2. Initialize Components
     this.strokeManager = new StrokeManager(() => this.requestRender());
     
     this.renderer = new CanvasRenderer(
        this.canvas,
        () => this.strokeManager.getStrokes(),
        () => this.strokeManager.selectionBox,
        () => this.strokeManager.isSelecting
     );
     
     this.inputHandler = new InputHandler(
        this.canvas,
        (p, mt, sh) => this.handleStart(p, mt, sh),
        (p, mt, sh) => this.handleMove(p, mt, sh),
        () => this.handleStop()
     );
     
     // 3. UI Manager with Event Callbacks
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
     
     // 4. Text Highlighter (para resaltar texto del DOM)
     this.textHighlighter = new TextHighlighter();
     
     this.start();
  }
  
  private start() {
      if (this.systemRunning) return;
      this.systemRunning = true;
      
      this.windowManager.init();
      this.renderer.startLoop();
      
      // Activar resaltado de texto en modo puntero por defecto
      this.textHighlighter.activate();
      
      // Auto-resize handling
      this.resizeObserver = new ResizeObserver(() => this.renderer.resize());
      this.resizeObserver.observe(document.body);
      window.addEventListener('resize', this.boundResize);
      window.addEventListener('scroll', this.boundScroll, { passive: true });
      
      this.renderer.resize();
  }
  
  public stop() {
      this.systemRunning = false;
      this.strokeManager.clearAll();
      this.renderer.stopLoop();
      this.windowManager.destroy();
      this.inputHandler.destroy();
      
      // Limpiar resaltados Y desactivar
      this.textHighlighter.clearAll();
      this.textHighlighter.deactivate();
      
      this.resizeObserver?.disconnect();
      window.removeEventListener('resize', this.boundResize);
      window.removeEventListener('scroll', this.boundScroll);
      
      this.canvas.remove();
      
      this.onExitCallback?.();
  }
  
  private boundResize = () => this.renderer.resize();
  private boundScroll = () => {
      // Just ensure we render on scroll if loop isn't running constantly?
      // Renderer has a loop, so we are good.
      // But we can force a render if optimization stopped the loop.
  };
  
  private requestRender() {
      // Logic if we wanted to only render on change.
      // Current renderer runs requestAnimationFrame loop always when active to handle laser fading.
  }
  
  /* ================= TOOL LOGIC ================= */
  
  private setTool(tool: ToolMode) {
      this.currentTool = tool;
      this.inputHandler.setInputActive(tool !== 'hand');
      this.windowManager.setToolActive(tool);
      
      // Canvas cursor
      const canvas = document.getElementById('presentation-canvas');
      if (canvas) canvas.classList.toggle('active', tool !== 'hand');
      
      // Text Highlighter: solo detecta selecciones en modo puntero (hand)
      // Pero los resaltados existentes se MANTIENEN visibles en otras herramientas
      if (tool === 'hand') {
          this.textHighlighter.activate();
      } else {
          this.textHighlighter.pause(); // Solo pausa, no limpia
      }
  }
  
  private setColor(color: string) {
      this.currentColor = color;
      this.windowManager.setActiveColor(color);
      
      // UX: Switch to pen if color clicked while in Hand/Laser
      if (this.currentTool === 'hand' || this.currentTool === 'laser' || this.currentTool === 'select') {
          this.setTool('pen');
      }
  }
  
  private handleUndo() {
      // Deshacer el último elemento (stroke o resaltado según orden)
      // Por ahora, undo funciona principalmente para strokes
      // Los resaltados se deshacen con su propio sistema cuando estás en modo puntero
      this.strokeManager.undo();
  }
  
  private handleClear() {
      // Limpiar todo: strokes y resaltados
      this.strokeManager.clearAll();
      this.textHighlighter.clearAll();
  }
  
  /* ================= INPUT LOGIC ================= */
  
  private handleStart(p: LaserPoint, isMultiTouch: boolean, isShift: boolean) {
      if (this.currentTool === 'text') {
          // Use textarea for multi-line support
          const input = document.createElement('textarea');
          
          input.style.position = 'absolute';
          input.style.left = `${p.x}px`;
          input.style.top = `${p.y - 20}px`;
          input.style.background = 'transparent';
          input.style.border = '1px dashed rgba(255,255,255,0.3)'; // Visual cue for editing area
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
          input.style.whiteSpace = 'pre'; // Preserve whitespace

          // Initial size
          input.style.minWidth = '50px';
          input.style.width = '20px'; // Start small to measure
          input.style.height = '40px';
          
          document.body.appendChild(input);
          
          const resizeInput = () => {
             input.style.width = '0px';
             input.style.height = '0px';
             
             // +10 buffer to avoid scrollbars flickering
             const newW = input.scrollWidth + 20;
             const newH = input.scrollHeight;
             
             // Prevent expanding beyond viewport width to avoid horizontal scroll
             const maxWidth = window.innerWidth - p.x - 20;
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
              // CRITICAL: Stop propagation to prevent WindowManager from triggering shortcuts
              // (e.g. 'c' clearing the board, 't' switching tools, etc.)
              e.stopPropagation();

              if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault(); // Prevent default new line if committing
                  commitText();
              } else if (e.key === 'Escape') {
                  input.remove();
              }
              // Shift+Enter allows new line naturally
              // Auto-resize will handle height increase
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
          // 1. Check if clicking on an already selected item to start DRAG
          const selected = this.strokeManager.getSelectedStrokes();
          if (selected.length > 0) {
              // Check hit on any selected stroke bbox
              const hit = selected.some(s => {
                  const sMinX = s.minX ?? -Infinity;
                  const sMaxX = s.maxX ?? Infinity;
                  const sMinY = s.minY ?? -Infinity;
                  const sMaxY = s.maxY ?? Infinity;
                  // Expand bbox slightly for easier grabbing
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

          // 2. Otherwise start SELECTION BOX
          this.strokeManager.isSelecting = true;
          this.strokeManager.selectionBox = { x: p.x, y: p.y, w: 0, h: 0 };
          this.strokeManager.deselectAll();
          
          return;
      }
  
      this.currentStroke = {
          points: [p],
          isDead: false,
          isPermanent: this.currentTool !== 'laser',
          color: this.currentTool === 'laser' ? UI_COLORS.laser : this.currentColor,
          type: this.currentTool,
          isSelected: false
      };
      
      this.strokeManager.addStroke(this.currentStroke);
      
      if (this.currentTool === 'laser') {
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
                  // Update cached BBox
                  if (s.minX !== undefined) s.minX += dx;
                  if (s.maxX !== undefined) s.maxX += dx;
                  if (s.minY !== undefined) s.minY += dy;
                  if (s.maxY !== undefined) s.maxY += dy;
              });
              
              this.lastDragPoint = p;
              // Force render call if needed (renderer loop usually handles it, but just in case)
              // this.requestRender(); 
              return;
          }

          if (this.strokeManager.isSelecting && this.strokeManager.selectionBox) {
              this.strokeManager.selectionBox.w = p.x - this.strokeManager.selectionBox.x;
              this.strokeManager.selectionBox.h = p.y - this.strokeManager.selectionBox.y;
          }
          return;
      }
  
      if (this.currentStroke) {
          // Si es forma (Arrow, Rect) O si es herramienta de dibujo (Pen, Highlighter) con Shift presionado
          const isDrawToolWithShift = (this.currentStroke.type === 'pen' || this.currentStroke.type === 'highlighter') && isShift;

          if (this.currentStroke.type === 'arrow' || this.currentStroke.type === 'rect' || isDrawToolWithShift) {
              let targetP = p;

              // Lógica de Shift para ortogonalidad (0, 45, 90 grados)
              if (isShift) {
                  const startP = this.currentStroke.points[0];
                  const dx = p.x - startP.x;
                  const dy = p.y - startP.y;
                  const absDx = Math.abs(dx);
                  const absDy = Math.abs(dy);

                  // Si dx es mucho mayor que dy, forzar horizontal
                  if (absDy < absDx * 0.5) {
                      targetP = { x: p.x, y: startP.y };
                  } 
                  // Si dy es mucho mayor que dx, forzar vertical
                  else if (absDx < absDy * 0.5) {
                       targetP = { x: startP.x, y: p.y };
                  }
                  // Diagonal perfecta
                  else {
                      const signX = Math.sign(dx);
                      const signY = Math.sign(dy);
                      const len = Math.max(absDx, absDy);
                      targetP = { x: startP.x + len * signX, y: startP.y + len * signY };
                  }
              }

              // Shapes and Shift-Draw update to be just Start -> End (Straight Line)
              this.currentStroke.points = [this.currentStroke.points[0], targetP];
          } else {
              // Freehand drawing
              this.currentStroke.points.push(p);
          }
          
          if (this.currentTool === 'laser') {
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
           // Compute BBox for future selection efficiency
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
           
           this.currentStroke = null;
           
           if (this.currentTool === 'laser') {
              this.renderer.setLastActivityTime(Date.now());
           }
      }
  }

  private handleCopy() {
    const selected = this.strokeManager.getSelectedStrokes();
    if (selected.length > 0) {
      // Deep clone to avoid reference issues
      this.clipboard = JSON.parse(JSON.stringify(selected));
    }
  }

  private handlePaste() {
    if (this.clipboard.length === 0) return;

    // Deselect current selection
    this.strokeManager.deselectAll();

    // Clone clipboard content to allow multiple pastes
    const toPaste: LaserStroke[] = JSON.parse(JSON.stringify(this.clipboard));

    // Calculate bounding box of clipboard content to center or offset logic
    // For simplicity: just offset by 20px
    const offset = 20;

    toPaste.forEach(stroke => {
      // Offset points
      stroke.points.forEach(p => {
        p.x += offset;
        p.y += offset;
      });

      // Update bbox if it exists
      if (stroke.minX !== undefined) stroke.minX += offset;
      if (stroke.maxX !== undefined) stroke.maxX += offset;
      if (stroke.minY !== undefined) stroke.minY += offset;
      if (stroke.maxY !== undefined) stroke.maxY += offset;

      // Select the new pasted strokes
      stroke.isSelected = true;

      // Treat as new strokes
      this.strokeManager.addStroke(stroke);
    });

    // Update clipboard content positions in memory so next paste cascades
    this.clipboard = JSON.parse(JSON.stringify(toPaste));
    
    // Switch to select tool if not active, so user sees the pasted items selected
    if (this.currentTool !== 'select') {
        this.setTool('select');
    }
  }
}
