
import svgwrite
from sympy import Point, Line, Triangle, Segment
from sympy.geometry import intersection
import os

class GeometryPlotter:
    def __init__(self, filename, width=400, height=320, padding=40):
        self.filename = filename
        self.width = width
        self.height = height
        self.padding = padding
        self.dwg = svgwrite.Drawing(filename, size=(width, height))
        
        # Style definitions
        self.styles = {
            'point': {'r': 4, 'fill': '#1e293b', 'stroke': 'none'},
            'highlight_point': {'r': 6, 'fill': '#ef4444', 'stroke': 'none'},
            'triangle_fill': {'fill': '#dcfce7', 'fill_opacity': 0.3, 'stroke': '#22c55e', 'stroke_width': 2},
            'triangle_fill_obtuse': {'fill': '#fef3c7', 'fill_opacity': 0.3, 'stroke': '#f59e0b', 'stroke_width': 2},
            'triangle_fill_right': {'fill': '#dbeafe', 'fill_opacity': 0.3, 'stroke': '#3b82f6', 'stroke_width': 2},
            'dashed_line': {'stroke': '#3b82f6', 'stroke_width': 1.5, 'stroke_dasharray': '6,4'},
            'helper_line': {'stroke': '#94a3b8', 'stroke_width': 1, 'stroke_dasharray': '4,4'},
            'orthocenter_lines': {'stroke': '#ef4444', 'stroke_width': 1.5, 'stroke_dasharray': '6,4'},
            'text': {'font_family': 'Inter, sans-serif', 'font_size': 14, 'fill': '#1e293b', 'font_weight': 'bold'}
        }
        
    def to_svg_coords(self, point):
        # Maps math coordinates to SVG coordinates
        # We need to define a bounding box for the math coordinates to scale them
        # For this specific task, we will just use 1 unit = 40 pixels and center roughly
        # Or simpler: input raw SVG coordinates into SymPy for calculation, 
        # but remember Y is down in SVG. 
        # To avoid confusion, let's work in SVG coordinates directly for "points"
        # but treating them as geometric entities.
        return (float(point.x), float(point.y))

    def draw_segment(self, p1, p2, **style):
        self.dwg.add(self.dwg.line(start=self.to_svg_coords(p1), 
                                   end=self.to_svg_coords(p2), 
                                   **style))

    def draw_point(self, p, label=None, **style):
        coords = self.to_svg_coords(p)
        self.dwg.add(self.dwg.circle(center=coords, **style))
        if label:
            # Simple offset for label
            self.dwg.add(self.dwg.text(label, insert=(coords[0]+10, coords[1]-10), **self.styles['text']))

    def save(self):
        self.dwg.save()
        print(f"Saved {self.filename}")

