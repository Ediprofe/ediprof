#!/bin/bash
# ============================================================
# export-to-docx.sh
# Exporta múltiples lecciones Markdown a un único documento Word
# con LaTeX renderizado, imágenes SVG convertidas a PNG (Playwright)
# ============================================================

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

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
            *)
                INPUT_FILES+=("$1")
                shift
                ;;
        esac
    done
    
    if [ ${#INPUT_FILES[@]} -eq 0 ]; then
        echo -e "${RED}❌ Error: No se especificaron archivos de entrada${NC}"
        exit 1
    fi
    [ -z "$OUTPUT_FILE" ] && OUTPUT_FILE="guia_exportada.docx"
}

main() {
    parse_args "$@"
    
    SCRIPT_PATH="${BASH_SOURCE[0]}"
    SCRIPT_DIR_ABS="$(cd "$(dirname "$SCRIPT_PATH")" && pwd)"
    PROJECT_ROOT="$(cd "$SCRIPT_DIR_ABS/.." && pwd)"
    SCRIPT_DIR="${PROJECT_ROOT}/scripts"
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}📚 Exportando ${#INPUT_FILES[@]} lecciones...${NC}"
    
    if [ "$NO_IMAGES" = true ]; then
        echo -e "${YELLOW}   (Modo sin imágenes - placeholders)${NC}"
        NO_IMAGES_FLAG="--no-images"
    else
        echo -e "${GREEN}   (Con imágenes incluidas)${NC}"
        NO_IMAGES_FLAG=""
    fi
    
    TEMP_DIR=$(mktemp -d)
    TEMP_IMG_DIR="${TEMP_DIR}/converted_images"
    mkdir -p "$TEMP_IMG_DIR"
    
    COMBINED_MD="${TEMP_DIR}/combined.md"
    > "$COMBINED_MD"
    
    for i in "${!INPUT_FILES[@]}"; do
        FILE="${INPUT_FILES[$i]}"
        echo -e "  📄 Procesando: $(basename "$FILE")"
        
        # Preprocesar con Node.js (más confiable que bash para regex)
        PROCESSED_MD="${TEMP_DIR}/processed_${i}.md"
        node "$SCRIPT_DIR/preprocess-markdown.mjs" "$FILE" "$PROCESSED_MD" "$TEMP_IMG_DIR" $NO_IMAGES_FLAG
        
        # Agregar al archivo combinado
        cat "$PROCESSED_MD" >> "$COMBINED_MD"
        
        if [ $i -lt $((${#INPUT_FILES[@]} - 1)) ]; then
            echo -e "\n\n\\newpage\n\n" >> "$COMBINED_MD"
        fi
    done
    
    echo -e "${GREEN}📝 Generando Word...${NC}"
    
    # Mostrar contenido para debug
    # echo "=== MARKDOWN COMBINADO ===" && head -50 "$COMBINED_MD"
    
    PANDOC_CMD="pandoc \"$COMBINED_MD\" --from markdown+tex_math_dollars --to docx --standalone"
    
    # Filtro de correcciones
    if [ -f "$SCRIPT_DIR/filters/docx-fixes.lua" ]; then
        PANDOC_CMD="$PANDOC_CMD --lua-filter=\"$SCRIPT_DIR/filters/docx-fixes.lua\""
    fi
    
    # Plantilla
    if [ -n "$TEMPLATE_FILE" ] && [ -f "$TEMPLATE_FILE" ]; then
        PANDOC_CMD="$PANDOC_CMD --reference-doc=\"$TEMPLATE_FILE\""
    fi
    
    PANDOC_CMD="$PANDOC_CMD -o \"$OUTPUT_FILE\""
    eval $PANDOC_CMD
    
    # Post-procesar (bordes, alineación, centrado de imágenes)
    if [ -f "$SCRIPT_DIR/fix-docx-tables.py" ]; then
        python3 "$SCRIPT_DIR/fix-docx-tables.py" "$OUTPUT_FILE" "$OUTPUT_FILE"
    fi
    
    echo -e "${GREEN}✅ ¡Éxito! Archivo creado en: ${YELLOW}$OUTPUT_FILE${NC}"
    rm -rf "$TEMP_DIR"
}

main "$@"
