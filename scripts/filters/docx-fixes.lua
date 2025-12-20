--[[
  docx-fixes.lua
  Filtro Pandoc para corregir formato en documentos Word
]]

-- Variable para rastrear si ya pasamos el primer H1
local first_h1_seen = false

-- Agregar salto de página SOLO antes de H1 (nuevas lecciones)
function Header(el)
  if el.level == 1 then
    if first_h1_seen then
      -- Agregar salto de página antes de este H1 (no el primero)
      local pagebreak = pandoc.RawBlock('openxml', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
      return {pagebreak, el}
    else
      first_h1_seen = true
      return el
    end
  end
  return el
end

-- Forzar estilo de tabla: bordes, centrada, ancho completo
function Table(tbl)
  -- Modificar atributos de la tabla para centrarla y darle ancho completo
  -- Esto se hace agregando clases que Pandoc traduce a estilos
  
  -- Crear un bloque OpenXML con las propiedades de tabla deseadas
  local table_props = pandoc.RawBlock('openxml', [[
<w:tblPr>
  <w:tblStyle w:val="TableGrid"/>
  <w:tblW w:w="5000" w:type="pct"/>
  <w:jc w:val="center"/>
  <w:tblBorders>
    <w:top w:val="single" w:sz="4" w:space="0" w:color="auto"/>
    <w:left w:val="single" w:sz="4" w:space="0" w:color="auto"/>
    <w:bottom w:val="single" w:sz="4" w:space="0" w:color="auto"/>
    <w:right w:val="single" w:sz="4" w:space="0" w:color="auto"/>
    <w:insideH w:val="single" w:sz="4" w:space="0" w:color="auto"/>
    <w:insideV w:val="single" w:sz="4" w:space="0" w:color="auto"/>
  </w:tblBorders>
</w:tblPr>
]])

  -- Agregar atributos a la tabla para que Pandoc aplique estilos
  if tbl.attr then
    tbl.attr.classes:insert("table-centered")
  end
  
  return tbl
end
