#!/usr/bin/env python3
"""
HYDROGEN ISOTOPES RENDERER
Genera ilustración comparativa de los tres isótopos de hidrógeno en una imagen.
CORREGIDO: Neutrones DENTRO del núcleo, mezclados con protones.
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))
sys.path.insert(0, str(Path(__file__).parent))

from core import COLORS


def pack_nucleus_centered(protons: int, neutrons: int, particle_radius: float) -> list:
    """
    Empaqueta nucleones asegurando que los neutrones estén MEZCLADOS con protones,
    no en la periferia del núcleo.
    """
    particles = []
    total = protons + neutrons

    # Crear pool alternando p y n desde el inicio
    pool = []
    p_count, n_count = protons, neutrons
    i = 0
    while p_count > 0 or n_count > 0:
        # Alternar: empezar con protón, luego neutrón, etc.
        if i % 2 == 0 and p_count > 0:
            pool.append("p")
            p_count -= 1
        elif n_count > 0:
            pool.append("n")
            n_count -= 1
        elif p_count > 0:
            pool.append("p")
            p_count -= 1
        i += 1

    # Phyllotaxis layout (espiral dorada)
    c = particle_radius * 2.0
    golden_angle = 137.508 * (math.pi / 180)

    for i, p_type in enumerate(pool):
        if i == 0:
            x, y = 0, 0
        else:
            r = c * math.sqrt(i)
            theta = i * golden_angle
            x = r * math.cos(theta)
            y = r * math.sin(theta)

        particles.append({"type": p_type, "x": x, "y": y})

    return particles


def render_hydrogen_comparison(output: Path):
    width = 950
    height = 480

    colors = COLORS

    svg_parts = []
    svg_parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">'
    )
    svg_parts.append(
        f'<rect width="{width}" height="{height}" fill="{colors["background"]}" rx="12"/>'
    )

    # Título Principal
    svg_parts.append(
        f'<text x="{width / 2}" y="38" font-family="Inter, sans-serif" font-size="26" font-weight="900" fill="{colors["text"]}" text-anchor="middle">Isótopos del Hidrógeno</text>'
    )
    svg_parts.append(
        f'<text x="{width / 2}" y="60" font-family="Inter, sans-serif" font-size="13" font-weight="bold" fill="{colors["text_light"]}" text-anchor="middle">Mismo número de protones (Z=1), diferente número de neutrones</text>'
    )

    cy = 240

    # Protio
    draw_atom(
        svg_parts,
        160,
        cy,
        protons=1,
        neutrons=0,
        name="Protio",
        mass="1 uma",
        symbol="¹H",
        highlight_neutrons=0,
        desc="99.98%",
    )

    # Deuterio
    draw_atom(
        svg_parts,
        475,
        cy,
        protons=1,
        neutrons=1,
        name="Deuterio",
        mass="2 uma",
        symbol="²H",
        highlight_neutrons=1,
        desc="0.015%",
    )

    # Tritio
    draw_atom(
        svg_parts,
        790,
        cy,
        protons=1,
        neutrons=2,
        name="Tritio",
        mass="3 uma",
        symbol="³H",
        highlight_neutrons=2,
        desc="Radiactivo",
    )

    # Leyenda inferior
    draw_legend(svg_parts, width, height - 25)

    svg_parts.append("</svg>")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(svg_parts), encoding="utf-8")
    print(f"✅ Comparación de hidrógeno generada: {output}")


def draw_atom(
    svg_parts, cx, cy, protons, neutrons, name, mass, symbol, highlight_neutrons, desc
):
    colors = COLORS

    # Título del isótopo - MÁS GRANDE
    svg_parts.append(
        f'<text x="{cx}" y="{cy - 115}" font-family="Inter, sans-serif" font-size="20" font-weight="bold" fill="{colors["text"]}" text-anchor="middle">{name}</text>'
    )
    svg_parts.append(
        f'<text x="{cx}" y="{cy - 90}" font-family="Inter, sans-serif" font-size="18" font-weight="900" fill="{colors["purple"]}" text-anchor="middle">{symbol}</text>'
    )

    # Órbita
    radius = 75
    svg_parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="#e2e8f0" stroke-width="2" opacity="0.8"/>'
    )

    # Electrón (1) - PEQUEÑO
    angle_rad = -math.pi / 4
    e_x = cx + radius * math.cos(angle_rad)
    e_y = cy + radius * math.sin(angle_rad)
    svg_parts.append(
        f'<circle cx="{e_x}" cy="{e_y}" r="5" fill="{colors["primary"]}" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{e_x}" y="{e_y + 2}" font-family="Inter, sans-serif" font-size="7" font-weight="bold" fill="white" text-anchor="middle">-</text>'
    )

    # Núcleo con nucleones MEZCLADOS
    nucleons = pack_nucleus_centered(protons, neutrons, particle_radius=11)

    # Radio del fondo del núcleo
    if neutrons == 0:
        nucleus_bg_radius = 20
    elif neutrons == 1:
        nucleus_bg_radius = 26
    else:
        nucleus_bg_radius = 32

    # Fondo del núcleo
    svg_parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{nucleus_bg_radius}" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" opacity="0.9"/>'
    )

    # Dibujar nucleones
    svg_parts.append(f'<g transform="translate({cx},{cy})">')

    for i, p in enumerate(nucleons):
        r = 11
        if p["type"] == "p":
            fill = colors["accent"]
            label = "+"
        else:
            fill = colors["highlight"] if highlight_neutrons > 0 else "#64748b"
            label = ""

        svg_parts.append(
            f'<circle cx="{p["x"]}" cy="{p["y"]}" r="{r}" fill="{fill}" stroke="white" stroke-width="1.5"/>'
        )
        if label:
            svg_parts.append(
                f'<text x="{p["x"]}" y="{p["y"] + 4}" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="white" text-anchor="middle">{label}</text>'
            )

    svg_parts.append("</g>")

    # Tarjeta informativa
    box_width = 130
    box_height = 80
    box_y = cy + 95

    svg_parts.append(
        f'<rect x="{cx - box_width / 2}" y="{box_y}" width="{box_width}" height="{box_height}" rx="8" fill="white" stroke="{colors["grid"]}" stroke-width="1.5"/>'
    )
    svg_parts.append(
        f'<text x="{cx}" y="{box_y + 22}" font-family="Inter, sans-serif" font-size="18" font-weight="900" fill="{colors["text"]}" text-anchor="middle">{mass}</text>'
    )
    svg_parts.append(
        f'<text x="{cx}" y="{box_y + 45}" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="{colors["accent"]}" text-anchor="middle">1 Protón</text>'
    )
    svg_parts.append(
        f'<text x="{cx}" y="{box_y + 65}" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="{colors["text_light"]}" text-anchor="middle">{neutrons} Neutrón{"es" if neutrons != 1 else ""}</text>'
    )

    # Descripción (abundancia/estado)
    color_desc = colors["secondary"] if desc != "Radiactivo" else colors["highlight"]
    svg_parts.append(
        f'<text x="{cx}" y="{box_y + 78}" font-family="Inter, sans-serif" font-size="10" font-weight="bold" fill="{color_desc}" text-anchor="middle">{desc}</text>'
    )


def draw_legend(svg_parts, width, y):
    colors = COLORS

    svg_parts.append(
        f'<rect x="{width / 2 - 280}" y="{y - 15}" width="560" height="22" rx="4" fill="white" stroke="{colors["grid"]}" stroke-width="1" opacity="0.95"/>'
    )

    # Protón
    svg_parts.append(
        f'<circle cx="{width / 2 - 220}" cy="{y - 4}" r="6" fill="{colors["accent"]}" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{width / 2 - 220}" y="{y - 1}" font-family="Inter, sans-serif" font-size="8" font-weight="bold" fill="white" text-anchor="middle">+</text>'
    )
    svg_parts.append(
        f'<text x="{width / 2 - 205}" y="{y}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{colors["text"]}" text-anchor="start">Protón</text>'
    )

    # Neutrón
    svg_parts.append(
        f'<circle cx="{width / 2 - 110}" cy="{y - 4}" r="6" fill="#64748b" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{width / 2 - 95}" y="{y}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{colors["text"]}" text-anchor="start">Neutrón</text>'
    )

    # Electrón
    svg_parts.append(
        f'<circle cx="{width / 2 + 10}" cy="{y - 4}" r="5" fill="{colors["primary"]}" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{width / 2 + 10}" y="{y - 2}" font-family="Inter, sans-serif" font-size="7" font-weight="bold" fill="white" text-anchor="middle">-</text>'
    )
    svg_parts.append(
        f'<text x="{width / 2 + 25}" y="{y}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{colors["text"]}" text-anchor="start">Electrón</text>'
    )

    # Neutrón extra
    svg_parts.append(
        f'<circle cx="{width / 2 + 120}" cy="{y - 4}" r="6" fill="{colors["highlight"]}" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{width / 2 + 135}" y="{y}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{colors["text"]}" text-anchor="start">Neutrón extra</text>'
    )


if __name__ == "__main__":
    render_hydrogen_comparison(
        Path("public/images/quimica/isotopos/hidrogeno-comparacion.svg")
    )
