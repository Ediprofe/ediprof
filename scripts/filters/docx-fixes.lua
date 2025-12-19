--[[
  docx-fixes.lua
  Filtro Pandoc para corregir formato en documentos Word
]]

-- Forzar estilo de tabla con bordes usando OpenXML Raw
function Table(tbl)
  -- Crear wrapper con raw OpenXML para bordes
  local openxml_borders = pandoc.RawBlock('openxml', [[
<w:tblPr>
  <w:tblStyle w:val="TableGrid"/>
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
  
  -- Retornar tabla con estilo
  return tbl
end
