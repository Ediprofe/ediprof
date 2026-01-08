
from pathlib import Path
from core.base import Point
from core.svg_builder import SVGBuilder
from core.colors import COLORS

OUTPUT_DIR = Path('public/images/matematicas/algebra/ecuaciones-lineales')

# --- SHARED HELPERS ---

def draw_number_line(builder, y, center_val, scale, x_offset=300, min_val=-8, max_val=8):
    """Draws a standard number line."""
    builder.line(Point(20, y), Point(580, y), stroke=COLORS['axis'], stroke_width=2, marker_end='arrow')
    
    start_i = int(min_val)
    end_i = int(max_val) + 1
    
    for i in range(start_i, end_i):
        # Position relative to the conceptual center value placed at x_offset
        # x_pos = x_offset + (i - center_val) * scale
        # Actually simpler: mapping function
        pass # implemented inside specific functions usually but let's keep it flexible

# --- MAIN RENDERERS ---

def create_basic_absolute_value():
    """Generates an illustration for |x| = d"""
    builder = SVGBuilder(600, 200)
    builder.rect(0, 0, 600, 200, fill=COLORS['background'])
    
    y_axis = 120
    center_x = 300
    scale = 30
    
    # Draw number line
    builder.line(Point(20, y_axis), Point(580, y_axis), stroke=COLORS['axis'], stroke_width=2, marker_end='arrow')
    
    for i in range(-7, 8):
        x = center_x + i * scale
        h = 10 if i == 0 else 5
        builder.line(Point(x, y_axis - h), Point(x, y_axis + h), stroke=COLORS['axis'], stroke_width=1)
        if i % 2 == 0 and i != 0:
            builder.text(str(i), Point(x, y_axis + 25), font_size=12, fill=COLORS['text_light'])
    
    builder.text("0", Point(center_x, y_axis + 25), font_size=12, fill=COLORS['text_light'], font_weight='bold')

    d = 4
    x_pos = center_x + d * scale
    x_neg = center_x - d * scale
    
    builder.point(Point(x_pos, y_axis), radius=5, fill=COLORS['point'])
    builder.point(Point(x_neg, y_axis), radius=5, fill=COLORS['point'])
    
    y_arrow = y_axis - 30
    builder.arrow(Point(center_x, y_arrow), Point(x_pos, y_arrow), stroke=COLORS['primary'], stroke_width=2)
    builder.arrow(Point(center_x, y_arrow), Point(x_neg, y_arrow), stroke=COLORS['primary'], stroke_width=2)
    
    builder.text("distancia = d", Point(center_x + d*scale/2, y_arrow - 15), font_size=12, fill=COLORS['primary'])
    builder.text("distancia = d", Point(center_x - d*scale/2, y_arrow - 15), font_size=12, fill=COLORS['primary'])
    
    builder.label("x = d", Point(x_pos, y_axis + 45), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    builder.label("x = -d", Point(x_neg, y_axis + 45), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])

    builder.formula_box("|x| = d", Point(300, 30))
    
    builder.save(OUTPUT_DIR / 'absolute_value_basic.svg')

