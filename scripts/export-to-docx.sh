#!/bin/bash
# ============================================================
# export-to-docx.sh
# Exporta múltiples lecciones Markdown a un único documento Word
# con LaTeX renderizado, imágenes SVG en alta resolución (Playwright)
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

# Procesar un archivo markdown
process_markdown_file() {
    local input_file="$1"
    local temp_images_dir="$2"
    local project_root="$3"
    local output_md="$4"
    
    # Leer contenido
    local content=$(cat "$input_file")
    
    # Procesar cada línea - reemplazar imágenes con placeholders
    while IFS= read -r line; do
        # Verificar si la línea contiene una imagen
        if echo "$line" | grep -q '!\[.*\](/images/'; then
            # Extraer el texto alternativo (descripción de la imagen)
            alt_text=$(echo "$line" | sed -E 's/!\[([^\]]*)\].*/\1/')
            
            # Generar URL usando la lógica existente del proyecto (cleanSlug)
            lesson_url=$(node "${project_root}/scripts/get-lesson-url.mjs" "$input_file" 2>/dev/null)
            full_url="https://ediprofe.com/${lesson_url}"
            
            # Crear placeholder vistoso para el docente
            echo "" >> "$output_md"
            echo "> **📷 INSERTAR IMAGEN AQUÍ**" >> "$output_md"
            echo ">" >> "$output_md"
            echo "> *${alt_text}*" >> "$output_md"
            echo ">" >> "$output_md"
            echo "> 🔗 [Ver imagen en la web](${full_url})" >> "$output_md"
            echo "" >> "$output_md"
        else
            echo "$line" >> "$output_md"
        fi
    done <<< "$content"
}

main() {
    parse_args "$@"
    
    SCRIPT_PATH="${BASH_SOURCE[0]}"
    SCRIPT_DIR_ABS="$(cd "$(dirname "$SCRIPT_PATH")" && pwd)"
    PROJECT_ROOT="$(cd "$SCRIPT_DIR_ABS/.." && pwd)"
    SCRIPT_DIR="${PROJECT_ROOT}/scripts"
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}📚 Exportando ${#INPUT_FILES[@]} lecciones...${NC}"
    
    TEMP_DIR=$(mktemp -d)
    TEMP_IMG_DIR="${TEMP_DIR}/converted_images"
    mkdir -p "$TEMP_IMG_DIR"
    
    COMBINED_MD="${TEMP_DIR}/combined.md"
    > "$COMBINED_MD"
    
    for i in "${!INPUT_FILES[@]}"; do
        FILE="${INPUT_FILES[$i]}"
        echo -e "  📄 Procesando: $(basename "$FILE")"
        
        process_markdown_file "$FILE" "$TEMP_IMG_DIR" "$PROJECT_ROOT" "$COMBINED_MD"
        
        if [ $i -lt $((${#INPUT_FILES[@]} - 1)) ]; then
            echo -e "\n\n\\newpage\n\n" >> "$COMBINED_MD"
        fi
    done
    
    echo -e "${GREEN}📝 Generando Word...${NC}"
    
    PANDOC_CMD="pandoc \"$COMBINED_MD\" --from markdown+tex_math_dollars --to docx --standalone"
    
    # Filtro de correcciones (tablas, alineación)
    if [ -f "$SCRIPT_DIR/filters/docx-fixes.lua" ]; then
        PANDOC_CMD="$PANDOC_CMD --lua-filter=\"$SCRIPT_DIR/filters/docx-fixes.lua\""
    fi
    
    # Plantilla
    if [ -n "$TEMPLATE_FILE" ] && [ -f "$TEMPLATE_FILE" ]; then
        PANDOC_CMD="$PANDOC_CMD --reference-doc=\"$TEMPLATE_FILE\""
    fi
    
    PANDOC_CMD="$PANDOC_CMD -o \"$OUTPUT_FILE\""
    eval $PANDOC_CMD
    
    # Post-procesar tablas (bordes y alineación)
    if [ -f "$SCRIPT_DIR/fix-docx-tables.py" ]; then
        python3 "$SCRIPT_DIR/fix-docx-tables.py" "$OUTPUT_FILE" "$OUTPUT_FILE"
    fi
    
    echo -e "${GREEN}✅ ¡Éxito! Archivo creado en: ${YELLOW}$OUTPUT_FILE${NC}"
    rm -rf "$TEMP_DIR"
}

main "$@"
