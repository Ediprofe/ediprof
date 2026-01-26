export interface LaserPoint {
  x: number;
  y: number;
}

export type ToolMode = 'laser' | 'pen' | 'arrow' | 'rect' | 'highlighter' | 'select' | 'hand';

export interface LaserStroke {
  points: LaserPoint[];
  isDead: boolean;
  isPermanent: boolean;
  color: string;
  type: ToolMode;
  isSelected?: boolean;
  // Bounding Box for optimization and selection
  minX?: number;
  maxX?: number;
  minY?: number;
  maxY?: number;
}