def create_shifted_absolute_value():
    """Generates an illustration for |x - a| = d"""
    builder = SVGBuilder(600, 250)
    builder.rect(0, 0, 600, 250, fill=COLORS['background'])
    
    y_axis = 140
    center_x = 300
    scale = 30
    
    builder.line(Point(20, y_axis), Point(580, y_axis), stroke=COLORS['axis'], stroke_width=2, marker_end='arrow')
    
    for i in range(-7, 8):
        x = center_x + i * scale
        h = 5
        builder.line(Point(x, y_axis - h), Point(x, y_axis + h), stroke=COLORS['axis'], stroke_width=1)
        if i % 2 == 0:
             builder.text(str(i), Point(x, y_axis + 25), font_size=10, fill=COLORS['text_light'])

    a = 2
    x_a = center_x + a * scale
    
    builder.line(Point(x_a, y_axis - 15), Point(x_a, y_axis + 15), stroke=COLORS['secondary'], stroke_width=2, dashed=True)
    builder.text("a", Point(x_a, y_axis - 25), font_size=14, fill=COLORS['secondary'], font_weight='bold')
    
    d = 3
    x_right = x_a + d * scale
    x_left = x_a - d * scale
    
    builder.point(Point(x_right, y_axis), radius=5, fill=COLORS['point'])
    builder.point(Point(x_left, y_axis), radius=5, fill=COLORS['point'])
    
    y_arrow = y_axis - 50
    builder.arrow(Point(x_a, y_arrow), Point(x_right, y_arrow), stroke=COLORS['primary'], stroke_width=2)
    builder.arrow(Point(x_a, y_arrow), Point(x_left, y_arrow), stroke=COLORS['primary'], stroke_width=2)
    
    builder.line(Point(x_a, y_axis - 15), Point(x_a, y_arrow), stroke=COLORS['secondary'], stroke_width=1, dashed=True)
    builder.line(Point(x_right, y_axis), Point(x_right, y_arrow), stroke=COLORS['point'], stroke_width=1, dashed=True)
    builder.line(Point(x_left, y_axis), Point(x_left, y_arrow), stroke=COLORS['point'], stroke_width=1, dashed=True)

    builder.text("d", Point(x_a + d*scale/2, y_arrow - 15), font_size=12, fill=COLORS['primary'])
    builder.text("d", Point(x_a - d*scale/2, y_arrow - 15), font_size=12, fill=COLORS['primary'])
    
    builder.text("Caso Positivo", Point(x_a + d*scale/2 + 30, y_arrow - 35), font_size=11, fill=COLORS['text_light'])
    builder.text("x - a = d", Point(x_a + d*scale/2 + 30, y_arrow - 50), font_size=12, fill=COLORS['text'], font_weight='bold')
    
    builder.text("Caso Negativo", Point(x_a - d*scale/2 - 30, y_arrow - 35), font_size=11, fill=COLORS['text_light'])
    builder.text("x - a = -d", Point(x_a - d*scale/2 - 30, y_arrow - 50), font_size=12, fill=COLORS['text'], font_weight='bold')

    builder.label("x = a + d", Point(x_right, y_axis + 45), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    builder.label("x = a - d", Point(x_left, y_axis + 45), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])

    builder.formula_box("|x - a| = d", Point(300, 30))

    builder.save(OUTPUT_DIR / 'absolute_value_shifted.svg')

def create_absolute_value_anatomy():
    """Generates an anatomy breakdown of the equation |x - 2| = 3"""
    builder = SVGBuilder(600, 300)
    builder.rect(0, 0, 600, 300, fill=COLORS['background'])
    
    eqn_y = 50
    f_size = 36
    center_eqn_x = 300
    
    x_abs_open = center_eqn_x - 100
    x_var = center_eqn_x - 70
    x_minus = center_eqn_x - 40
    x_two = center_eqn_x - 10
    x_abs_close = center_eqn_x + 20
    x_equals = center_eqn_x + 50
    x_three = center_eqn_x + 80
    
    builder.text("|", Point(x_abs_open, eqn_y), font_size=f_size, fill=COLORS['text_light'])
    builder.text("x", Point(x_var, eqn_y), font_size=f_size, fill=COLORS['text'])
    builder.text("-", Point(x_minus, eqn_y), font_size=f_size, fill=COLORS['text'])
    builder.text("2", Point(x_two, eqn_y), font_size=f_size, fill=COLORS['secondary'], font_weight='bold')
    builder.text("|", Point(x_abs_close, eqn_y), font_size=f_size, fill=COLORS['text_light'])
    builder.text("=", Point(x_equals, eqn_y), font_size=f_size, fill=COLORS['text_light'])
    builder.text("3", Point(x_three, eqn_y), font_size=f_size, fill=COLORS['primary'], font_weight='bold')
    
    builder.text("Centro", Point(x_two, eqn_y - 30), font_size=14, fill=COLORS['secondary'])
    builder.text("Distancia", Point(x_three, eqn_y - 30), font_size=14, fill=COLORS['primary'])
    
    line_y = 200
    scale = 35
    center_val = 2
    dist_val = 3
    visual_center_x = 300
    
    def get_x(val):
        return (val - center_val) * scale + visual_center_x
        
    builder.line(Point(20, line_y), Point(580, line_y), stroke=COLORS['axis'], stroke_width=2, marker_end='arrow')
    
    for i in range(-2, 7):
        vx = get_x(i)
        h = 5
        builder.line(Point(vx, line_y - h), Point(vx, line_y + h), stroke=COLORS['axis'], stroke_width=1)
        col = COLORS['text_light']
        if i == center_val: col = COLORS['secondary']
        builder.text(str(i), Point(vx, line_y + 25), font_size=12, fill=col, font_weight='bold' if i==center_val else 'normal')

    p_start_2 = Point(x_two, eqn_y + 15)
    p_end_2 = Point(get_x(center_val), line_y - 20)
    builder.arrow(p_start_2, p_end_2, stroke=COLORS['secondary'], stroke_width=2, dashed=True)
    
    t_right = get_x(center_val + dist_val/2)
    t_left = get_x(center_val - dist_val/2)
    
    builder.path(f"M {get_x(center_val)} {line_y} Q {t_right} {line_y - 60} {get_x(center_val + dist_val)} {line_y}", 
                 stroke=COLORS['primary'], fill="none", stroke_width=2)
    builder.path(f"M {get_x(center_val)} {line_y} Q {t_left} {line_y - 60} {get_x(center_val - dist_val)} {line_y}", 
                 stroke=COLORS['primary'], fill="none", stroke_width=2)

    builder.text("3 pasos", Point(t_right, line_y - 40), font_size=12, fill=COLORS['primary'])
    builder.text("3 pasos", Point(t_left, line_y - 40), font_size=12, fill=COLORS['primary'])

    builder.point(Point(get_x(5), line_y), radius=6, fill=COLORS['success'])
    builder.point(Point(get_x(-1), line_y), radius=6, fill=COLORS['success'])
    
    builder.label("x = 5", Point(get_x(5), line_y + 50), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    builder.label("x = -1", Point(get_x(-1), line_y + 50), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])

    builder.save(OUTPUT_DIR / 'absolute_value_anatomy.svg')


