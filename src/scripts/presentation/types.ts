export interface LaserPoint {
  x: number;
  y: number;
}

export type ToolMode = 'laser' | 'pen' | 'arrow' | 'rect' | 'highlighter' | 'select' | 'hand' | 'text';

export interface LaserStroke {
  points: LaserPoint[];
  isDead: boolean;
  isPermanent: boolean;
  color: string;
  type: ToolMode;
  text?: string;
  isSelected?: boolean;
  // Bounding Box for optimization and selection
  minX?: number;
  maxX?: number;
  minY?: number;
  maxY?: number;
  // Timestamp when stroke was created (for laser fade calculation)
  createdAt?: number;
}