def generate_orthocenters():
    output_dir = "public/images/geometria/triangulos"
    os.makedirs(output_dir, exist_ok=True)

    # --- CASE 1: ACUTE TRIANGLE ---
    plot = GeometryPlotter(f"{output_dir}/ortocentro-acutangulo.svg")
    
    # Define points (using SVG coordinate space intuitively: Y increases downwards)
    # A top-ish, B bottom-right, C bottom-left
    A = Point(200, 50)
    B = Point(350, 280)
    C = Point(50, 280)
    
    # Create SymPy Triangle
    T = Triangle(A, B, C)
    
    # Calculate Orthocenter
    altitudes = T.altitudes
    H = T.orthocenter
    
    # Draw Triangle
    plot.dwg.add(plot.dwg.polygon(points=[plot.to_svg_coords(A), plot.to_svg_coords(B), plot.to_svg_coords(C)], 
                                  **plot.styles['triangle_fill']))
    
    # Draw Altitudes (dashed)
    # Altitude from A points to BC
    h_a_segment = Segment(A, T.sides[0].projection(A)) # Side[0] is BC
    # For visual niceness, we draw from vertex to the foot
    # T.altitudes returns lines, we want segments.
    # Manually projecting to be safe
    
    for vertex, side in zip([A, B, C], [T.sides[0], T.sides[1], T.sides[2]]):
         foot = side.projection(vertex)
         plot.draw_segment(vertex, foot, **plot.styles['dashed_line'])
         # Draw foot point
         plot.draw_point(foot, **{'r': 3, 'fill': '#3b82f6'})

    # Draw Vertices and Labels
    plot.draw_point(A, "A", **plot.styles['point'])
    plot.draw_point(B, "B", **plot.styles['point'])
    plot.draw_point(C, "C", **plot.styles['point'])
    
    # Draw Orthocenter
    plot.draw_point(H, "H", **plot.styles['highlight_point'])
    
    plot.save()

    # --- CASE 2: RIGHT TRIANGLE ---
    plot = GeometryPlotter(f"{output_dir}/ortocentro-rectangulo.svg")
    
    # Right angle at A
    A = Point(50, 280)  # Bottom-left (actually let's make it the right-angle vertex)
    B = Point(350, 280) # Bottom-right
    C = Point(50, 50)   # Top-left
    
    T = Triangle(A, B, C)
    H = T.orthocenter # Should be A
    
    plot.dwg.add(plot.dwg.polygon(points=[plot.to_svg_coords(A), plot.to_svg_coords(B), plot.to_svg_coords(C)], 
                                  **plot.styles['triangle_fill_right']))
    
    # Draw Right Angle Symbol
    size = 20
    plot.dwg.add(plot.dwg.path(d=f"M {float(A.x)} {float(A.y)-size} L {float(A.x)+size} {float(A.y)-size} L {float(A.x)+size} {float(A.y)}",
                               fill="none", stroke="#3b82f6", stroke_width=2))

    # Altitudes
    # 1. C to AB (is CA itself) -> drawn as part of triangle, maybe highlight?
    # 2. B to AC (is BA itself)
    # 3. A to BC (calculated)
    foot_A = T.sides[0].projection(A) # BC is side 0 because opposite A
    plot.draw_segment(A, foot_A, **plot.styles['dashed_line'])
    plot.draw_point(foot_A, **{'r': 3, 'fill': '#3b82f6'})
    
    # Draw Vertices
    plot.draw_point(A, "A=H", **plot.styles['highlight_point'])
    plot.draw_point(B, "B", **plot.styles['point'])
    plot.draw_point(C, "C", **plot.styles['point'])

    plot.save()
    
    # --- CASE 3: OBTUSE TRIANGLE ---
    plot = GeometryPlotter(f"{output_dir}/ortocentro-obtusangulo.svg", height=400) # Taller for H outside
    
    # Obtuse angle at A
    # A bit more centered to allow H below
    A = Point(120, 200) 
    B = Point(350, 200)
    C = Point(80, 80)
    
    T = Triangle(A, B, C)
    H = T.orthocenter

    # Extensions for visuals
    # Extend AB to the left
    left_ext = Point(20, 200)
    plot.draw_segment(A, left_ext, **plot.styles['helper_line'])
    
    # Extend AC downwards/leftwards
    # Direction C -> A
    # A + (A-C)*scale
    dir_CA = A - C
    # Simplify, just extend line AC down
    line_AC = Line(A, C)
    # Find a point far enough
    ext_point_AC = A + dir_CA * 1.5 # extend
    
    plot.dwg.add(plot.dwg.line(start=plot.to_svg_coords(C), end=plot.to_svg_coords(H), **plot.styles['helper_line'])) # Line covering C, A, H approx
    
    # Draw Triangle
    plot.dwg.add(plot.dwg.polygon(points=[plot.to_svg_coords(A), plot.to_svg_coords(B), plot.to_svg_coords(C)], 
                                  **plot.styles['triangle_fill_obtuse']))
    
    # Draw Altitudes (connecting vertex to line containing opposite side)
    # Altitude from C to line AB (will hit AB extension)
    foot_C = Line(A, B).projection(C)
    plot.draw_segment(C, foot_C, **plot.styles['dashed_line'])
    
    # Altitude from B to line AC (will hit AC extension)
    foot_B = Line(A, C).projection(B)
    plot.draw_segment(B, foot_B, **plot.styles['dashed_line'])
    
    # Altitude from A to BC (inside?)
    foot_A = Line(B, C).projection(A)
    plot.draw_segment(A, foot_A, **plot.styles['dashed_line'])

    # Connect Orthocenter to vertices to show intersection
    plot.draw_segment(H, A, **plot.styles['orthocenter_lines'])
    plot.draw_segment(H, foot_B, **plot.styles['orthocenter_lines']) # Connect to existing lines
    plot.draw_segment(H, foot_C, **plot.styles['orthocenter_lines'])

    # Draw Vertices
    plot.draw_point(A, "A", **plot.styles['point'])
    plot.draw_point(B, "B", **plot.styles['point'])
    plot.draw_point(C, "C", **plot.styles['point'])
    
    plot.draw_point(H, "H", **plot.styles['highlight_point'])
    
    plot.save()

if __name__ == "__main__":
    generate_orthocenters()
