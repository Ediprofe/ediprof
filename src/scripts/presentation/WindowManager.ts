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
    onCopy?: () => void;
    onPaste?: () => void;
  };

  // Referencia al dock para posicionamiento dinámico
  private dockWrapper: HTMLElement | null = null;

  constructor(events: typeof WindowManager.prototype.events) {
    this.events = events;
  }

  public init() {
    this.injectStyles();
    this.createDock();
    this.setupListeners();
    this.setupKeyboardShortcuts();
    this.setupVisualViewport();
  }

  public destroy() {
    const dock = document.getElementById('presentation-dock');
    if (dock) dock.remove();

    const board = document.getElementById('presentation-board');
    if (board) board.remove();

    const styles = document.getElementById('presentation-mode-styles');
    if (styles) styles.remove();

    window.removeEventListener('keydown', this.boundHandleKey);

    // Limpiar Visual Viewport listeners
    if (window.visualViewport) {
      window.visualViewport.removeEventListener('resize', this.boundUpdateDockPosition);
      window.visualViewport.removeEventListener('scroll', this.boundUpdateDockPosition);
    }

    // Ensure page scroll is always restored when presentation mode closes,
    // even if it was closed while white/black board was active.
    document.body.style.overflow = '';

    this.dockWrapper = null;
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
      text: 'pm-text-btn',
      highlighter: 'pm-highlighter-btn',
      guide: 'pm-guide-btn',
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

  // ============================================
  // VISUAL VIEWPORT - Posicionamiento dinámico con zoom
  // ============================================

  private boundUpdateDockPosition = () => this.updateDockPosition();

  private setupVisualViewport() {
    if (window.visualViewport) {
      window.visualViewport.addEventListener('resize', this.boundUpdateDockPosition);
      window.visualViewport.addEventListener('scroll', this.boundUpdateDockPosition);
    }
    // Posición inicial
    requestAnimationFrame(() => this.updateDockPosition());
  }

  private updateDockPosition() {
    if (!this.dockWrapper) return;

    const vv = window.visualViewport;
    if (!vv) {
      // Fallback para navegadores sin Visual Viewport API
      this.dockWrapper.style.left = '0';
      this.dockWrapper.style.top = `${window.innerHeight - 80}px`;
      this.dockWrapper.style.width = `${window.innerWidth}px`;
      this.dockWrapper.style.transform = 'none';
      return;
    }

    const scale = 1 / vv.scale;

    // Posicionar el wrapper para que cubra el ancho del viewport visual
    // y esté en la parte inferior
    const left = vv.offsetLeft;
    const top = vv.offsetTop + vv.height - 80 * scale;
    const width = vv.width;

    this.dockWrapper.style.left = `${left}px`;
    this.dockWrapper.style.top = `${top}px`;
    this.dockWrapper.style.width = `${width}px`;
    this.dockWrapper.style.transform = `scale(${scale})`;
    this.dockWrapper.style.transformOrigin = 'center top';
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
      return `<button class="color-dot${isDefault ? ' active' : ''}" data-color="${c.hex}" data-shortcut="${c.key}" title="${c.name} (${c.key})" style="background: ${c.hex}; ${borderStyle}"></button>`;
    }).join('\n           ');

    // Dock Container
    this.dockWrapper = document.createElement('div');
    this.dockWrapper.id = 'presentation-dock';
    this.dockWrapper.className = 'presentation-dock-wrapper-bottom';
    this.dockWrapper.innerHTML = `
        <div class="presentation-glass-dock">
        <div style="display:flex;gap:4px">
          <button id="pm-hand-btn" class="dock-btn tool-trigger active" data-shortcut="H" title="Puntero (H)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m3 3 7.07 16.97 2.51-7.39 7.39-2.51L3 3z"></path><path d="m13 13 6 6"></path></svg><span>Puntero</span>
          </button>
           <button id="pm-select-btn" class="dock-btn tool-trigger" data-shortcut="S" title="Seleccionar (S)">
             <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg><span>Selecc.</span>
          </button>
          <button id="pm-arrow-btn" class="dock-btn tool-trigger" data-shortcut="A" title="Flecha (A)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </button>
           <button id="pm-rect-btn" class="dock-btn tool-trigger" data-shortcut="R" title="Rect (R)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"></rect></svg>
          </button>
          <button id="pm-text-btn" class="dock-btn tool-trigger" data-shortcut="T" title="Texto (T)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line></svg>
          </button>
          <button id="pm-laser-btn" class="dock-btn tool-trigger" data-shortcut="L" title="Láser (L)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m13.4 2 3.5 3.5-3.5 3.5-3.5-3.5z"></path><path d="M7.4 15.6 2 21"></path><path d="m15.5 15.5 4-4"></path><path d="M14 17h5"></path><path d="M17 14v5"></path><path d="m7.4 9.4 6.2 6.2"></path></svg><span>Láser</span>
          </button>
          <button id="pm-guide-btn" class="dock-btn tool-trigger" data-shortcut="G" title="Guía (G)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20"></path><path d="M2 8v8"></path><path d="M22 8v8"></path></svg><span>Guía</span>
          </button>
          <button id="pm-pen-btn" class="dock-btn tool-trigger" data-shortcut="P" title="Lápiz (P)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"></path><path d="m15 5 4 4"></path></svg><span>Lápiz</span>
          </button>
          <button id="pm-highlighter-btn" class="dock-btn tool-trigger" data-shortcut="M" title="Resaltador (M)">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m9 11-6 6v3h9l3-3"/><path d="m22 12-4.6 4.6a2 2 0 0 1-2.8 0l-5.2-5.2a2 2 0 0 1 0-2.8L14 4"/></svg>
          </button>
        </div>
        <div class="dock-divider"></div>
        <div id="pm-colors" style="display:flex;gap:4px">
           ${colorDotsHTML}
        </div>
        <div class="dock-divider"></div>
         <div style="display:flex;gap:4px">
           <button id="pm-undo-btn" class="dock-btn" data-shortcut="Ctrl+Z" title="Deshacer (Ctrl+Z)">
             <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7v6h6"></path><path d="M21 17a9 9 0 0 0-9-9 9 9 0 0 0-6 2.3L3 13"></path></svg>
           </button>
           <button id="pm-clear-btn" class="dock-btn" data-shortcut="C" title="Limpiar (C)">
             <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"></path><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"></path><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"></path></svg>
           </button>
           <button id="pm-close-btn" class="dock-btn dock-btn-close" data-shortcut="Esc" title="Cerrar (Esc)">
             <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
           </button>
         </div>
         <div class="dock-divider"></div>
         <div style="display:flex;gap:4px">
           <button id="pm-board-white" class="dock-btn" data-shortcut="W" title="Pizarra Blanca (W)">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><line x1="3" x2="21" y1="9" y2="9"/><line x1="9" x2="9" y1="21" y2="9"/></svg>
           </button>
           <button id="pm-board-black" class="dock-btn" data-shortcut="B" title="Pizarra Negra (B)">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/></svg>
           </button>
         </div>
        </div>
      `;
    document.body.appendChild(this.dockWrapper);
  }

  private setupListeners() {
    document.getElementById('pm-hand-btn')?.addEventListener('click', () => this.events.onToolChange('hand'));
    document.getElementById('pm-select-btn')?.addEventListener('click', () => this.events.onToolChange('select'));
    document.getElementById('pm-laser-btn')?.addEventListener('click', () => this.events.onToolChange('laser'));
    document.getElementById('pm-guide-btn')?.addEventListener('click', () => this.events.onToolChange('guide'));
    document.getElementById('pm-pen-btn')?.addEventListener('click', () => this.events.onToolChange('pen'));
    document.getElementById('pm-arrow-btn')?.addEventListener('click', () => this.events.onToolChange('arrow'));
    document.getElementById('pm-rect-btn')?.addEventListener('click', () => this.events.onToolChange('rect'));
    document.getElementById('pm-text-btn')?.addEventListener('click', () => this.events.onToolChange('text'));
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

    // Ignore shortcuts if typing in an input/textarea
    if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) {
        return;
    }

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

    // Ctrl+C = Copiar
    if (isMod && key === 'c') {
      e.preventDefault();
      this.events.onCopy?.();
      return;
    }

    // Ctrl+V = Pegar
    if (isMod && key === 'v') {
      e.preventDefault();
      this.events.onPaste?.();
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
    if (key === 'c' && !isMod) {
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
