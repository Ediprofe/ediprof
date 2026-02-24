#!/usr/bin/env python3
"""
PERIODOS Y NIVELES RENDERER - UN ÁTOMO POR IMAGEN
SVGs separados para mayor claridad didáctica.
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS


def draw_atom_clean(
    svg,
    cx,
    cy,
    shells,
    symbol,
    electron_radius=5,
    base_radius=60,
    step=35,
    nucleus_radius=20,
    electron_color=None,
):
    """Dibuja átomo limpio con núcleo y capas."""
    if electron_color is None:
        electron_color = COLORS["primary"]

    # Núcleo
    svg.append(
        f'<circle cx="{cx}" cy="{cy}" r="{nucleus_radius}" fill="#8b5cf6" stroke="white" stroke-width="2"/>'
    )
    svg.append(
        f'<text x="{cx}" y="{cy + 5}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="white" text-anchor="middle">{symbol}</text>'
    )

    # Órbitas y electrones
    for i, e_count in enumerate(shells):
        r = base_radius + i * step
        svg.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#e2e8f0" stroke-width="1.5" opacity="0.9"/>'
        )

        if e_count > 0:
            angle_step = (2 * math.pi) / e_count
            start_angle = -math.pi / 2
            for e in range(e_count):
                theta = start_angle + e * angle_step
                ex = cx + r * math.cos(theta)
                ey = cy + r * math.sin(theta)
                svg.append(
                    f'<circle cx="{ex}" cy="{ey}" r="{electron_radius}" fill="{electron_color}" stroke="white" stroke-width="1"/>'
                )
                svg.append(
                    f'<text x="{ex}" y="{ey + 2}" font-family="Inter, sans-serif" font-size="6" font-weight="bold" fill="white" text-anchor="middle">-</text>'
                )


# ============================================
# 1. ELECTRONES EN CAPAS
# ============================================
def render_electrones_en_capas():
    svg = []
    width, height = 500, 380

    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">'
    )
    svg.append(
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>'
    )

    svg.append(
        f'<text x="{width / 2}" y="28" font-family="Inter, sans-serif" font-size="16" font-weight="900" fill="{COLORS["text"]}" text-anchor="middle">Electrones en Capas</text>'
    )
    svg.append(
        f'<text x="{width / 2}" y="45" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text_light"]}" text-anchor="middle">Se organizan en niveles alrededor del núcleo</text>'
    )

    cx, cy = 250, 190

    draw_atom_clean(
        svg,
        cx,
        cy,
        shells=[2, 4],
        symbol="C",
        electron_radius=6,
        base_radius=65,
        step=45,
        nucleus_radius=20,
    )

    # Leyenda abajo
    legend_y = 340
    svg.append(
        f'<rect x="80" y="{legend_y - 12}" width="340" height="28" rx="5" fill="white" stroke="{COLORS["grid"]}" stroke-width="1"/>'
    )
    svg.append(
        f'<circle cx="110" cy="{legend_y}" r="8" fill="#8b5cf6" stroke="white" stroke-width="1"/>'
    )
    svg.append(
        f'<text x="125" y="{legend_y + 3}" font-family="Inter, sans-serif" font-size="9" fill="{COLORS["text"]}">Núcleo</text>'
    )
    svg.append(
        f'<circle cx="195" cy="{legend_y}" r="4" fill="{COLORS["primary"]}" stroke="white" stroke-width="1"/>'
    )
    svg.append(
        f'<text x="208" y="{legend_y + 3}" font-family="Inter, sans-serif" font-size="9" fill="{COLORS["text"]}">Electrón</text>'
    )
    svg.append(
        f'<circle cx="290" cy="{legend_y}" r="7" fill="none" stroke="#e2e8f0" stroke-width="1"/>'
    )
    svg.append(
        f'<text x="305" y="{legend_y + 3}" font-family="Inter, sans-serif" font-size="9" fill="{COLORS["text"]}">Capa (2, 4 e⁻)</text>'
    )

    svg.append("</svg>")
    return "\n".join(svg)


# ============================================
# 2. ÁTOMOS INDIVIDUALES (4 SVGs separados)
# ============================================
def render_atomo_individual(symbol, name, period, shells):
    """Genera un SVG para un solo átomo."""
    svg = []
    width, height = 400, 350

    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">'
    )
    svg.append(
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>'
    )

    # Título
    svg.append(
        f'<text x="{width / 2}" y="28" font-family="Inter, sans-serif" font-size="16" font-weight="900" fill="{COLORS["text"]}" text-anchor="middle">{name} ({symbol})</text>'
    )
    svg.append(
        f'<text x="{width / 2}" y="45" font-family="Inter, sans-serif" font-size="11" fill="{COLORS["primary"]}" text-anchor="middle">Período {period}</text>'
    )

    cx, cy = 200, 175

    # Escala según número de capas
    num_shells = len(shells)
    base = 50 if num_shells <= 2 else 40
    step = 35 if num_shells <= 2 else 28
    nucleus_r = 18 if num_shells <= 2 else 15

    draw_atom_clean(
        svg,
        cx,
        cy,
        shells=shells,
        symbol=symbol,
        electron_radius=5,
        base_radius=base,
        step=step,
        nucleus_radius=nucleus_r,
    )

    # Info abajo
    svg.append(
        f'<text x="{width / 2}" y="300" font-family="Inter, sans-serif" font-size="13" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{num_shells} {"capa" if num_shells == 1 else "capas"} de energía</text>'
    )
    svg.append(
        f'<text x="{width / 2}" y="320" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text_light"]}" text-anchor="middle">Configuración: {", ".join(map(str, shells))}</text>'
    )

    svg.append("</svg>")
    return "\n".join(svg)


# ============================================
# 3. COMPARACIONES (3 SVGs separados)
# ============================================
def render_comparacion(left, right):
    """Genera SVG de comparación entre dos átomos."""
    svg = []
    width, height = 600, 380

    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">'
    )
    svg.append(
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>'
    )

    # Título
    svg.append(
        f'<text x="{width / 2}" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="900" fill="{COLORS["text"]}" text-anchor="middle">Tamaño Atómico: {left["symbol"]} vs {right["symbol"]}</text>'
    )

    # Átomo izquierdo
    cx1 = 150
    cy1 = 175
    num_l = len(left["shells"])
    base_l = 40
    step_l = 25
    draw_atom_clean(
        svg,
        cx1,
        cy1,
        shells=left["shells"],
        symbol=left["symbol"],
        electron_radius=4,
        base_radius=base_l,
        step=step_l,
        nucleus_radius=14,
        electron_color=COLORS["primary"],
    )
    svg.append(
        f'<text x="{cx1}" y="335" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text_light"]}" text-anchor="middle">{left["name"]} — Período {left["period"]}</text>'
    )
    svg.append(
        f'<text x="{cx1}" y="350" font-family="Inter, sans-serif" font-size="9" fill="{COLORS["primary"]}" text-anchor="middle">{num_l} {"capa" if num_l == 1 else "capas"}</text>'
    )

    # Flecha
    svg.append(
        f'<text x="{width / 2}" y="180" font-family="Inter, sans-serif" font-size="20" font-weight="bold" fill="{COLORS["text_light"]}" text-anchor="middle">&lt;</text>'
    )

    # Átomo derecho
    cx2 = 450
    cy2 = 175
    num_r = len(right["shells"])
    base_r = 35 if num_r > 4 else 40
    step_r = 20 if num_r > 4 else 25
    draw_atom_clean(
        svg,
        cx2,
        cy2,
        shells=right["shells"],
        symbol=right["symbol"],
        electron_radius=4,
        base_radius=base_r,
        step=step_r,
        nucleus_radius=14,
        electron_color=COLORS["secondary"],
    )
    svg.append(
        f'<text x="{cx2}" y="335" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text_light"]}" text-anchor="middle">{right["name"]} — Período {right["period"]}</text>'
    )
    svg.append(
        f'<text x="{cx2}" y="350" font-family="Inter, sans-serif" font-size="9" fill="{COLORS["secondary"]}" text-anchor="middle">{num_r} capas</text>'
    )

    # Conclusión
    svg.append(
        f'<text x="{width / 2}" y="370" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{right["symbol"]} > {left["symbol"]} (más capas = más grande)</text>'
    )

    svg.append("</svg>")
    return "\n".join(svg)


# ============================================
# 4. POTASIO vs OXÍGENO (corregido)
# ============================================
def render_potasio_oxigeno():
    svg = []
    width, height = 900, 450

    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">'
    )
    svg.append(
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>'
    )

    # Título
    svg.append(
        f'<text x="{width / 2}" y="28" font-family="Inter, sans-serif" font-size="16" font-weight="900" fill="{COLORS["text"]}" text-anchor="middle">Comparación: Potasio (4 capas) vs Oxígeno (2 capas)</text>'
    )

    # ===== POTASIO (K) =====
    k_x, k_y = 220, 210

    svg.append(
        f'<rect x="35" y="45" width="370" height="380" rx="10" fill="white" stroke="{COLORS["primary"]}" stroke-width="2"/>'
    )
    svg.append(
        f'<rect x="35" y="45" width="370" height="32" rx="10" fill="{COLORS["primary"]}"/>'
    )
    svg.append(
        f'<rect x="35" y="69" width="370" height="8" fill="{COLORS["primary"]}"/>'
    )
    svg.append(
        f'<text x="{k_x}" y="68" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="white" text-anchor="middle">Potasio (K)</text>'
    )

    draw_atom_clean(
        svg,
        k_x,
        k_y,
        shells=[2, 8, 8, 1],
        symbol="K",
        electron_radius=4,
        base_radius=40,
        step=25,
        nucleus_radius=14,
    )

    svg.append(
        f'<text x="{k_x}" y="360" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">Período 4 → 4 capas</text>'
    )
    svg.append(
        f'<text x="{k_x}" y="385" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text_light"]}" text-anchor="middle">2, 8, 8, 1 = 19 e⁻ (Z=19)</text>'
    )

    # ===== OXÍGENO (O) =====
    o_x, o_y = 680, 210

    svg.append(
        f'<rect x="495" y="45" width="370" height="380" rx="10" fill="white" stroke="{COLORS["secondary"]}" stroke-width="2"/>'
    )
    svg.append(
        f'<rect x="495" y="45" width="370" height="32" rx="10" fill="{COLORS["secondary"]}"/>'
    )
    svg.append(
        f'<rect x="495" y="69" width="370" height="8" fill="{COLORS["secondary"]}"/>'
    )
    svg.append(
        f'<text x="{o_x}" y="68" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="white" text-anchor="middle">Oxígeno (O)</text>'
    )

    draw_atom_clean(
        svg,
        o_x,
        o_y,
        shells=[2, 6],
        symbol="O",
        electron_radius=5,
        base_radius=55,
        step=40,
        nucleus_radius=16,
    )

    svg.append(
        f'<text x="{o_x}" y="360" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">Período 2 → 2 capas</text>'
    )
    svg.append(
        f'<text x="{o_x}" y="385" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text_light"]}" text-anchor="middle">2, 6 = 8 e⁻ (Z=8)</text>'
    )

    # Flecha comparativa
    svg.append(
        f'<text x="{width / 2}" y="215" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{COLORS["text_light"]}" text-anchor="middle">vs</text>'
    )

    svg.append("</svg>")
    return "\n".join(svg)


def main():
    output_dir = Path("public/images/quimica/periodos-niveles")
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Electrones en capas
    (output_dir / "electrones-en-capas.svg").write_text(
        render_electrones_en_capas(), encoding="utf-8"
    )
    print("✅ electrones-en-capas.svg")

    # 2. Átomos individuales (4 archivos)
    atoms = [
        {"symbol": "H", "name": "Hidrógeno", "period": 1, "shells": [1]},
        {"symbol": "O", "name": "Oxígeno", "period": 2, "shells": [2, 6]},
        {"symbol": "Na", "name": "Sodio", "period": 3, "shells": [2, 8, 1]},
        {"symbol": "K", "name": "Potasio", "period": 4, "shells": [2, 8, 8, 1]},
    ]

    for atom in atoms:
        filename = f"{atom['symbol'].lower()}-periodo-{atom['period']}.svg"
        (output_dir / filename).write_text(
            render_atomo_individual(
                atom["symbol"], atom["name"], atom["period"], atom["shells"]
            ),
            encoding="utf-8",
        )
        print(f"✅ {filename}")

    # 3. Comparaciones (3 archivos)
    comparisons = [
        (
            {"symbol": "Li", "name": "Litio", "period": 2, "shells": [2, 1]},
            {
                "symbol": "Cs",
                "name": "Cesio",
                "period": 6,
                "shells": [2, 8, 18, 18, 8, 1],
            },
        ),
        (
            {"symbol": "O", "name": "Oxígeno", "period": 2, "shells": [2, 6]},
            {"symbol": "S", "name": "Azufre", "period": 3, "shells": [2, 8, 6]},
        ),
        (
            {"symbol": "Na", "name": "Sodio", "period": 3, "shells": [2, 8, 1]},
            {"symbol": "K", "name": "Potasio", "period": 4, "shells": [2, 8, 8, 1]},
        ),
    ]

    for left, right in comparisons:
        filename = f"tamano-{left['symbol'].lower()}-{right['symbol'].lower()}.svg"
        (output_dir / filename).write_text(
            render_comparacion(left, right), encoding="utf-8"
        )
        print(f"✅ {filename}")

    # 4. Potasio vs Oxígeno
    (output_dir / "potasio-oxigeno.svg").write_text(
        render_potasio_oxigeno(), encoding="utf-8"
    )
    print("✅ potasio-oxigeno.svg")


if __name__ == "__main__":
    main()
