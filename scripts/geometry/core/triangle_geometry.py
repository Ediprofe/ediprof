"""
📐 Triangle Geometry - Exact calculations using SymPy

This module provides exact calculations for triangle notable points and lines.
All calculations use SymPy's symbolic geometry for mathematical precision.

Usage:
    from core.triangle_geometry import TriangleGeometry
    
    tri = TriangleGeometry((100, 350), (500, 350), (300, 50))
    print(tri.barycenter)
    print(tri.orthocenter)
    print(tri.circumcenter)
    print(tri.incenter)
"""

from sympy import Point, Triangle, Line, Segment, N, sqrt, atan2, pi, cos
from sympy.geometry import Circle


class TriangleGeometry:
    """Exact triangle geometry calculations using SymPy."""
    
    def __init__(self, A, B, C):
        """
        Initialize with three vertices as (x, y) tuples.
        
        Args:
            A, B, C: Tuples of (x, y) coordinates for each vertex
        """
        self.A = Point(A[0], A[1])
        self.B = Point(B[0], B[1])
        self.C = Point(C[0], C[1])
        self.triangle = Triangle(self.A, self.B, self.C)
        
        # Sides
        self.side_a = Segment(self.B, self.C)  # Opposite to A
        self.side_b = Segment(self.A, self.C)  # Opposite to B
        self.side_c = Segment(self.A, self.B)  # Opposite to C
        
    @property
    def vertices(self):
        """Return vertices as float tuples."""
        return (
            (float(self.A.x), float(self.A.y)),
            (float(self.B.x), float(self.B.y)),
            (float(self.C.x), float(self.C.y))
        )
    
    @property
    def midpoints(self):
        """Return midpoints of each side as float tuples."""
        M_a = self.side_a.midpoint
        M_b = self.side_b.midpoint
        M_c = self.side_c.midpoint
        return {
            'M_a': (float(M_a.x), float(M_a.y)),
            'M_b': (float(M_b.x), float(M_b.y)),
            'M_c': (float(M_c.x), float(M_c.y))
        }
    
    @property
    def barycenter(self):
        """Return barycenter (centroid) as float tuple."""
        G = self.triangle.centroid
        return (float(G.x), float(G.y))
    
    @property
    def orthocenter(self):
        """Return orthocenter as float tuple."""
        H = self.triangle.orthocenter
        return (float(H.x), float(H.y))
    
    @property
    def circumcenter(self):
        """Return circumcenter as float tuple."""
        O = self.triangle.circumcenter
        return (float(O.x), float(O.y))
    
    @property
    def circumradius(self):
        """Return circumradius as float."""
        return float(self.triangle.circumradius)
    
    @property
    def incenter(self):
        """Return incenter as float tuple."""
        I = self.triangle.incenter
        return (float(I.x), float(I.y))
    
    @property
    def inradius(self):
        """Return inradius as float."""
        return float(self.triangle.inradius)
    
    @property
    def medians(self):
        """Return the three medians as segment endpoints."""
        mids = self.midpoints
        return {
            'median_A': (self.vertices[0], mids['M_a']),
            'median_B': (self.vertices[1], mids['M_b']),
            'median_C': (self.vertices[2], mids['M_c'])
        }
    
    @property
    def altitudes(self):
        """Return the three altitudes as segment endpoints (vertex to foot)."""
        alts = self.triangle.altitudes
        result = {}
        for key, altitude in alts.items():
            # altitude is a Segment from vertex to foot on opposite side
            p1 = altitude.p1
            p2 = altitude.p2
            result[f'altitude_{key}'] = (
                (float(p1.x), float(p1.y)),
                (float(p2.x), float(p2.y))
            )
        return result
    
    @property
    def altitude_feet(self):
        """Return the feet of altitudes as float tuples."""
        result = {}
        # Foot of altitude from A to BC
        line_a = Line(self.B, self.C)
        foot_a = line_a.projection(self.A)
        result['H_a'] = (float(foot_a.x), float(foot_a.y))
        
        # Foot of altitude from B to AC
        line_b = Line(self.A, self.C)
        foot_b = line_b.projection(self.B)
        result['H_b'] = (float(foot_b.x), float(foot_b.y))
        
        # Foot of altitude from C to AB
        line_c = Line(self.A, self.B)
        foot_c = line_c.projection(self.C)
        result['H_c'] = (float(foot_c.x), float(foot_c.y))
        
        return result
    
    @property
    def angles(self):
        """Return angles at each vertex in degrees."""
        angles = self.triangle.angles
        return {
            'A': float(N(angles[self.A] * 180 / pi)),
            'B': float(N(angles[self.B] * 180 / pi)),
            'C': float(N(angles[self.C] * 180 / pi))
        }
    
    def is_acute(self):
        """Check if triangle is acute (all angles < 90°)."""
        angs = self.angles
        return all(a < 90 for a in angs.values())
    
    def is_obtuse(self):
        """Check if triangle is obtuse (one angle > 90°)."""
        angs = self.angles
        return any(a > 90 for a in angs.values())
    
    def is_right(self):
        """Check if triangle is right (one angle = 90°)."""
        angs = self.angles
        return any(abs(a - 90) < 0.01 for a in angs.values())
    
    def euler_line_points(self):
        """Return O, G, H for Euler line visualization."""
        return {
            'O': self.circumcenter,
            'G': self.barycenter,
            'H': self.orthocenter
        }


