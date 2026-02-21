#!/usr/bin/env python3
"""
CARBON ISOTOPES COMPARISON RENDERER
Genera ilustración comparativa de los TRES isótopos de carbono en una sola imagen.
CORREGIDO: Más espacio, símbolos destacados, neutrones mezclados en el núcleo.
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))
sys.path.insert(0, str(Path(__file__).parent))

from core import COLORS


def pack_nucleus_centered(protons: int, neutrons: int, particle_radius: float) -> list:
    """
    Empaqueta nucleones asegurando que los neutrones estén MEZCLADOS con protones.
    """
    particles = []

    # Crear pool alternando p y n desde el inicio
    pool = []
    p_count, n_count = protons, neutrons
    i = 0
    while p_count > 0 or n_count > 0:
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

    # Phyllotaxis layout
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


def render_carbon_three_isotopes(output: Path):
    width = 1500
    height = 620

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
        f'<text x="{width / 2}" y="42" font-family="Inter, sans-serif" font-size="30" font-weight="900" fill="{colors["text"]}" text-anchor="middle">Isótopos del Carbono</text>'
    )
    svg_parts.append(
        f'<text x="{width / 2}" y="68" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{colors["text_light"]}" text-anchor="middle">Mismo número de protones (Z=6), diferente número de neutrones</text>'
    )

    # Tres posiciones - ESPACIADAS
    positions = [
        {
            "x": 250,
            "name": "Carbono-12",
            "symbol": "¹²C",
            "mass": "12 uma",
            "protons": 6,
            "neutrons": 6,
            "extra": 0,
            "abundance": "98.9%",
            "desc": "Estable",
        },
        {
            "x": 750,
            "name": "Carbono-13",
            "symbol": "¹³C",
            "mass": "13 uma",
            "protons": 6,
            "neutrons": 7,
            "extra": 1,
            "abundance": "1.1%",
            "desc": "Estable",
        },
        {
            "x": 1250,
            "name": "Carbono-14",
            "symbol": "¹⁴C",
            "mass": "14 uma",
            "protons": 6,
            "neutrons": 8,
            "extra": 2,
            "abundance": "Trazas",
            "desc": "Radiactivo",
        },
    ]

    cy = 290

    for pos in positions:
        draw_carbon_atom(
            svg_parts,
            cx=pos["x"],
            cy=cy,
            protons=pos["protons"],
            neutrons=pos["neutrons"],
            name=pos["name"],
            symbol=pos["symbol"],
            mass=pos["mass"],
            extra_neutrons=pos["extra"],
            abundance=pos["abundance"],
            desc=pos["desc"],
        )

    draw_legend(svg_parts, width, height - 28)

    svg_parts.append("</svg>")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(svg_parts), encoding="utf-8")
    print(f"✅ Comparación de 3 isótopos generada: {output}")


def draw_carbon_atom(
    svg_parts,
    cx,
    cy,
    protons,
    neutrons,
    name,
    symbol,
    mass,
    extra_neutrons,
    abundance,
    desc,
):
    colors = COLORS

    ORBIT_1_RADIUS = 105
    ORBIT_2_RADIUS = 140
    ELECTRON_RADIUS = 5
    NUCLEON_RADIUS = 9
    NUCLEUS_BG_RADIUS = 65

    # Título del isótopo
    svg_parts.append(
        f'<text x="{cx}" y="{cy - 185}" font-family="Inter, sans-serif" font-size="22" font-weight="bold" fill="{colors["text"]}" text-anchor="middle">{name}</text>'
    )

    # Símbolo DESTACADO - CAJA VISUAL
    box_w, box_h = 70, 32
    svg_parts.append(
        f'<rect x="{cx - box_w / 2}" y="{cy - 172}" width="{box_w}" height="{box_h}" rx="8" fill="#f5f3ff" stroke="{colors["purple"]}" stroke-width="2"/>'
    )
    svg_parts.append(
        f'<text x="{cx}" y="{cy - 150}" font-family="Inter, sans-serif" font-size="20" font-weight="900" fill="{colors["purple"]}" text-anchor="middle">{symbol}</text>'
    )

    # Órbitas
    svg_parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{ORBIT_1_RADIUS}" fill="none" stroke="#e2e8f0" stroke-width="2" opacity="0.8"/>'
    )
    svg_parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{ORBIT_2_RADIUS}" fill="none" stroke="#e2e8f0" stroke-width="2" opacity="0.8"/>'
    )

    # Electrones (6) - PEQUEÑOS con "-"
    # Capa 1: 2 electrones
    svg_parts.append(
        f'<circle cx="{cx}" cy="{cy - ORBIT_1_RADIUS}" r="{ELECTRON_RADIUS}" fill="{colors["primary"]}" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{cx}" y="{cy - ORBIT_1_RADIUS + 2}" font-family="Inter, sans-serif" font-size="7" font-weight="bold" fill="white" text-anchor="middle">-</text>'
    )
    svg_parts.append(
        f'<circle cx="{cx}" cy="{cy + ORBIT_1_RADIUS}" r="{ELECTRON_RADIUS}" fill="{colors["primary"]}" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{cx}" y="{cy + ORBIT_1_RADIUS + 2}" font-family="Inter, sans-serif" font-size="7" font-weight="bold" fill="white" text-anchor="middle">-</text>'
    )

    # Capa 2: 4 electrones
    for angle in [45, 135, 225, 315]:
        rad = angle * (math.pi / 180)
        ex = cx + ORBIT_2_RADIUS * math.cos(rad)
        ey = cy + ORBIT_2_RADIUS * math.sin(rad)
        svg_parts.append(
            f'<circle cx="{ex}" cy="{ey}" r="{ELECTRON_RADIUS}" fill="{colors["primary"]}" stroke="white" stroke-width="1"/>'
        )
        svg_parts.append(
            f'<text x="{ex}" y="{ey + 2}" font-family="Inter, sans-serif" font-size="7" font-weight="bold" fill="white" text-anchor="middle">-</text>'
        )

    # Núcleo - FONDO DESTACADO
    nucleus_radius = NUCLEUS_BG_RADIUS if neutrons <= 7 else 70
    svg_parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{nucleus_radius}" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" opacity="0.95"/>'
    )

    # Nucleones MEZCLADOS
    nucleons = pack_nucleus_centered(protons, neutrons, NUCLEON_RADIUS)

    # Identificar neutrones extra (los últimos n)
    neutron_indices = [i for i, p in enumerate(nucleons) if p["type"] == "n"]
    extra_neutron_indices = set()
    if extra_neutrons > 0 and len(neutron_indices) >= extra_neutrons:
        extra_neutron_indices = set(neutron_indices[-extra_neutrons:])

    svg_parts.append(f'<g transform="translate({cx},{cy})">')
    for i, p in enumerate(nucleons):
        r = NUCLEON_RADIUS
        if p["type"] == "p":
            fill = colors["accent"]
            label = "+"
        else:
            is_extra = i in extra_neutron_indices
            fill = colors["highlight"] if is_extra else "#64748b"
            label = ""

        svg_parts.append(
            f'<circle cx="{p["x"]}" cy="{p["y"]}" r="{r}" fill="{fill}" stroke="white" stroke-width="1"/>'
        )
        if label:
            svg_parts.append(
                f'<text x="{p["x"]}" y="{p["y"] + 3}" font-family="Inter, sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">{label}</text>'
            )
    svg_parts.append("</g>")

    # Tarjeta informativa
    box_width = 145
    box_height = 105
    box_y = cy + 180

    svg_parts.append(
        f'<rect x="{cx - box_width / 2}" y="{box_y}" width="{box_width}" height="{box_height}" rx="8" fill="white" stroke="{colors["grid"]}" stroke-width="1.5"/>'
    )

    # Masa
    svg_parts.append(
        f'<text x="{cx}" y="{box_y + 25}" font-family="Inter, sans-serif" font-size="20" font-weight="900" fill="{colors["text"]}" text-anchor="middle">{mass}</text>'
    )

    # Protones
    svg_parts.append(
        f'<circle cx="{cx - 58}" cy="{box_y + 50}" r="6" fill="{colors["accent"]}" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{cx - 58}" y="{box_y + 52}" font-family="Inter, sans-serif" font-size="8" font-weight="bold" fill="white" text-anchor="middle">+</text>'
    )
    svg_parts.append(
        f'<text x="{cx - 45}" y="{box_y + 53}" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="{colors["accent"]}" text-anchor="start">6 protones</text>'
    )

    # Neutrones
    neutron_color = colors["highlight"] if extra_neutrons > 0 else "#64748b"
    svg_parts.append(
        f'<circle cx="{cx - 58}" cy="{box_y + 72}" r="6" fill="{neutron_color}" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{cx - 45}" y="{box_y + 75}" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="{colors["text_light"]}" text-anchor="start">{neutrons} neutrones</text>'
    )

    # Abundancia y estado
    svg_parts.append(
        f'<text x="{cx}" y="{box_y + 95}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{colors["secondary"]}" text-anchor="middle">{abundance} • {desc}</text>'
    )


def draw_legend(svg_parts, width, y):
    colors = COLORS

    svg_parts.append(
        f'<rect x="{width / 2 - 340}" y="{y - 18}" width="680" height="26" rx="4" fill="white" stroke="{colors["grid"]}" stroke-width="1" opacity="0.95"/>'
    )

    # Protón
    svg_parts.append(
        f'<circle cx="{width / 2 - 280}" cy="{y - 5}" r="7" fill="{colors["accent"]}" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{width / 2 - 280}" y="{y - 2}" font-family="Inter, sans-serif" font-size="9" font-weight="bold" fill="white" text-anchor="middle">+</text>'
    )
    svg_parts.append(
        f'<text x="{width / 2 - 265}" y="{y - 1}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{colors["text"]}" text-anchor="start">Protón (p⁺)</text>'
    )

    # Neutrón normal
    svg_parts.append(
        f'<circle cx="{width / 2 - 140}" cy="{y - 5}" r="7" fill="#64748b" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{width / 2 - 125}" y="{y - 1}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{colors["text"]}" text-anchor="start">Neutrón (n⁰)</text>'
    )

    # Neutrón extra
    svg_parts.append(
        f'<circle cx="{width / 2 + 10}" cy="{y - 5}" r="7" fill="{colors["highlight"]}" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{width / 2 + 25}" y="{y - 1}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{colors["text"]}" text-anchor="start">Neutrón extra</text>'
    )

    # Electrón
    svg_parts.append(
        f'<circle cx="{width / 2 + 160}" cy="{y - 5}" r="5" fill="{colors["primary"]}" stroke="white" stroke-width="1"/>'
    )
    svg_parts.append(
        f'<text x="{width / 2 + 160}" y="{y - 3}" font-family="Inter, sans-serif" font-size="7" font-weight="bold" fill="white" text-anchor="middle">-</text>'
    )
    svg_parts.append(
        f'<text x="{width / 2 + 175}" y="{y - 1}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{colors["text"]}" text-anchor="start">Electrón (e⁻)</text>'
    )


if __name__ == "__main__":
    render_carbon_three_isotopes(
        Path("public/images/quimica/isotopos/carbono-tres-isotopos.svg")
    )
