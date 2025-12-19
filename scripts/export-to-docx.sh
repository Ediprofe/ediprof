#!/bin/bash
# ============================================================
# export-to-docx.sh
# Exporta múltiples lecciones Markdown a un único documento Word
# con LaTeX renderizado, usando plantilla de estilos personalizada
# ============================================================
#
# USO:
#   ./scripts/export-to-docx.sh archivo1.md archivo2.md ... -o salida.docx
#
# OPCIONES:
#   -o, --output     Archivo de salida (.docx)
#   -t, --template   Plantilla Word de referencia para estilos
#   --no-images      Reemplazar imágenes con texto placeholder [IMAGEN: alt]
#
# EJEMPLO:
#   ./scripts/export-to-docx.sh \
#     src/content/fisica/**/01-introduccion/*.md \
#     -t ~/Desktop/plantilla-bitacora.docx \
#     --no-images \
#     -o ~/Desktop/guia-fisica.docx
#
# REQUISITOS:
#   - pandoc (brew install pandoc)
# ============================================================

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Verificar dependencias
check_deps() {
    if ! command -v pandoc &> /dev/null; then
        echo -e "${RED}❌ Error: pandoc no está instalado${NC}"
        echo "   Instala con: brew install pandoc"
        exit 1
    fi
}

# Parsear argumentos
parse_args() {
    INPUT_FILES=()
    OUTPUT_FILE=""
    TEMPLATE_FILE=""
    NO_IMAGES=false
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            -o|--output)
                OUTPUT_FILE="$2"
                shift 2
                ;;
            -t|--template)
                TEMPLATE_FILE="$2"
                shift 2
                ;;
            --no-images)
                NO_IMAGES=true
                shift
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                INPUT_FILES+=("$1")
                shift
                ;;
        esac
    done
    
    if [ ${#INPUT_FILES[@]} -eq 0 ]; then
        echo -e "${RED}❌ Error: No se especificaron archivos de entrada${NC}"
        show_help
        exit 1
    fi
    
    if [ -z "$OUTPUT_FILE" ]; then
        OUTPUT_FILE="output.docx"
    fi
}

show_help() {
    echo "Uso: $0 archivo1.md [archivo2.md ...] [opciones]"
    echo ""
    echo "Opciones:"
    echo "  -o, --output      Archivo de salida (.docx)"
    echo "  -t, --template    Plantilla Word de referencia para estilos"
    echo "  --no-images       Reemplazar imágenes con texto placeholder"
    echo "  -h, --help        Mostrar esta ayuda"
    echo ""
    echo "Ejemplo:"
    echo "  $0 src/content/fisica/**/*.md -t plantilla.docx -o guia.docx"
}

# Función para eliminar imágenes completamente
remove_images() {
    local input_file="$1"
    # Elimina líneas que contienen ![...](...) completamente
    sed -E '/!\[[^\]]*\]\([^\)]+\)/d' "$input_file"
}

# Función principal
main() {
    check_deps
    parse_args "$@"
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}📚 Exportando ${#INPUT_FILES[@]} lección(es) a Word${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    # Crear directorio temporal para procesar
    TEMP_DIR=$(mktemp -d)
    trap "rm -rf $TEMP_DIR" EXIT
    
    # Combinar todos los archivos con separadores de página
    COMBINED="$TEMP_DIR/combined.md"
    > "$COMBINED"
    
    for i in "${!INPUT_FILES[@]}"; do
        FILE="${INPUT_FILES[$i]}"
        if [ ! -f "$FILE" ]; then
            echo -e "${YELLOW}⚠️  Archivo no encontrado: $FILE${NC}"
            continue
        fi
        
        BASENAME=$(basename "$FILE")
        echo -e "  ${GREEN}✓${NC} $(basename "$FILE")"
        
        if [ "$NO_IMAGES" = true ]; then
            # Eliminar imágenes completamente
            remove_images "$FILE" >> "$COMBINED"
        else
            cat "$FILE" >> "$COMBINED"
        fi
        
        # Agregar salto de página entre lecciones (excepto la última)
        if [ $i -lt $((${#INPUT_FILES[@]} - 1)) ]; then
            echo -e "\n\n\\newpage\n\n" >> "$COMBINED"
        fi
    done
    
    echo ""
    echo -e "${GREEN}📝 Convirtiendo a Word...${NC}"
    
    # Obtener directorio del script para encontrar filtros
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    FILTER_DIR="$SCRIPT_DIR/filters"
    
    # Construir comando pandoc
    PANDOC_CMD="pandoc \"$COMBINED\" --from markdown+tex_math_dollars --to docx --standalone"
    
    # Agregar filtro de correcciones para docx si existe
    if [ -f "$FILTER_DIR/docx-fixes.lua" ]; then
        PANDOC_CMD="$PANDOC_CMD --lua-filter=\"$FILTER_DIR/docx-fixes.lua\""
        echo -e "  ${GREEN}✓${NC} Filtro de correcciones DOCX activado"
    fi
    
    # Agregar plantilla si se especificó
    if [ -n "$TEMPLATE_FILE" ]; then
        if [ -f "$TEMPLATE_FILE" ]; then
            PANDOC_CMD="$PANDOC_CMD --reference-doc=\"$TEMPLATE_FILE\""
            echo -e "  ${GREEN}✓${NC} Usando plantilla: $(basename "$TEMPLATE_FILE")"
        else
            echo -e "${YELLOW}⚠️  Plantilla no encontrada: $TEMPLATE_FILE${NC}"
        fi
    fi
    
    PANDOC_CMD="$PANDOC_CMD --output \"$OUTPUT_FILE\""
    
    # Ejecutar pandoc
    eval $PANDOC_CMD
    
    # Post-procesar para agregar bordes a las tablas
    if [ -f "$SCRIPT_DIR/fix-docx-tables.py" ]; then
        python3 "$SCRIPT_DIR/fix-docx-tables.py" "$OUTPUT_FILE" "$OUTPUT_FILE"
    fi
    
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}✅ Documento creado exitosamente${NC}"
    echo -e "   📄 Archivo: ${YELLOW}$OUTPUT_FILE${NC}"
    echo -e "   📚 Lecciones: ${#INPUT_FILES[@]}"
    if [ "$NO_IMAGES" = true ]; then
        echo -e "   🖼️  Imágenes: Reemplazadas con placeholders"
    fi
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

main "$@"