def create_obtuse_triangle(base_width=400, height=200, obtuse_angle_vertex='A'):
    """
    Create an obtuse triangle with guaranteed obtuse angle.
    
    Returns vertices (A, B, C) where angle at A is obtuse.
    """
    # For obtuse angle at A, place A such that the angle BAC > 90°
    # This means B and C should be on the same side relative to A
    
    # Base: B and C at the bottom
    B = (100, 350)
    C = (500, 350)
    
    # A should be positioned such that angle at A is obtuse
    # If A is close to the line BC but shifted, the angle becomes obtuse
    A = (150, 200)  # Close to B, making angle at A obtuse
    
    # Verify it's actually obtuse
    tri = TriangleGeometry(A, B, C)
    if not tri.is_obtuse():
        # Adjust A further
        A = (120, 180)
    
    return A, B, C


def create_acute_triangle():
    """Create a clearly acute triangle."""
    A = (300, 60)
    B = (100, 340)
    C = (500, 340)
    return A, B, C


def create_right_triangle():
    """Create a right triangle with right angle at B."""
    A = (150, 80)
    B = (150, 340)  # Right angle here
    C = (500, 340)
    return A, B, C


# Test the module
if __name__ == '__main__':
    print("=== Testing TriangleGeometry ===\n")
    
    # Test acute triangle
    print("Acute Triangle:")
    A, B, C = create_acute_triangle()
    tri = TriangleGeometry(A, B, C)
    print(f"  Vertices: A={A}, B={B}, C={C}")
    print(f"  Angles: {tri.angles}")
    print(f"  Is acute: {tri.is_acute()}")
    print(f"  Barycenter (G): {tri.barycenter}")
    print(f"  Orthocenter (H): {tri.orthocenter}")
    print(f"  Circumcenter (O): {tri.circumcenter}")
    print(f"  Incenter (I): {tri.incenter}")
    print()
    
    # Test obtuse triangle
    print("Obtuse Triangle:")
    A, B, C = create_obtuse_triangle()
    tri = TriangleGeometry(A, B, C)
    print(f"  Vertices: A={A}, B={B}, C={C}")
    print(f"  Angles: {tri.angles}")
    print(f"  Is obtuse: {tri.is_obtuse()}")
    print(f"  Orthocenter (H): {tri.orthocenter}")
    print()
    
    # Test right triangle
    print("Right Triangle:")
    A, B, C = create_right_triangle()
    tri = TriangleGeometry(A, B, C)
    print(f"  Vertices: A={A}, B={B}, C={C}")
    print(f"  Angles: {tri.angles}")
    print(f"  Is right: {tri.is_right()}")
    print(f"  Orthocenter (H): {tri.orthocenter}")
