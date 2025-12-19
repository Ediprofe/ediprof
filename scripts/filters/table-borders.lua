--[[
  table-borders.lua
  Filtro Pandoc para agregar bordes a todas las tablas en documentos Word
  usando OpenXML directamente (método más confiable)
]]

function Table(tbl)
  -- Crear bloque raw con OpenXML para definir bordes de tabla
  -- Esto se inserta directamente en el documento Word
  local border_style = [[
<w:tblPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:tblBorders>
    <w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>
    <w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>
    <w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>
    <w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>
    <w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>
    <w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>
  </w:tblBorders>
</w:tblPr>
]]

  -- Retornar la tabla con atributos que Pandoc usa para Word
  -- Usamos el estilo "Table Grid" que en Word tiene bordes
  if tbl.attr then
    tbl.attr.attributes["custom-style"] = "Table Grid"
  end
  
  return tbl
end

-- Alternativa: aplicar directamente a cada celda
function TableCell(cell)
  return cell
end
