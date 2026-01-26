import { COLOR_PALETTE, KEYBOARD_SHORTCUTS } from './config';

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
  };

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
    document.querySelectorAll('.tool-trigger').forEach((el) => el.classList.remove('active'));

    const idMap: Record<string, string> = {
      hand: 'pm-hand-btn',
      select: 'pm-select-btn',
      laser: 'pm-laser-btn',
      pen: 'pm-pen-btn',
      arrow: 'pm-arrow-btn',
      rect: 'pm-rect-btn',
      highlighter: 'pm-highlighter-btn',
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

    document.body.style.overflow = type === 'none' ? '' : 'hidden';
  }

  private injectStyles() {
    // Los estilos se importan desde PresentationTrigger.astro
    // Este método se mantiene por compatibilidad y posibles overrides futuros
  }

  private createDock() {
    if (document.getElementById('presentation-dock')) return;

    // Board Background Layer
    const board = document.createElement('div');
    board.id = 'presentation-board';
    board.className = 'presentation-board';
    document.body.appendChild(board);

    // Generar dots de colores desde config
    const colorDotsHTML = COLOR_PALETTE.map((c, i) => {
      const isDefault = i === 2; // Rojo por defecto
      const borderStyle = c.hex === '#111111' ? 'border: 1px solid rgba(255,255,255,0.4)' : '';
      return `<button class="color-dot${isDefault ? ' active' : ''}" data-color="${c.hex}" title="${c.name} (${c.key})" style="background: ${c.hex}; ${borderStyle}"></button>`;
    }).join('\n           ');

    // Dock Container
    const dockWrapper = document.createElement('div');
    dockWrapper.id = 'presentation-dock';
    dockWrapper.className = 'presentation-dock-wrapper-bottom';
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
           ${colorDotsHTML}
        </div>
        <div class="dock-divider"></div>
         <div style="display:flex;gap:4px">
           <button id="pm-undo-btn" class="dock-btn" title="Deshacer (Ctrl+Z)">
             <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7v6h6"></path><path d="M21 17a9 9 0 0 0-9-9 9 9 0 0 0-6 2.3L3 13"></path></svg>
           </button>
           <button id="pm-clear-btn" class="dock-btn" title="Limpiar (C)">
             <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"></path><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"></path><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"></path></svg>
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

    // Escape siempre cierra
    if (key === 'escape') {
      this.events.onClose();
      return;
    }

    // Ctrl+Z = Deshacer
    if (isMod && key === 'z') {
      e.preventDefault();
      this.events.onUndo();
      return;
    }

    // Herramientas (desde config)
    const toolShortcuts = KEYBOARD_SHORTCUTS.tools as Record<string, string>;
    if (toolShortcuts[key]) {
      this.events.onToolChange(toolShortcuts[key]);
      return;
    }

    // Boards (sin modificadores)
    const boardShortcuts = KEYBOARD_SHORTCUTS.boards as Record<string, string>;
    if (!isMod && boardShortcuts[key]) {
      this.events.onBoardChange(boardShortcuts[key] as 'white' | 'black');
      return;
    }

    // Acciones
    if (key === 'c') {
      this.events.onClear();
      return;
    }

    if (key === 'delete' || key === 'backspace') {
      this.events.onDeleteSelected();
      return;
    }

    // Colores (desde config)
    const colorMatch = COLOR_PALETTE.find((c) => c.key === key);
    if (colorMatch) {
      this.events.onColorChange(colorMatch.hex);
    }
  }
}
