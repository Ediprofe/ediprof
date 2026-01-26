export class WindowManager {
  // Callback events
  private events: {
    onToolChange: (tool: string) => void;
    onColorChange: (color: string) => void;
    onUndo: () => void;
    onClear: () => void;
    onDeleteSelected: () => void;
    onBoardChange: (type: 'none' | 'white' | 'black') => void;
    onClose: () => void;
  }

  constructor(events: typeof WindowManager.prototype.events) {
    this.events = events;
  }

  public init() {
    this.injectStyles();
    this.createDock();
    this.setupListeners();
    this.setupKeyboardShortcuts();
  }
  
  public destroy() {
      const dock = document.getElementById('presentation-dock');
      if (dock) dock.remove();
      
      const board = document.getElementById('presentation-board');
      if (board) board.remove();
      
      const styles = document.getElementById('presentation-mode-styles');
      if (styles) styles.remove();
      
      window.removeEventListener('keydown', this.boundHandleKey);
  }

  public setToolActive(tool: string) {
    document.querySelectorAll('.tool-trigger').forEach(el => el.classList.remove('active'));
    
    const idMap: Record<string, string> = {
        'hand': 'pm-hand-btn',
        'select': 'pm-select-btn',
        'laser': 'pm-laser-btn',
        'pen': 'pm-pen-btn',
        'arrow': 'pm-arrow-btn',
        'rect': 'pm-rect-btn',
        'highlighter': 'pm-highlighter-btn'
    };
    
    const btn = document.getElementById(idMap[tool]);
    if (btn) btn.classList.add('active');
  }

  public setActiveColor(color: string) {
    document.querySelectorAll('#pm-colors .color-dot').forEach((d) => {
       if (d.getAttribute('data-color') === color) d.classList.add('active');
       else d.classList.remove('active');
    });
  }
  
  public setBoardState(type: 'none' | 'white' | 'black') {
      const board = document.getElementById('presentation-board');
      const whiteBtn = document.getElementById('pm-board-white');
      const blackBtn = document.getElementById('pm-board-black');

      if (board) {
         board.className = type === 'none' ? 'presentation-board' : `presentation-board ${type}`;
      }
      
      whiteBtn?.classList.toggle('active', type === 'white');
      blackBtn?.classList.toggle('active', type === 'black');
      
      document.body.style.overflow = type === 'none' ? '' : 'hidden'; // Lock scroll if board open
  }

  private injectStyles() {
     let style = document.getElementById('presentation-mode-styles');
     if (!style) {
       style = document.createElement('style');
       style.id = 'presentation-mode-styles';
       document.head.appendChild(style);
     }
     
     // Always update content to ensure latest styles (handle HMR/updates)
     style.textContent = `
       .presentation-canvas {
         position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
         z-index: 999999998; pointer-events: none; touch-action: none;
       }
       .presentation-canvas.active { pointer-events: auto; cursor: crosshair; }
       .presentation-board {
         position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
         z-index: 999999997; pointer-events: none; opacity: 0;
         background-color: transparent; transition: opacity 0.3s ease;
       }
       .presentation-board.white {
         opacity: 1; pointer-events: auto; background-color: #ffffff;
         background-image: linear-gradient(#e5e7eb 1px, transparent 1px), linear-gradient(90deg, #e5e7eb 1px, transparent 1px);
         background-size: 40px 40px;
       }
       .presentation-board.black {
         opacity: 1; pointer-events: auto; background-color: #1a1a1a;
         background-image: linear-gradient(#333 1px, transparent 1px), linear-gradient(90deg, #333 1px, transparent 1px);
         background-size: 40px 40px;
       }
       .presentation-dock-wrapper {
         position: fixed; top: 12px; left: 50%; transform: translateX(-50%); 
         display: flex; justify-content: center; width: auto;
         z-index: 999999999; pointer-events: none;
       }
       .presentation-glass-dock {
         background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
         border: 1px solid rgba(255, 255, 255, 0.1); padding: 8px 16px; border-radius: 24px;
         display: flex; align-items: center; gap: 10px; pointer-events: auto;
         box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
       }
       /* Ensure elements inside don't break flex layout */
       .presentation-glass-dock > * {
         flex-shrink: 0;
       }

       .dock-btn { 
          background: transparent; border: 1px solid transparent; color: rgba(255, 255, 255, 0.7);
          padding: 0 10px; height: 40px; border-radius: 14px; cursor: pointer; display: flex;
          align-items: center; gap: 8px; font-family: sans-serif; font-size: 0.8rem; font-weight: 500;
       }
       .dock-btn:hover { background: rgba(255, 255, 255, 0.1); color: white; }
       .dock-btn.active { background: #2563eb; color: white; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3); }
       
       /* Specific colors for active states */
       #pm-laser-btn.active { background: #ef4444; box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3); }
       #pm-pen-btn.active { background: #eab308; box-shadow: 0 4px 12px rgba(234, 179, 8, 0.3); }
       #pm-arrow-btn.active { background: #10b981; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3); }
       #pm-rect-btn.active { background: #6366f1; box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3); }
       #pm-select-btn.active { background: #8b5cf6; box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3); }
       #pm-highlighter-btn.active { background: #facc15; color: #000; box-shadow: 0 4px 12px rgba(250, 204, 21, 0.3); }

       .color-dot { width: 20px; height: 20px; border-radius: 50%; border: 2px solid rgba(255,255,255,0.2); cursor: pointer; }
       .color-dot.active { border-color: white; transform: scale(1.25); box-shadow: 0 0 10px rgba(255,255,255,0.3); }
       .dock-divider { width: 1px; height: 24px; background: rgba(255,255,255,0.15); }
       
       /* Tablet Logic: Scale slightly to avoid overlapping sidebars */
       @media (max-width: 1024px) {
          .dock-btn span { display: none; } /* Hide labels on tablet too */
          .presentation-glass-dock { padding: 6px 12px; gap: 6px; }
          .dock-btn { padding: 0 6px; }
       }

       /* Mobile Logic: Smaller scale and hide complex tools if needed */
       @media (max-width: 640px) {
         .presentation-glass-dock { transform: scale(0.9); transform-origin: top center; }
         #pm-arrow-btn, #pm-rect-btn { display: none; }
       }
     `;
  }

  private createDock() {
      if (document.getElementById('presentation-dock')) return;
      
      // Board Background Layer
      const board = document.createElement('div');
      board.id = 'presentation-board';
      board.className = 'presentation-board';
      document.body.appendChild(board);

      // Dock Container
      const dockWrapper = document.createElement('div');
      dockWrapper.id = 'presentation-dock';
      dockWrapper.className = 'presentation-dock-wrapper';
      dockWrapper.innerHTML = `
        <div class="presentation-glass-dock">
        <div style="display:flex;gap:4px">
          <button id="pm-hand-btn" class="dock-btn tool-trigger active" title="Puntero (H)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m3 3 7.07 16.97 2.51-7.39 7.39-2.51L3 3z"></path><path d="m13 13 6 6"></path></svg><span>Puntero</span>
          </button>
           <button id="pm-select-btn" class="dock-btn tool-trigger" title="Seleccionar (S)">
             <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg><span>Selecc.</span>
          </button>
          <button id="pm-arrow-btn" class="dock-btn tool-trigger" title="Flecha (A)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </button>
           <button id="pm-rect-btn" class="dock-btn tool-trigger" title="Rect (R)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"></rect></svg>
          </button>
          <button id="pm-laser-btn" class="dock-btn tool-trigger" title="Láser (L)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m13.4 2 3.5 3.5-3.5 3.5-3.5-3.5z"></path><path d="M7.4 15.6 2 21"></path><path d="m15.5 15.5 4-4"></path><path d="M14 17h5"></path><path d="M17 14v5"></path><path d="m7.4 9.4 6.2 6.2"></path></svg><span>Láser</span>
          </button>
          <button id="pm-pen-btn" class="dock-btn tool-trigger" title="Lápiz (P)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"></path><path d="m15 5 4 4"></path></svg><span>Lápiz</span>
          </button>
          <button id="pm-highlighter-btn" class="dock-btn tool-trigger" title="Resaltador (M)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m9 11-6 6v3h9l3-3"/><path d="m22 12-4.6 4.6a2 2 0 0 1-2.8 0l-5.2-5.2a2 2 0 0 1 0-2.8L14 4"/></svg>
          </button>
        </div>
        <div class="dock-divider"></div>
        <div id="pm-colors" style="display:flex;gap:4px">
           <button class="color-dot" data-color="#FFFFFF" title="Blanco (1)" style="background: #FFFFFF;"></button>
           <button class="color-dot" data-color="#FFD700" title="Amarillo (2)" style="background: #FFD700;"></button>
           <button class="color-dot active" data-color="#EF4444" title="Rojo (3)" style="background: #EF4444;"></button>
           <button class="color-dot" data-color="#3B82F6" title="Azul (4)" style="background: #3B82F6;"></button>
           <button class="color-dot" data-color="#111111" title="Negro (5)" style="background: #111111; border: 1px solid rgba(255,255,255,0.4)"></button>
           <button class="color-dot" data-color="#00FF99" title="Neon Green (6)" style="background: #00FF99; border: 1px solid rgba(255,255,255,0.2)"></button>
        </div>
        <div class="dock-divider"></div>
         <div style="display:flex;gap:4px">
           <button id="pm-undo-btn" class="dock-btn" title="Deshacer (Ctrl+Z)">
             <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7v6h6"></path><path d="M21 17a9 9 0 0 0-9-9 9 9 0 0 0-6 2.3L3 13"></path></svg>
           </button>
           <button id="pm-clear-btn" class="dock-btn" title="Limpiar (C)">
             <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><script>/*ClearIcon*/</script><path d="M3 6h18"></path><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"></path><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"></path></svg>
           </button>
           <button id="pm-close-btn" class="dock-btn dock-btn-close" title="Cerrar (Esc)">
             <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
           </button>
         </div>
         <div class="dock-divider"></div>
         <div style="display:flex;gap:4px">
           <button id="pm-board-white" class="dock-btn" title="Pizarra Blanca (W)">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><line x1="3" x2="21" y1="9" y2="9"/><line x1="9" x2="9" y1="21" y2="9"/></svg>
           </button>
           <button id="pm-board-black" class="dock-btn" title="Pizarra Negra (B)">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/></svg>
           </button>
         </div>
        </div>
      `;
      document.body.appendChild(dockWrapper);
  }

  private setupListeners() {
      document.getElementById('pm-hand-btn')?.addEventListener('click', () => this.events.onToolChange('hand'));
      document.getElementById('pm-select-btn')?.addEventListener('click', () => this.events.onToolChange('select'));
      document.getElementById('pm-laser-btn')?.addEventListener('click', () => this.events.onToolChange('laser'));
      document.getElementById('pm-pen-btn')?.addEventListener('click', () => this.events.onToolChange('pen'));
      document.getElementById('pm-arrow-btn')?.addEventListener('click', () => this.events.onToolChange('arrow'));
      document.getElementById('pm-rect-btn')?.addEventListener('click', () => this.events.onToolChange('rect'));
      document.getElementById('pm-highlighter-btn')?.addEventListener('click', () => this.events.onToolChange('highlighter'));
      
      document.getElementById('pm-undo-btn')?.addEventListener('click', () => this.events.onUndo());
      document.getElementById('pm-clear-btn')?.addEventListener('click', () => this.events.onClear());
      document.getElementById('pm-close-btn')?.addEventListener('click', () => this.events.onClose());
      
      document.getElementById('pm-board-white')?.addEventListener('click', () => this.events.onBoardChange('white'));
      document.getElementById('pm-board-black')?.addEventListener('click', () => this.events.onBoardChange('black'));
      
      document.querySelectorAll('#pm-colors .color-dot').forEach((dot) => {
        dot.addEventListener('click', () => {
          const color = dot.getAttribute('data-color') || '#FFFFFF';
          this.events.onColorChange(color);
        });
      });
  }
  
  private boundHandleKey = (e: KeyboardEvent) => this.handleKeyDown(e);
  
  private setupKeyboardShortcuts() {
      window.addEventListener('keydown', this.boundHandleKey);
  }

  private handleKeyDown(e: KeyboardEvent) {
    const key = e.key.toLowerCase();
    const isMod = e.ctrlKey || e.metaKey;

    if (key === 'escape') this.events.onClose();
    else if (isMod && key === 'z') {
      e.preventDefault();
      this.events.onUndo();
    }
    
    // Tools
    else if (key === 'h') this.events.onToolChange('hand');
    else if (key === 'l') this.events.onToolChange('laser');
    else if (key === 'p') this.events.onToolChange('pen');
    else if (key === 'm') this.events.onToolChange('highlighter');
    else if (key === 's') this.events.onToolChange('select');
    else if (key === 'a') this.events.onToolChange('arrow');
    else if (key === 'r') this.events.onToolChange('rect');
    
    // Boards (idempotent checks handled in controller usually, or here just fire event)
    else if (!isMod && key === 'b') this.events.onBoardChange('black');
    else if (!isMod && key === 'w') this.events.onBoardChange('white');
    
    // Actions
    else if (key === 'c') this.events.onClear();
    else if (key === 'delete' || key === 'backspace') this.events.onDeleteSelected();
    
    // Colors
    else if (key === '1') this.events.onColorChange('#FFFFFF');
    else if (key === '2') this.events.onColorChange('#FFD700');
    else if (key === '3') this.events.onColorChange('#EF4444');
    else if (key === '4') this.events.onColorChange('#3B82F6');
    else if (key === '5') this.events.onColorChange('#111111');
    else if (key === '6') this.events.onColorChange('#00FF99');
  }
}
