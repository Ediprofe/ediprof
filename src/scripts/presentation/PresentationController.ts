import { StrokeManager } from './StrokeManager';
import { CanvasRenderer } from './CanvasRenderer';
import { InputHandler } from './InputHandler';
import { WindowManager } from './WindowManager';
import { TOOL_COLORS, UI_COLORS } from './config';
import type { LaserPoint, ToolMode, LaserStroke } from './types';

export class PresentationController {
  private strokeManager: StrokeManager;
  private renderer: CanvasRenderer;
  private inputHandler: InputHandler;
  private windowManager: WindowManager;

  private currentTool: ToolMode = 'hand';
  private currentColor: string = TOOL_COLORS.red;
  private systemRunning = false;
  private currentStroke: LaserStroke | null = null;
  
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
        (p, mt) => this.handleStart(p, mt),
        (p, mt) => this.handleMove(p, mt),
        () => this.handleStop()
     );
     
     // 3. UI Manager with Event Callbacks
     this.windowManager = new WindowManager({
        onToolChange: (t) => this.setTool(t as ToolMode),
        onColorChange: (c) => this.setColor(c),
        onUndo: () => this.strokeManager.undo(),
        onClear: () => this.strokeManager.clearAll(),
        onDeleteSelected: () => this.strokeManager.deleteSelected(),
        onBoardChange: (t) => this.windowManager.setBoardState(t),
        onClose: () => this.stop()
     });
     
     this.start();
  }
  
  private start() {
      if (this.systemRunning) return;
      this.systemRunning = true;
      
      this.windowManager.init();
      this.renderer.startLoop();
      
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
  }
  
  private setColor(color: string) {
      this.currentColor = color;
      this.windowManager.setActiveColor(color);
      
      // UX: Switch to pen if color clicked while in Hand/Laser
      if (this.currentTool === 'hand' || this.currentTool === 'laser' || this.currentTool === 'select') {
          this.setTool('pen');
      }
  }
  
  /* ================= INPUT LOGIC ================= */
  
  private handleStart(p: LaserPoint, isMultiTouch: boolean) {
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
          this.strokeManager.isSelecting = true;
          this.strokeManager.selectionBox = { x: p.x, y: p.y, w: 0, h: 0 };
          
          // Deselect previous on new selection start?
          // Common behavior: clicking outside selection clears it. 
          // Dragging starts new selection.
          // Let's clear previous selection unless Shift held? (Skip shift for now).
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
  
  private handleMove(p: LaserPoint, isMultiTouch: boolean) {
      if (this.currentTool === 'select') {
          if (this.strokeManager.isSelecting && this.strokeManager.selectionBox) {
              this.strokeManager.selectionBox.w = p.x - this.strokeManager.selectionBox.x;
              this.strokeManager.selectionBox.h = p.y - this.strokeManager.selectionBox.y;
          }
          return;
      }
  
      if (this.currentStroke) {
          if (this.currentStroke.type === 'arrow' || this.currentStroke.type === 'rect') {
              // Shapes update their second point
              this.currentStroke.points = [this.currentStroke.points[0], p];
          } else {
              // Lines add points
              this.currentStroke.points.push(p);
          }
          
          if (this.currentTool === 'laser') {
              this.renderer.setLastActivityTime(Date.now());
          }
      }
  }
  
  private handleStop() {
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
}
