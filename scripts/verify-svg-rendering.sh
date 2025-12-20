#!/bin/bash
# ============================================================
# verify-svg-rendering.sh
# Verifica que los renderers de SVG producen resultados consistentes
# Úsalo ANTES y DESPUÉS de refactoring para comparar
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TEST_DIR="/tmp/svg-verification-$(date +%Y%m%d_%H%M%S)"

mkdir -p "$TEST_DIR"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔍 Verificación de renderizado de SVGs"
echo "   Directorio de prueba: $TEST_DIR"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

cd "$PROJECT_ROOT"

# Contador de éxitos y fallos
SUCCESS=0
FAILED=0

# Test 1: CircleSpec renderer
echo ""
echo "📐 Test 1: CircleSpec (círculos)"
for spec in specs/geometria/circulos/*.json; do
    if [ -f "$spec" ]; then
        name=$(basename "$spec" .json)
        output="$TEST_DIR/circle-$name.svg"
        if python3 scripts/geometry/circle_spec_renderer.py --spec "$spec" --output "$output" 2>/dev/null; then
            echo "   ✅ $name"
            ((SUCCESS++))
        else
            echo "   ❌ $name"
            ((FAILED++))
        fi
    fi
done

# Test 2: Trigonometry renderer
echo ""
echo "📐 Test 2: TrigonometrySpec"
for spec in specs/geometria/trigonometria/*.json; do
    if [ -f "$spec" ]; then
        name=$(basename "$spec" .json)
        output="$TEST_DIR/trig-$name.svg"
        if python3 scripts/geometry/trigonometry_renderer.py --spec "$spec" --output "$output" 2>/dev/null; then
            echo "   ✅ $name"
            ((SUCCESS++))
        else
            echo "   ❌ $name"
            ((FAILED++))
        fi
    fi
done

# Test 3: Funciones renderer (si hay specs)
echo ""
echo "📐 Test 3: GraphSpec (funciones)"
count=0
for spec in specs/funciones/*.json; do
    if [ -f "$spec" ] && [ $count -lt 5 ]; then
        name=$(basename "$spec" .json)
        output="$TEST_DIR/func-$name.svg"
        if python3 scripts/functions/renderer.py --spec "$spec" --output "$output" 2>/dev/null; then
            echo "   ✅ $name"
            ((SUCCESS++))
        else
            echo "   ❌ $name"
            ((FAILED++))
        fi
        ((count++))
    fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Resumen:"
echo "   ✅ Exitosos: $SUCCESS"
echo "   ❌ Fallidos: $FAILED"
echo ""
echo "   SVGs generados en: $TEST_DIR"
echo ""

# Generar hash de todos los SVGs
HASH_FILE="$TEST_DIR/svg-hashes.txt"
find "$TEST_DIR" -name "*.svg" -exec md5 {} \; | sort > "$HASH_FILE"
echo "   Hashes guardados en: $HASH_FILE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ $FAILED -gt 0 ]; then
    exit 1
fi
