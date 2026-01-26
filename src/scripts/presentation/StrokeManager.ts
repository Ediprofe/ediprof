import type { LaserStroke, ToolMode } from './types';

export class StrokeManager {
  private strokes: LaserStroke[] = [];
  private onUpdate: () => void;
  public selectionBox: { x: number, y: number, w: number, h: number } | null = null;
  public isSelecting: boolean = false;

  constructor(onUpdate: () => void) {
    this.onUpdate = onUpdate;
  }

  public getStrokes(): LaserStroke[] {
    return this.strokes;
  }

  public addStroke(stroke: LaserStroke) {
    this.strokes.push(stroke);
    this.onUpdate();
  }

  public setStrokes(strokes: LaserStroke[]) {
    this.strokes = strokes;
    this.onUpdate();
  }

  // CRITICAL: Restoration of "Smart Undo" logic
  public undo() {
    if (this.strokes.length === 0) return;

    // Check the last stroke added
    const lastStroke = this.strokes[this.strokes.length - 1];

    if (!lastStroke.isPermanent) {
      // SCENARIO 1: laser.
      // User intent: "Clear the laser trails"
      // Action: Remove ALL non-permanent (laser) strokes.
      this.strokes = this.strokes.filter(s => s.isPermanent);
    } else {
      // SCENARIO 2: Permanent stroke (Pen, Arrow, Rect).
      // User intent: Undo the last action finely.
      this.strokes.pop();
    }
    
    this.onUpdate();
  }

  public clearAll() {
    this.strokes = [];
    this.onUpdate();
  }

  public deleteSelected() {
     const initialCount = this.strokes.length;
     this.strokes = this.strokes.filter(s => !s.isSelected);
     if (this.strokes.length !== initialCount) {
         this.onUpdate();
     }
  }

  // Called periodically to cleanup "dead" strokes if we implemented fading logic inside StrokeManager
  // But currently fading is visual-only based on timestamp in Renderer.
  // Unless we want to physically remove old laser strokes? 
  // The original code did: checks duration and removes.
  public cleanupOldStrokes(maxAge: number, lastActivityTime: number) {
      // In original code:
      // if (timeSinceLastActivity > duration) this.strokes = this.strokes.filter(s => s.isPermanent);
      // We can replicate that logic in the Controller loop.
  }
  
  public computeSelection(box: { x: number, y: number, w: number, h: number }) {
      const rx = Math.min(box.x, box.x + box.w);
      const ry = Math.min(box.y, box.y + box.h);
      const rw = Math.abs(box.w);
      const rh = Math.abs(box.h);

      let hasSelection = false;

      this.strokes.forEach(s => {
          if (!s.isPermanent) return; // Don't select laser
          
          const sMinX = s.minX ?? -Infinity;
          const sMaxX = s.maxX ?? Infinity;
          const sMinY = s.minY ?? -Infinity;
          const sMaxY = s.maxY ?? Infinity;

          const intersects = !(sMaxX < rx || sMinX > rx + rw || sMaxY < ry || sMinY > ry + rh);
           
          if (intersects) {
              s.isSelected = true;
              hasSelection = true;
          } else {
              // Only deselect if we are strictly selecting new things?
              // Usually selection tool clears previous selection on start, handled in Start.
          }
      });
      
      return hasSelection;
  }
  
  public deselectAll() {
      this.strokes.forEach(s => s.isSelected = false);
      this.onUpdate();
  }
  
  public hasSelectedStrokes(): boolean {
      return this.strokes.some(s => s.isSelected);
  }
}
