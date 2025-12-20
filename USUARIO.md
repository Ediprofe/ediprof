# 👤 GUÍA PARA EL USUARIO - Ediprofe

> **Este documento es para ti, el dueño del proyecto.** Contiene comandos, scripts y tips prácticos para gestionar la plataforma.

---

## 📋 Resumen del Proyecto

| Aspecto | Detalle |
|---------|---------|
| **URL** | https://ediprofe.com |
| **Framework** | Astro (Static Site Generation) |
| **Hosting** | Vercel |
| **Contenido** | Markdown + LaTeX + SVGs |
| **Materias** | Matemáticas, Física, Química, Ciencias |

---

## 🚀 DESARROLLO LOCAL

### Iniciar servidor de desarrollo
```bash
cd ~/Documents/EDIPROFE.COM/ediprof
npm run dev
```
El sitio estará en: **http://localhost:4321** (o 4322 si el puerto está ocupado)

### Build de producción
```bash
npm run build
```

### Preview del build
```bash
npm run preview
```

---

## 📤 EXPORTAR LECCIONES (PDF / Word)

### ⭐ Forma fácil (menú interactivo)
```bash
npm run export
```

Te guiará paso a paso:
1. ¿PDF o Word?
2. ¿Qué materia?
3. ¿Qué unidad?
4. ¿Qué tema?
5. ¿Todo el tema o lecciones específicas?
6. ¿Nombre del archivo?

> **Nota:** Para PDF, el servidor debe estar corriendo (`npm run dev`)

---

## 📄 COMANDOS AVANZADOS (PDF)

### PDF de una lección individual
```bash
node scripts/export-to-pdf.mjs \
  --lesson fisica/introduccion-a-la-fisica/introduccion/la-fisica-y-sus-ramas \
  --output ~/Desktop/leccion.pdf
```

### PDF de un tema completo
```bash
node scripts/export-to-pdf.mjs \
  --tema fisica/introduccion-a-la-fisica/introduccion \
  --output ~/Desktop/guia-introduccion-fisica.pdf
```

---

## 📝 COMANDOS AVANZADOS (Word)

### Una lección individual
```bash
bash scripts/export-to-docx.sh \
  src/content/fisica/01-introduccion-a-la-fisica/01-introduccion/01-la-fisica-y-sus-ramas.md \
  -o ~/Desktop/leccion.docx
```

### Múltiples lecciones en un solo documento
```bash
bash scripts/export-to-docx.sh \
  src/content/fisica/01-introduccion-a-la-fisica/01-introduccion/01-la-fisica-y-sus-ramas.md \
  src/content/fisica/01-introduccion-a-la-fisica/01-introduccion/02-metodo-cientifico.md \
  -o ~/Desktop/guia-completa.docx
```

---

## 🆕 CREAR NUEVA LECCIÓN

```bash
node scripts/new-lesson.js
```

Te pedirá:
1. Materia (matematicas, fisica, quimica, ciencias)
2. Capítulo
3. Tema
4. Nombre de la lección

---

## 📁 ESTRUCTURA DE CARPETAS

```
ediprof/
├── src/
│   ├── content/                    # 📚 AQUÍ VAN LAS LECCIONES
│   │   ├── matematicas/
│   │   │   ├── 01-aritmetica/
│   │   │   │   ├── 01-tema/
│   │   │   │   │   ├── _meta.json  # Metadatos del tema
│   │   │   │   │   ├── 01-leccion.md
│   │   │   │   │   └── 02-leccion.md
│   │   ├── fisica/
│   │   ├── quimica/
│   │   └── ciencias/
│   ├── components/                 # Componentes Astro
│   ├── layouts/                    # Layouts de páginas
│   └── styles/                     # Estilos CSS
├── public/
│   └── images/                     # 🖼️ IMÁGENES Y SVGs
│       ├── geometria/
│       ├── fisica/
│       └── quimica/
├── scripts/                        # 🔧 SCRIPTS DE AUTOMATIZACIÓN
│   ├── geometry/                   # Renderers de geometría
│   ├── export-to-pdf.mjs
│   └── export-to-docx.sh
├── specs/                          # Specs JSON para ilustraciones
├── CLAUDE.md                       # Doc técnico para agentes
├── PETICION.md                     # Punto de entrada para peticiones
└── USUARIO.md                      # Este documento
```

