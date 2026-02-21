#!/usr/bin/env python3
"""
GROUPS PERIODS COORDINATES RENDERER
Ilustra la localización de elementos usando grupos y períodos como coordenadas.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS


def load_spec(spec_path: str) -> dict:
    with open(spec_path, "r", encoding="utf-8") as f:
        return json.load(f)


def render_groups_periods(spec: dict) -> str:
    layout = spec["layout"]
    elements = spec["elements"]
    highlights = spec["highlight_elements"]

    cell_w = layout["cell_width"]
    cell_h = layout["cell_height"]
    gap = layout["gap"]
    padding = layout["padding"]

    # Dimensiones
    cols = 18
    rows = 4
    extra_right = 200  # Espacio para leyenda de coordenadas

    width = padding * 2 + cols * (cell_w + gap) - gap + extra_right
    height = padding * 2 + rows * (cell_h + gap) + 80  # Extra para título y leyenda

    svg = []
    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">'
    )
    svg.append(
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>'
    )

    # Título
    svg.append(
        f'<text x="{width / 2 - extra_right / 2}" y="25" font-family="Inter, sans-serif" font-size="16" font-weight="900" fill="{COLORS["text"]}" text-anchor="middle">{spec["title"]}</text>'
    )
    svg.append(
        f'<text x="{width / 2 - extra_right / 2}" y="42" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text_light"]}" text-anchor="middle">{spec["subtitle"]}</text>'
    )

    # Offset vertical
    title_offset = 50

    # === ETIQUETAS DE GRUPOS (1-18) ===
    for g in range(1, 19):
        x = padding + (g - 1) * (cell_w + gap) + cell_w / 2
        svg.append(
            f'<text x="{x}" y="{padding + title_offset - 8}" font-family="Inter, sans-serif" font-size="9" font-weight="bold" fill="{COLORS["primary"]}" text-anchor="middle">{g}</text>'
        )

    # Flecha indicando GRUPOS
    arrow_y = padding + title_offset - 22
    svg.append(
        f'<text x="{padding + 9 * (cell_w + gap)}" y="{arrow_y}" font-family="Inter, sans-serif" font-size="10" font-weight="bold" fill="{COLORS["primary"]}" text-anchor="middle">GRUPOS →</text>'
    )

    # === ETIQUETAS DE PERÍODOS (1-4) ===
    for p in range(1, 5):
        y = padding + title_offset + (p - 1) * (cell_h + gap) + cell_h / 2 + 3
        svg.append(
            f'<text x="{padding - 8}" y="{y}" font-family="Inter, sans-serif" font-size="9" font-weight="bold" fill="#8b5cf6" text-anchor="end">{p}</text>'
        )

    # Flecha indicando PERÍODOS
    svg.append(
        f'<text x="{padding - 30}" y="{padding + title_offset + 2 * (cell_h + gap) + cell_h / 2}" font-family="Inter, sans-serif" font-size="9" font-weight="bold" fill="#8b5cf6" text-anchor="middle" transform="rotate(-90 {padding - 30} {padding + title_offset + 2 * (cell_h + gap) + cell_h / 2})">PERÍODOS ↓</text>'
    )

    # === DIBUJAR TODOS LOS ELEMENTOS ===
    for elem in elements:
        group = elem["group"]
        period = elem["period"]
        symbol = elem["symbol"]
        is_highlight = elem.get("highlight", False)

        x = padding + (group - 1) * (cell_w + gap)
        y = padding + title_offset + (period - 1) * (cell_h + gap)

        # Color de fondo
        if is_highlight:
            # Buscar el color del highlight
            h_color = next(
                (h["color"] for h in highlights if h["symbol"] == symbol),
                COLORS["primary"],
            )
            fill = h_color
            stroke = h_color
            text_color = "white"
        else:
            fill = "white"
            stroke = "#e2e8f0"
            text_color = COLORS["text"]

        # Celda
        svg.append(
            f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{fill}" stroke="{stroke}" stroke-width="1.5" rx="4"/>'
        )

        # Símbolo
        font_size = 11 if len(symbol) <= 2 else 9
        svg.append(
            f'<text x="{x + cell_w / 2}" y="{y + cell_h / 2 + 4}" font-family="Inter, sans-serif" font-size="{font_size}" font-weight="bold" fill="{text_color}" text-anchor="middle">{symbol}</text>'
        )

    # === LEYENDA DE COORDENADAS (LADO DERECHO) ===
    legend_x = padding + cols * (cell_w + gap) + 20
    legend_y = padding + title_offset

    # Título de leyenda
    svg.append(
        f'<text x="{legend_x + 70}" y="{legend_y}" font-family="Inter, sans-serif" font-size="12" font-weight="900" fill="{COLORS["text"]}" text-anchor="middle">Coordenadas</text>'
    )

    # Elementos destacados
    for i, h in enumerate(highlights):
        y = legend_y + 25 + i * 50

        # Caja del elemento
        svg.append(
            f'<rect x="{legend_x}" y="{y}" width="45" height="35" fill="{h["color"]}" stroke="{h["color"]}" stroke-width="2" rx="6"/>'
        )
        svg.append(
            f'<text x="{legend_x + 22}" y="{y + 24}" font-family="Inter, sans-serif" font-size="16" font-weight="bold" fill="white" text-anchor="middle">{h["symbol"]}</text>'
        )

        # Nombre y coordenadas
        svg.append(
            f'<text x="{legend_x + 55}" y="{y + 14}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{COLORS["text"]}">{h["name"]}</text>'
        )
        svg.append(
            f'<text x="{legend_x + 55}" y="{y + 30}" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text_light"]}">Grupo {h["group"]} • Período {h["period"]}</text>'
        )

    # === LEYENDA INFERIOR ===
    bottom_y = padding + title_offset + rows * (cell_h + gap) + 25

    # Explicación de grupos
    svg.append(
        f'<rect x="{padding}" y="{bottom_y}" width="300" height="35" fill="#eff6ff" stroke="{COLORS["primary"]}" stroke-width="1.5" rx="6"/>'
    )
    svg.append(
        f'<text x="{padding + 10}" y="{bottom_y + 15}" font-family="Inter, sans-serif" font-size="10" font-weight="bold" fill="{COLORS["primary"]}">Grupos = Columnas verticales (1-18)</text>'
    )
    svg.append(
        f'<text x="{padding + 10}" y="{bottom_y + 28}" font-family="Inter, sans-serif" font-size="9" fill="{COLORS["text_light"]}">Elementos del mismo grupo tienen propiedades similares</text>'
    )

    # Explicación de períodos
    svg.append(
        f'<rect x="{padding + 320}" y="{bottom_y}" width="300" height="35" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5" rx="6"/>'
    )
    svg.append(
        f'<text x="{padding + 330}" y="{bottom_y + 15}" font-family="Inter, sans-serif" font-size="10" font-weight="bold" fill="#8b5cf6">Períodos = Filas horizontales (1-7)</text>'
    )
    svg.append(
        f'<text x="{padding + 330}" y="{bottom_y + 28}" font-family="Inter, sans-serif" font-size="9" fill="{COLORS["text_light"]}">El número de período = niveles de energía</text>'
    )

    svg.append("</svg>")

    # Ajustar altura
    final_height = bottom_y + 50
    svg[0] = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {final_height}">'
    )
    svg[1] = (
        f'<rect width="{width}" height="{final_height}" fill="{COLORS["background"]}" rx="12"/>'
    )

    return "\n".join(svg)


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    spec = load_spec(args.spec)
    svg_content = render_groups_periods(spec)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(svg_content, encoding="utf-8")
    print(f"✅ SVG generado: {args.output}")


if __name__ == "__main__":
    main()
