#!/usr/bin/env python3
"""
Renderer: Período = Número de Capas
Diseño: Tabla ancha arriba + átomos abajo
"""

import sys
import math
from pathlib import Path


def generate_svg():
    width = 900
    height = 400

    svg = []
    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">'
    )
    svg.append(f'<rect width="{width}" height="{height}" fill="#f8fafc" rx="12"/>')

    # Title
    svg.append(
        f'<text x="450" y="28" font-family="Inter, sans-serif" font-size="16" font-weight="900" fill="#1e293b" text-anchor="middle">Período = Número de Capas de Electrones</text>'
    )

    # Colors per period
    colors = {1: "#3b82f6", 2: "#22c55e", 3: "#f97316", 4: "#8b5cf6"}

    # Table config
    table_y = 45
    cell_w = 45
    cell_h = 28
    cell_gap = 2
    group_gap = 80  # Gap between groups 2 and 13

    # Center the table - calculate total width
    # Table has 8 cells + 1 gap in middle = 8*cell_w + 7*cell_gap + group_gap
    table_total_width = 8 * cell_w + 7 * cell_gap + group_gap
    table_start_x = (width - table_total_width) / 2

    # Period number position
    period_x = table_start_x - 20

    # Elements per period: (symbol, group_number)
    # Groups: 1, 2, (gap), 13, 14, 15, 16, 17, 18
    period_elements = {
        1: [("H", 1), ("He", 18)],
        2: [
            ("Li", 1),
            ("Be", 2),
            ("B", 13),
            ("C", 14),
            ("N", 15),
            ("O", 16),
            ("F", 17),
            ("Ne", 18),
        ],
        3: [
            ("Na", 1),
            ("Mg", 2),
            ("Al", 13),
            ("Si", 14),
            ("P", 15),
            ("S", 16),
            ("Cl", 17),
            ("Ar", 18),
        ],
        4: [
            ("K", 1),
            ("Ca", 2),
            ("Ga", 13),
            ("Ge", 14),
            ("As", 15),
            ("Se", 16),
            ("Br", 17),
            ("Kr", 18),
        ],
    }

    # Highlight elements
    highlight = {1: "H", 2: "Li", 3: "Na", 4: "K"}

    # Group to x position mapping
    def group_to_x(group):
        if group <= 2:
            return table_start_x + (group - 1) * (cell_w + cell_gap)
        else:
            return (
                table_start_x
                + 2 * (cell_w + cell_gap)
                + group_gap
                + (group - 13) * (cell_w + cell_gap)
            )

    # Draw table
    for period in range(1, 5):
        color = colors[period]
        y = table_y + (period - 1) * (cell_h + 6)

        # Period number
        svg.append(
            f'<text x="{period_x}" y="{y + cell_h / 2 + 5}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{color}" text-anchor="middle">{period}</text>'
        )

        # Draw cells
        for symbol, group in period_elements[period]:
            x = group_to_x(group)
            is_highlight = symbol == highlight[period]

            if is_highlight:
                svg.append(
                    f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{color}" rx="4"/>'
                )
                svg.append(
                    f'<text x="{x + cell_w / 2}" y="{y + cell_h / 2 + 5}" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="white" text-anchor="middle">{symbol}</text>'
                )
            else:
                svg.append(
                    f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="white" stroke="{color}" stroke-width="1" rx="4"/>'
                )
                svg.append(
                    f'<text x="{x + cell_w / 2}" y="{y + cell_h / 2 + 4}" font-family="Inter, sans-serif" font-size="11" fill="#64748b" text-anchor="middle">{symbol}</text>'
                )

    # === ATOMS BELOW ===
    atom_y = 250
    atom_spacing = 225
    atom_start_x = 112

    electron_config = {"H": [1], "Li": [2, 1], "Na": [2, 8, 1], "K": [2, 8, 8, 1]}

    for i, period in enumerate([1, 2, 3, 4]):
        color = colors[period]
        symbol = highlight[period]
        cx = atom_start_x + i * atom_spacing

        # Nucleus
        svg.append(f'<circle cx="{cx}" cy="{atom_y}" r="14" fill="{color}"/>')
        svg.append(
            f'<text x="{cx}" y="{atom_y + 5}" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="white" text-anchor="middle">{symbol}</text>'
        )

        # Shells
        shells = electron_config[symbol]
        base_r = 26
        shell_gap = 14

        for shell_idx, e_count in enumerate(shells):
            r = base_r + shell_idx * shell_gap
            svg.append(
                f'<circle cx="{cx}" cy="{atom_y}" r="{r}" fill="none" stroke="{color}" stroke-width="1.5" opacity="0.5"/>'
            )

            # Electrons
            for e in range(e_count):
                angle = (2 * math.pi * e / e_count) - math.pi / 2
                ex = cx + r * math.cos(angle)
                ey = atom_y + r * math.sin(angle)
                svg.append(
                    f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="3.5" fill="#3b82f6"/>'
                )

        # Label below
        svg.append(
            f'<text x="{cx}" y="{atom_y + 70}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{color}" text-anchor="middle">{period} capa{"" if period == 1 else "s"}</text>'
        )

        # Electron config
        e_text = " · ".join([f"{n}e" for n in shells])
        svg.append(
            f'<text x="{cx}" y="{atom_y + 85}" font-family="Inter, sans-serif" font-size="9" fill="#64748b" text-anchor="middle">{e_text}</text>'
        )

    # Simple footer
    svg.append(
        f'<text x="450" y="385" font-family="Inter, sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">El número de período indica cuántas capas de electrones tiene el átomo</text>'
    )

    svg.append("</svg>")

    return "\n".join(svg)


if __name__ == "__main__":
    output_path = (
        Path(__file__).parent.parent.parent
        / "public"
        / "images"
        / "quimica"
        / "periodos-niveles"
        / "periodo-como-fila.svg"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(generate_svg())

    print(f"SVG generado: {output_path}")
