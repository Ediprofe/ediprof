#!/usr/bin/env python3
"""
PERIODO COMO FILA - TABLA REALISTA
Tabla periódica con elementos reales, símbolos y nombres.
Conexión visual clara entre filas y capas de electrones.
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS


# Datos de elementos (símbolo, nombre, Z) para períodos 1-4
ELEMENTS = {
    # Período 1
    1: [(1, "H", "Hidrógeno"), (2, "He", "Helio")],
    # Período 2
    2: [
        (3, "Li", "Litio"),
        (4, "Be", "Berilio"),
        (5, "B", "Boro"),
        (6, "C", "Carbono"),
        (7, "N", "Nitrógeno"),
        (8, "O", "Oxígeno"),
        (9, "F", "Flúor"),
        (10, "Ne", "Neón"),
    ],
    # Período 3
    3: [
        (11, "Na", "Sodio"),
        (12, "Mg", "Magnesio"),
        (13, "Al", "Aluminio"),
        (14, "Si", "Silicio"),
        (15, "P", "Fósforo"),
        (16, "S", "Azufre"),
        (17, "Cl", "Cloro"),
        (18, "Ar", "Argón"),
    ],
    # Período 4
    4: [
        (19, "K", "Potasio"),
        (20, "Ca", "Calcio"),
        (21, "Sc", "Escandio"),
        (22, "Ti", "Titanio"),
        (23, "V", "Vanadio"),
        (24, "Cr", "Cromo"),
        (25, "Mn", "Manganeso"),
        (26, "Fe", "Hierro"),
        (27, "Co", "Cobalto"),
        (28, "Ni", "Níquel"),
        (29, "Cu", "Cobre"),
        (30, "Zn", "Zinc"),
        (31, "Ga", "Galio"),
        (32, "Ge", "Germanio"),
        (33, "As", "Arsénico"),
        (34, "Se", "Selenio"),
        (35, "Br", "Bromo"),
        (36, "Kr", "Kriptón"),
    ],
}

# Posiciones de grupos (1-18)
GROUP_POSITIONS = {
    1: 0,
    2: 1,
    # Grupos 3-12 (metales de transición)
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 7,
    9: 8,
    10: 9,
    11: 10,
    12: 11,
    # Grupos 13-18
    13: 12,
    14: 13,
    15: 14,
    16: 15,
    17: 16,
    18: 17,
}

# Z por grupo en cada período
Z_BY_PERIOD_GROUP = {
    1: {1: 1, 18: 2},
    2: {1: 3, 2: 4, 13: 5, 14: 6, 15: 7, 16: 8, 17: 9, 18: 10},
    3: {1: 11, 2: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18},
    4: {
        1: 19,
        2: 20,
        3: 21,
        4: 22,
        5: 23,
        6: 24,
        7: 25,
        8: 26,
        9: 27,
        10: 28,
        11: 29,
        12: 30,
        13: 31,
        14: 32,
        15: 33,
        16: 34,
        17: 35,
        18: 36,
    },
}

# Elementos a destacar con nombre
HIGHLIGHT_NAMES = {
    1: "H",
    3: "Li",
    11: "Na",
    19: "K",
    2: "He",
    10: "Ne",
    18: "Ar",
    36: "Kr",
}


def render_periodo_como_fila():
    svg = []
    width, height = 1100, 520

    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">'
    )
    svg.append(
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>'
    )

    # Título
    svg.append(
        f'<text x="{width / 2}" y="28" font-family="Inter, sans-serif" font-size="20" font-weight="900" fill="{COLORS["text"]}" text-anchor="middle">Período = Fila en la Tabla Periódica</text>'
    )

    # Colores por período
    period_colors = {
        1: "#3b82f6",
        2: "#22c55e",
        3: "#f97316",
        4: "#8b5cf6",
    }

    # ===== TABLA PERIÓDICA REALISTA =====
    table_x = 40
    table_y = 55
    cell_w = 26
    cell_h = 32
    gap = 1

    # Números de grupo arriba
    for g in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
        col = GROUP_POSITIONS[g]
        x = table_x + col * (cell_w + gap) + cell_w / 2
        svg.append(
            f'<text x="{x}" y="{table_y - 3}" font-family="Inter, sans-serif" font-size="7" fill="{COLORS["text_light"]}" text-anchor="middle">{g}</text>'
        )

    # Dibujar elementos
    for period in range(1, 5):
        color = period_colors[period]
        row_y = table_y + (period - 1) * (cell_h + gap)

        # Fondo de fila
        svg.append(
            f'<rect x="{table_x - 2}" y="{row_y - 2}" width="{18 * (cell_w + gap) + 4}" height="{cell_h + 4}" fill="{color}" opacity="0.08" rx="3"/>'
        )

        # Número de período a la izquierda
        svg.append(
            f'<text x="{table_x - 12}" y="{row_y + cell_h / 2 + 3}" font-family="Inter, sans-serif" font-size="10" font-weight="bold" fill="{color}" text-anchor="end">{period}</text>'
        )

        # Elementos de esta fila
        groups_in_period = Z_BY_PERIOD_GROUP[period]
        for group, z in groups_in_period.items():
            col = GROUP_POSITIONS[group]
            cell_x = table_x + col * (cell_w + gap)

            # Obtener símbolo
            symbol = ""
            for elem_z, sym, name in ELEMENTS[period]:
                if elem_z == z:
                    symbol = sym
                    break

            # ¿Destacar con nombre?
            is_highlighted = z in HIGHLIGHT_NAMES

            # Celda
            if is_highlighted:
                svg.append(
                    f'<rect x="{cell_x}" y="{row_y}" width="{cell_w}" height="{cell_h}" fill="{color}" stroke="white" stroke-width="1.5" rx="2"/>'
                )
                text_color = "white"
            else:
                svg.append(
                    f'<rect x="{cell_x}" y="{row_y}" width="{cell_w}" height="{cell_h}" fill="white" stroke="{color}" stroke-width="0.5" rx="2"/>'
                )
                text_color = COLORS["text"]

            # Z (arriba izquierda)
            svg.append(
                f'<text x="{cell_x + 2}" y="{row_y + 8}" font-family="Inter, sans-serif" font-size="5" fill="{text_color if is_highlighted else COLORS["text_light"]}">{z}</text>'
            )

            # Símbolo
            svg.append(
                f'<text x="{cell_x + cell_w / 2}" y="{row_y + 18}" font-family="Inter, sans-serif" font-size="9" font-weight="bold" fill="{text_color}" text-anchor="middle">{symbol}</text>'
            )

            # Nombre (solo destacados)
            if is_highlighted:
                name = ""
                for elem_z, sym, n in ELEMENTS[period]:
                    if elem_z == z:
                        name = n
                        break
                # Acortar nombre si es largo
                if len(name) > 8:
                    name = name[:7] + "."
                svg.append(
                    f'<text x="{cell_x + cell_w / 2}" y="{row_y + 27}" font-family="Inter, sans-serif" font-size="5" fill="white" text-anchor="middle">{name}</text>'
                )

    # Etiqueta "PERÍODOS"
    svg.append(
        f'<text x="{table_x - 25}" y="{table_y + 2 * (cell_h + gap) + cell_h / 2}" font-family="Inter, sans-serif" font-size="8" font-weight="bold" fill="{COLORS["text_light"]}" text-anchor="middle" transform="rotate(-90 {table_x - 25} {table_y + 2 * (cell_h + gap) + cell_h / 2})">PERÍODOS</text>'
    )

    # ===== ÁTOMOS REPRESENTATIVOS (derecha) =====
    atoms_x = 580

    # Caja
    svg.append(
        f'<rect x="{atoms_x}" y="55" width="500" height="175" rx="10" fill="white" stroke="{COLORS["grid"]}" stroke-width="1.5"/>'
    )
    svg.append(
        f'<text x="{atoms_x + 250}" y="75" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">Átomos de cada fila (con sus capas de electrones)</text>'
    )

    # 4 átomos: H, Li, Na, K
    atoms = [
        {"symbol": "H", "name": "Hidrógeno", "period": 1, "shells": [1]},
        {"symbol": "Li", "name": "Litio", "period": 2, "shells": [2, 1]},
        {"symbol": "Na", "name": "Sodio", "period": 3, "shells": [2, 8, 1]},
        {"symbol": "K", "name": "Potasio", "period": 4, "shells": [2, 8, 8, 1]},
    ]

    for i, atom in enumerate(atoms):
        ax = atoms_x + 65 + i * 120
        ay = 145
        color = period_colors[atom["period"]]

        # Núcleo
        svg.append(
            f'<circle cx="{ax}" cy="{ay}" r="12" fill="{color}" stroke="white" stroke-width="1.5"/>'
        )
        svg.append(
            f'<text x="{ax}" y="{ay + 4}" font-family="Inter, sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">{atom["symbol"]}</text>'
        )

        # Capas
        for j, e_count in enumerate(atom["shells"]):
            r = 22 + j * 12
            svg.append(
                f'<circle cx="{ax}" cy="{ay}" r="{r}" fill="none" stroke="{color}" stroke-width="1.2" opacity="0.8"/>'
            )

            # Electrones
            if e_count > 0:
                angle_step = (2 * math.pi) / e_count
                for e in range(e_count):
                    theta = -math.pi / 2 + e * angle_step
                    ex = ax + r * math.cos(theta)
                    ey = ay + r * math.sin(theta)
                    svg.append(
                        f'<circle cx="{ex}" cy="{ey}" r="2.5" fill="{COLORS["primary"]}" stroke="white" stroke-width="0.5"/>'
                    )

        # Etiqueta
        svg.append(
            f'<text x="{ax}" y="{ay + 55}" font-family="Inter, sans-serif" font-size="8" font-weight="bold" fill="{color}" text-anchor="middle">{atom["name"]}</text>'
        )
        svg.append(
            f'<text x="{ax}" y="{ay + 68}" font-family="Inter, sans-serif" font-size="9" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{atom["period"]} {"capa" if atom["period"] == 1 else "capas"}</text>'
        )

    # ===== FLECHAS CONECTORAS =====
    arrow_x = table_x + 18 * (cell_w + gap) + 15

    for period in range(1, 5):
        color = period_colors[period]
        row_y = table_y + (period - 1) * (cell_h + gap) + cell_h / 2
        atom_x = atoms_x + 65 + (period - 1) * 120

        # Línea conectora
        svg.append(
            f'<line x1="{arrow_x}" y1="{row_y}" x2="{atom_x - 30}" y2="{145}" stroke="{color}" stroke-width="2" stroke-dasharray="4,2" opacity="0.6"/>'
        )
        svg.append(f'<circle cx="{atom_x - 30}" cy="{145}" r="3" fill="{color}"/>')

    # ===== MENSAJE CLAVE =====
    msg_y = 250
    svg.append(
        f'<rect x="150" y="{msg_y}" width="800" height="40" rx="8" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="2"/>'
    )
    svg.append(
        f'<text x="{width / 2}" y="{msg_y + 17}" font-family="Inter, sans-serif" font-size="13" font-weight="bold" fill="#8b5cf6" text-anchor="middle">💡 Cada fila hacia abajo añade una capa de electrones</text>'
    )
    svg.append(
        f'<text x="{width / 2}" y="{msg_y + 32}" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text"]}" text-anchor="middle">Fila 1 = 1 capa • Fila 2 = 2 capas • Fila 3 = 3 capas • Fila 4 = 4 capas</text>'
    )

    # ===== TABLA DE EJEMPLOS =====
    ex_y = 310
    svg.append(
        f'<text x="{width / 2}" y="{ex_y}" font-family="Inter, sans-serif" font-size="13" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">Ejemplos: Elementos destacados en cada fila</text>'
    )

    examples = [
        (1, "H", "Hidrógeno", "1 capa", "#3b82f6"),
        (2, "Li", "Litio", "2 capas", "#22c55e"),
        (3, "Na", "Sodio", "3 capas", "#f97316"),
        (4, "K", "Potasio", "4 capas", "#8b5cf6"),
    ]

    for i, (period, sym, name, caps, color) in enumerate(examples):
        ex = 160 + i * 200
        svg.append(
            f'<rect x="{ex - 80}" y="{ex_y + 15}" width="160" height="55" rx="6" fill="white" stroke="{color}" stroke-width="1.5"/>'
        )
        svg.append(
            f'<circle cx="{ex - 55}" cy="{ex_y + 42}" r="12" fill="{color}" stroke="white" stroke-width="1"/>'
        )
        svg.append(
            f'<text x="{ex - 55}" y="{ex_y + 46}" font-family="Inter, sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">{sym}</text>'
        )
        svg.append(
            f'<text x="{ex + 5}" y="{ex_y + 38}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{name}</text>'
        )
        svg.append(
            f'<text x="{ex + 5}" y="{ex_y + 52}" font-family="Inter, sans-serif" font-size="10" fill="{color}" text-anchor="middle">Período {period} → {caps}</text>'
        )

    # ===== RESUMEN FINAL =====
    svg.append(
        f'<text x="{width / 2}" y="410" font-family="Inter, sans-serif" font-size="11" fill="{COLORS["text_light"]}" text-anchor="middle">Observa: H está en la fila 1 (1 capa), Li en fila 2 (2 capas), Na en fila 3 (3 capas), K en fila 4 (4 capas)</text>'
    )

    # Leyenda de gases nobles
    svg.append(
        f'<text x="{width / 2}" y="435" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text_light"]}" text-anchor="middle">Gases nobles: He (fila 1), Ne (fila 2), Ar (fila 3), Kr (fila 4) — Última columna de cada período</text>'
    )

    # ===== LEYENDA DE COLORES =====
    leg_y = 460
    svg.append(
        f'<rect x="200" y="{leg_y}" width="700" height="35" rx="6" fill="white" stroke="{COLORS["grid"]}" stroke-width="1"/>'
    )

    for i, (period, color) in enumerate(sorted(period_colors.items())):
        lx = 250 + i * 170
        svg.append(
            f'<rect x="{lx}" y="{leg_y + 8}" width="20" height="20" fill="{color}" rx="3"/>'
        )
        svg.append(
            f'<text x="{lx + 30}" y="{leg_y + 22}" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text"]}">Período {period} (Fila {period})</text>'
        )

    svg.append("</svg>")
    return "\n".join(svg)


def main():
    output_dir = Path("public/images/quimica/periodos-niveles")
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "periodo-como-fila.svg").write_text(
        render_periodo_como_fila(), encoding="utf-8"
    )
    print("✅ periodo-como-fila.svg")


if __name__ == "__main__":
    main()