---

## 🎨 COLORES POR MATERIA

| Materia | Color | Hex |
|---------|-------|-----|
| 🧮 Matemáticas | Rojo | `#ef4444` |
| ⚡ Física | Azul | `#3b82f6` |
| 🧪 Química | Naranja | `#ea580c` |
| 🌿 Ciencias | Verde | `#22c55e` |

---

## 🖼️ AGREGAR IMÁGENES

### SVGs generados (geometría, gráficas)
```markdown
![Descripción](/images/geometria/circulos/radio.svg)
```

### Imágenes de tablet (dibujos manuales)

1. Nombrar con prefijo `t-`: `t-mi-dibujo.png`
2. Guardar en: `public/images/{materia}/t-mi-dibujo.png`
3. Convertir archivo a `.mdx` (renombrar de `.md` a `.mdx`)
4. Agregar imports al inicio:

```mdx
import { Image } from 'astro:assets';
import miDibujo from '/public/images/quimica/t-mi-dibujo.png';

# Título de la lección

<Image src={miDibujo} alt="Descripción" format="webp" />
```

---

## ✅ VERIFICAR SVGs

Después de que un agente modifique los renderers:
```bash
bash scripts/verify-svg-rendering.sh
```

---

## 🔗 URLS DEL SITIO

### Producción
- **Inicio:** https://ediprofe.com
- **Matemáticas:** https://ediprofe.com/matematicas
- **Física:** https://ediprofe.com/fisica
- **Química:** https://ediprofe.com/quimica
- **Ciencias:** https://ediprofe.com/ciencias

### Desarrollo local
- **Inicio:** http://localhost:4321
- **Cualquier lección:** http://localhost:4321/{materia}/{capitulo}/{tema}/{leccion}

---

## 📊 ESTADÍSTICAS RÁPIDAS

Para ver cuántas lecciones hay:
```bash
find src/content -name "*.md" -o -name "*.mdx" | wc -l
```

Por materia:
```bash
find src/content/matematicas -name "*.md" | wc -l
find src/content/fisica -name "*.md" | wc -l
find src/content/quimica -name "*.md" | wc -l
find src/content/ciencias -name "*.md" | wc -l
```

---

## 🔄 DEPLOY A PRODUCCIÓN

El deploy a Vercel es **automático** cuando haces push a `main`:

```bash
git add .
git commit -m "Descripción del cambio"
git push origin main
```

Vercel detecta el push y despliega automáticamente en ~1-2 minutos.

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### El servidor no inicia
```bash
# Limpiar node_modules y reinstalar
rm -rf node_modules
npm install
npm run dev
```

### Una imagen no carga
1. Verificar que la ruta sea correcta (case-sensitive)
2. Verificar que el archivo exista en `public/images/...`
3. Si es `.mdx`, verificar que el import esté correcto

### LaTeX no renderiza
- Verificar que uses `$...$` (inline) o `$$...$$` (bloque)
- No usar `\[...\]` ni `\(...\)`
- No poner LaTeX en títulos (`## ...`)

### SVG se ve cortado
- El contenedor debe tener `width: 100%`, no `max-width: 500px`

---

## 📞 REDES SOCIALES

Configuradas en `src/config/materias.ts`:

| Red | URL |
|-----|-----|
| YouTube | https://youtube.com/@ediprofe |
| TikTok | https://tiktok.com/@ediprofe |
| Instagram | https://instagram.com/ediprofe |

---

## 💡 TIPS

1. **Para pedir contenido nuevo:** Escribe en `PETICION.md` y comparte con el agente
2. **Para revisar antes de publicar:** Usa las URLs de `/print/` y `/print-tema/`
3. **Para exportar guías completas:** Usa el script de PDF con `--tema`
4. **Para agregar dibujos de tablet:** Siempre usa `.mdx` con `<Image>` para optimización automática

---

## 📚 DOCUMENTOS RELACIONADOS

| Documento | Para quién | Contenido |
|-----------|------------|-----------|
| `USUARIO.md` | **Tú** | Comandos y guías prácticas |
| `PETICION.md` | Agente IA | Punto de entrada para peticiones |
| `CLAUDE.md` | Agente IA | Referencia técnica completa |
| `.agent/workflows/` | Agente IA | Workflows específicos por tipo |