# === EXAMPLE ILLUSTRATIONS ===

def create_example_1_basic_7():
    """Example 1: |x| = 7"""
    builder = SVGBuilder(600, 180)
    builder.rect(0, 0, 600, 180, fill=COLORS['background'])
    
    y = 90
    cx = 300
    scale = 30
    
    builder.line(Point(20, y), Point(580, y), stroke=COLORS['axis'], stroke_width=2, marker_end='arrow')
    
    for i in range(-9, 10):
        if i % 2 != 0 and abs(i) != 7: continue # Skip some ticks for space
        px = cx + i * scale
        if 20 <= px <= 580:
            builder.line(Point(px, y-5), Point(px, y+5), stroke=COLORS['axis'])
            col = COLORS['text_light']
            if i == 0: col = COLORS['secondary']
            builder.text(str(i), Point(px, y+25), font_size=11, fill=col)

    # Solutions
    builder.point(Point(cx + 7*scale, y), radius=6, fill=COLORS['success'])
    builder.point(Point(cx - 7*scale, y), radius=6, fill=COLORS['success'])
    
    builder.label("x = 7", Point(cx + 7*scale, y-25), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    builder.label("x = -7", Point(cx - 7*scale, y-25), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    
    # Distance arcs
    builder.path(f"M {cx} {y} Q {cx + 3.5*scale} {y - 40} {cx + 7*scale} {y}", stroke=COLORS['primary'], fill="none")
    builder.path(f"M {cx} {y} Q {cx - 3.5*scale} {y - 40} {cx - 7*scale} {y}", stroke=COLORS['primary'], fill="none")
    
    builder.text("|7|", Point(cx + 3.5*scale, y-50), font_size=12, fill=COLORS['primary'])
    builder.text("|-7|", Point(cx - 3.5*scale, y-50), font_size=12, fill=COLORS['primary'])
    
    builder.save(OUTPUT_DIR / 'ex_basic_7.svg')

def create_example_2_shifted():
    """Example 2: |x - 5| = 2"""
    builder = SVGBuilder(600, 180)
    builder.rect(0, 0, 600, 180, fill=COLORS['background'])
    
    y = 90
    cx = 300
    scale = 35
    center_val = 5
    dist = 2
    
    builder.line(Point(20, y), Point(580, y), stroke=COLORS['axis'], stroke_width=2, marker_end='arrow')
    
    def get_x(val):
        return cx + (val - center_val) * scale
        
    for i in range(1, 10):
        px = get_x(i)
        builder.line(Point(px, y-5), Point(px, y+5), stroke=COLORS['axis'])
        col = COLORS['text_light']
        if i == center_val: col = COLORS['secondary']
        builder.text(str(i), Point(px, y+25), font_size=11, fill=col, font_weight='bold' if i == center_val else 'normal')

    # Center label
    builder.text("Centro", Point(get_x(center_val), y+45), font_size=11, fill=COLORS['secondary'])

    # Solutions: 3 and 7
    s1, s2 = 3, 7
    builder.point(Point(get_x(s1), y), radius=6, fill=COLORS['success'])
    builder.point(Point(get_x(s2), y), radius=6, fill=COLORS['success'])
    
    builder.label("x = 3", Point(get_x(s1), y-30), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    builder.label("x = 7", Point(get_x(s2), y-30), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    
    # Arcs
    builder.path(f"M {get_x(center_val)} {y} Q {get_x(center_val+1)} {y - 40} {get_x(s2)} {y}", stroke=COLORS['primary'], fill="none")
    builder.path(f"M {get_x(center_val)} {y} Q {get_x(center_val-1)} {y - 40} {get_x(s1)} {y}", stroke=COLORS['primary'], fill="none")
    
    builder.text("2 pasos", Point(get_x(6), y-45), font_size=11, fill=COLORS['primary'])
    builder.text("2 pasos", Point(get_x(4), y-45), font_size=11, fill=COLORS['primary'])
    
    builder.save(OUTPUT_DIR / 'ex_shifted_5_2.svg')

def create_example_3_coeff():
    """Example 3: |2x + 1| = 9 -> Sol: 4, -5"""
    builder = SVGBuilder(600, 150)
    builder.rect(0, 0, 600, 150, fill=COLORS['background'])
    
    y = 75
    cx = 300
    scale = 25
    center_visual = 0 # Center visual at 0 just for scale
    
    builder.line(Point(20, y), Point(580, y), stroke=COLORS['axis'], stroke_width=2, marker_end='arrow')
    
    # Show approx range -7 to 7
    for i in range(-7, 8):
        px = cx + i * scale
        builder.line(Point(px, y-5), Point(px, y+5), stroke=COLORS['axis'])
        if i % 1 == 0:
            builder.text(str(i), Point(px, y+25), font_size=11, fill=COLORS['text_light'])

    # Solutions: 4 and -5
    s1, s2 = 4, -5
    builder.point(Point(cx + s1*scale, y), radius=6, fill=COLORS['success'])
    builder.point(Point(cx + s2*scale, y), radius=6, fill=COLORS['success'])
    
    builder.label("x = 4", Point(cx + s1*scale, y-25), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    builder.label("x = -5", Point(cx + s2*scale, y-25), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    
    builder.save(OUTPUT_DIR / 'ex_coeff_2x.svg')

def create_example_4_impossible():
    """Example 4: |x + 3| = -4"""
    builder = SVGBuilder(600, 200)
    builder.rect(0, 0, 600, 200, fill=COLORS['background'])
    
    y = 100
    cx = 300
    scale = 35
    center_val = -3
    
    def get_x(val):
        return cx + (val - center_val) * scale

    builder.line(Point(20, y), Point(580, y), stroke=COLORS['axis'], stroke_width=2, marker_end='arrow')
    
    # Range centered on -3
    for i in range(-7, 2):
        px = get_x(i)
        if 20 <= px <= 580:
            builder.line(Point(px, y-5), Point(px, y+5), stroke=COLORS['axis'])
            col = COLORS['text_light']
            if i == center_val: col = COLORS['secondary']
            builder.text(str(i), Point(px, y+25), font_size=11, fill=col, font_weight='bold' if i==center_val else 'normal')

    # Visualizing the error
    center_pt = Point(get_x(center_val), y)
    builder.text("Centro: -3", Point(center_pt.x, y+45), font_size=12, fill=COLORS['secondary'])
    
    # Ghost arrows trying to go nowhere? 
    # Better: A "Stop" sign metaphor or a red cross.
    
    # Draw a "Distance" bar that is broken or red
    # Let's draw a red line below indicating "Distance -4?" and a big Cross
    
    builder.line(Point(center_pt.x, y - 40), Point(center_pt.x + 100, y - 40), stroke=COLORS['danger'], stroke_width=2, dashed=True)
    builder.text("¿Distancia = -4?", Point(center_pt.x + 50, y - 55), font_size=12, fill=COLORS['danger'])
    
    # X MARK
    cross_pos = Point(center_pt.x + 50, y - 40)
    builder.line(Point(cross_pos.x - 10, cross_pos.y - 10), Point(cross_pos.x + 10, cross_pos.y + 10), stroke=COLORS['danger'], stroke_width=4)
    builder.line(Point(cross_pos.x - 10, cross_pos.y + 10), Point(cross_pos.x + 10, cross_pos.y - 10), stroke=COLORS['danger'], stroke_width=4)
    
    builder.label("IMPOSIBLE", Point(center_pt.x + 50, y - 10), bg_color=COLORS['fill_red_light'], fill=COLORS['danger'])
    builder.text("La distancia nunca es negativa", Point(center_pt.x + 50, y + 80), font_size=14, fill=COLORS['text'], font_weight='bold')

    builder.save(OUTPUT_DIR / 'ex_impossible.svg')

def create_example_5_clearance():
    """Example 5: reduces to |x - 2| = 4"""
    builder = SVGBuilder(600, 180)
    builder.rect(0, 0, 600, 180, fill=COLORS['background'])
    
    y = 90
    cx = 300
    scale = 30
    center_val = 2
    
    def get_x(val):
        return cx + (val - center_val) * scale

    builder.line(Point(20, y), Point(580, y), stroke=COLORS['axis'], stroke_width=2, marker_end='arrow')
    
    for i in range(-4, 9):
        px = get_x(i)
        if 20 <= px <= 580:
            builder.line(Point(px, y-5), Point(px, y+5), stroke=COLORS['axis'])
            col = COLORS['text_light']
            if i == center_val: col = COLORS['secondary']
            builder.text(str(i), Point(px, y+25), font_size=11, fill=col, font_weight='bold' if i == center_val else 'normal')

    # Solutions: 6 and -2
    s1, s2 = 6, -2
    builder.point(Point(get_x(s1), y), radius=6, fill=COLORS['success'])
    builder.point(Point(get_x(s2), y), radius=6, fill=COLORS['success'])
    
    builder.label("x = 6", Point(get_x(s1), y-30), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    builder.label("x = -2", Point(get_x(s2), y-30), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    
    # Arcs
    builder.path(f"M {get_x(center_val)} {y} Q {get_x(center_val+2)} {y - 40} {get_x(s1)} {y}", stroke=COLORS['primary'], fill="none")
    builder.path(f"M {get_x(center_val)} {y} Q {get_x(center_val-2)} {y - 40} {get_x(s2)} {y}", stroke=COLORS['primary'], fill="none")
    
    builder.text("4", Point(get_x(4), y-40), font_size=12, fill=COLORS['primary'])
    builder.text("4", Point(get_x(0), y-40), font_size=12, fill=COLORS['primary'])
    
    builder.formula_box("|x - 2| = 4", Point(300, 30))

    builder.save(OUTPUT_DIR / 'ex_clearance.svg')

def create_example_6_double():
    """Example 6: -4 and 2/3"""
    builder = SVGBuilder(600, 150)
    builder.rect(0, 0, 600, 150, fill=COLORS['background'])
    
    y = 75
    cx = 350 # Shift to right as -4 is far left
    scale = 35
    
    builder.line(Point(20, y), Point(580, y), stroke=COLORS['axis'], stroke_width=2, marker_end='arrow')
    
    for i in range(-5, 4):
        px = cx + i * scale
        builder.line(Point(px, y-5), Point(px, y+5), stroke=COLORS['axis'])
        builder.text(str(i), Point(px, y+25), font_size=11, fill=COLORS['text_light'])

    # Solutions: -4 and 2/3 (0.66)
    s1 = -4
    s2 = 0.66
    
    p1 = Point(cx + s1*scale, y)
    p2 = Point(cx + s2*scale, y)
    
    builder.point(p1, radius=6, fill=COLORS['success'])
    builder.point(p2, radius=6, fill=COLORS['success'])
    
    builder.label("x = -4", Point(p1.x, y-25), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    builder.label("x = 2/3", Point(p2.x, y-25), bg_color=COLORS['fill_green_light'], fill=COLORS['success'])
    
    builder.save(OUTPUT_DIR / 'ex_double.svg')

if __name__ == "__main__":
    create_basic_absolute_value()
    create_shifted_absolute_value()
    create_absolute_value_anatomy()
    create_example_1_basic_7()
    create_example_2_shifted()
    create_example_3_coeff()
    create_example_4_impossible()
    create_example_5_clearance()
    create_example_6_double()
