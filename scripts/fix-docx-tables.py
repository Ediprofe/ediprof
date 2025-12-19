#!/usr/bin/env python3
"""
fix-docx-tables.py
Agrega bordes a todas las tablas de un documento Word generado por Pandoc.

Uso: python3 fix-docx-tables.py input.docx output.docx
"""

import sys
import zipfile
import shutil
import os
import re
from xml.etree import ElementTree as ET

# Namespace de Word
WORD_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ET.register_namespace('w', WORD_NS)

def add_borders_to_tables(input_path, output_path):
    """Agrega bordes a todas las tablas y corrige alineación del texto."""
    
    # Crear copia temporal
    temp_dir = f"/tmp/docx_fix_{os.getpid()}"
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        # Extraer docx
        with zipfile.ZipFile(input_path, 'r') as z:
            z.extractall(temp_dir)
        
        # Modificar document.xml
        doc_path = os.path.join(temp_dir, 'word', 'document.xml')
        
        with open(doc_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # =============================================
        # 1. AGREGAR BORDES A TABLAS
        # =============================================
        borders_xml = '''<w:tblBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>
            <w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>
            <w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>
        </w:tblBorders>'''
        
        pattern_no_borders = r'(<w:tblPr[^>]*>)((?:(?!</w:tblPr>).)*?)(</w:tblPr>)'
        
        def add_borders(match):
            start = match.group(1)
            middle = match.group(2)
            end = match.group(3)
            if 'w:tblBorders' in middle:
                return match.group(0)
            return start + middle + borders_xml + end
        
        content = re.sub(pattern_no_borders, add_borders, content, flags=re.DOTALL)
        
        pattern_table_no_pr = r'(<w:tbl[^>]*>)(?!\s*<w:tblPr)'
        replacement_with_pr = r'\1<w:tblPr>' + borders_xml + '</w:tblPr>'
        content = re.sub(pattern_table_no_pr, replacement_with_pr, content)
        
        # =============================================
        # 2. CAMBIAR JUSTIFICACIÓN A ALINEACIÓN IZQUIERDA
        # =============================================
        # Reemplazar w:jc val="both" (justificado) por val="left" (izquierda)
        content = re.sub(r'<w:jc w:val="both"/>', '<w:jc w:val="left"/>', content)
        content = re.sub(r'<w:jc w:val="both" />', '<w:jc w:val="left"/>', content)
        
        # También en propiedades de párrafo con justificación
        content = re.sub(r'w:val="both"', 'w:val="left"', content)
        
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # =============================================
        # 3. MODIFICAR ESTILOS (styles.xml) 
        # =============================================
        styles_path = os.path.join(temp_dir, 'word', 'styles.xml')
        if os.path.exists(styles_path):
            with open(styles_path, 'r', encoding='utf-8') as f:
                styles_content = f.read()
            
            # Cambiar justificación a izquierda en los estilos también
            styles_content = re.sub(r'<w:jc w:val="both"/>', '<w:jc w:val="left"/>', styles_content)
            styles_content = re.sub(r'<w:jc w:val="both" />', '<w:jc w:val="left"/>', styles_content)
            
            with open(styles_path, 'w', encoding='utf-8') as f:
                f.write(styles_content)
        
        # Reempaquetar docx
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, temp_dir)
                    z.write(file_path, arc_name)
        
        print(f"✅ Documento corregido: bordes + alineación izquierda")
        
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 fix-docx-tables.py input.docx [output.docx]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file
    
    add_borders_to_tables(input_file, output_file)
