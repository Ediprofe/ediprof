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

### Comandos principales

| Comando | Qué muestra |
|---------|-------------|
| `npm run dev` | Solo contenido **publicado** (simula producción) |
| `npm run dev:all` | **TODO** el contenido (incluso borradores) |
| `npm run build` | Build de producción |

```bash
cd ~/Documents/EDIPROFE.COM/ediprof

# Para desarrollo normal (ver borradores)
npm run dev:all

# Para simular producción
npm run dev
```

El sitio estará en: **http://localhost:4321** (o 4322 si el puerto está ocupado)

---

## 🔀 FLUJO DE TRABAJO (dev → main)

### Ramas
- **`dev`** → Trabajo en desarrollo (usa `npm run dev:all`)
- **`main`** → Producción (solo contenido aprobado)

### Sistema de borradores

Cada tema tiene un `_meta.json` que controla si se publica:

```json
// Borrador (NO se publica)
{ "name": "Fracciones", "draft": true }

// Publicado
{ "name": "Fracciones", "draft": false }
// O simplemente:
{ "name": "Fracciones" }
```

### Aprobar un tema para producción

```bash
# 1. Editar _meta.json del tema
#    Cambiar "draft": true → "draft": false

# 2. Commit en dev
git add src/content/materia/capitulo/tema/_meta.json
git commit -m "✅ Aprobar tema X"

# 3. Merge a main y push
git checkout main
git merge dev
git push origin main
```

---

## 📝 CORREGIR LECCIONES (con agente IA)

### Prompt rápido
```
Corrige esta lección siguiendo el estilo Ediprofe.
**Lección:** src/content/matematicas/02-algebra/01-introduccion/01-lenguaje-algebraico.md
```

### Archivos de referencia
- `.agent/prompts/corregir-leccion.md` → Prompt completo
- `.agent/prompts/estilo-ediprofe.md` → Referencia de estilo

### Estructura obligatoria de toda lección
```
□ # **Título** (SIN emoji en H1)
□ Párrafo intro (1-2 oraciones)
□ ## 🎯 ¿Qué vas a aprender? (4-5 puntos)
□ Contenido con ejemplos paso a paso
□ ## 📝 Ejercicios de Práctica (10 ejercicios con <details>)
□ ## 🔑 Resumen (tabla + conclusión)
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

Ediprofe maneja **3 tipos de imágenes** con estrategias diferentes:

| Tipo | Almacenamiento | Ejemplo |
|------|----------------|---------|
| **PNG/JPG/WebP** (fotos, dibujos) | Cloudflare R2 (CDN) | `https://cdn.ediprofe.com/img/fisica/a1b2-nombre.webp` |
| **SVG generados** (geometría, gráficas) | Local (`public/images/`) | `/images/geometria/circulos/radio.svg` |
| **Tablet** (dibujos manuales) | R2 o local | Prefijo `t-` |

---

### ⭐ Sistema R2 para PNG/JPG (RECOMENDADO)

Las imágenes PNG y JPG se almacenan en **Cloudflare R2** con:
- ✅ **Optimización automática** (PNG → WebP, reduce ~60-80%)
- ✅ **CDN global** (carga rápida en todo el mundo)
- ✅ **URLs independientes** (no se rompen si reorganizas carpetas)
- ✅ **ID único** (evita colisiones de nombres)

#### Flujo de trabajo

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  1. Copiar  │────▶│ 2. npm run  │────▶│ 3. Selects  │────▶│ 4. Cmd+V   │
│  a inbox/   │     │    img      │     │   materia   │     │  en .md    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

#### Paso 1: Copiar imagen al inbox
```bash
cp ~/Downloads/grafica-velocidad.png inbox/
```

#### Paso 2: Ejecutar el menú interactivo
```bash
npm run img
```

El menú te guía:
1. **Busca la imagen** → escribe para filtrar (autocompletado)
2. **Selecciona materia** → usa flechas ↑↓
3. **¿Eliminar original?** → limpia inbox automáticamente
4. **¿Subir otra?** → si hay más imágenes

#### Paso 3: Pegar en tu markdown
El comando copia automáticamente el markdown. Solo haz **Cmd+V**:

```markdown
![grafica-velocidad](https://cdn.ediprofe.com/img/fisica/x7k9-grafica-velocidad.webp)
```

#### ¿Qué hace el sistema?

| Paso | Acción | Resultado |
|------|--------|-----------|
| 1 | Genera ID único | `x7k9` (4 chars alfanuméricos) |
| 2 | Optimiza imagen | PNG 500KB → WebP 80KB |
| 3 | Sube a R2 | `img/fisica/x7k9-grafica-velocidad.webp` |
| 4 | Actualiza índice | `images-index.json` |
| 5 | Copia markdown | Al clipboard, listo para pegar |

#### Comandos útiles
```bash
# Menú interactivo (recomendado)
npm run img

# Listar todas las imágenes subidas
npm run img -- --list

# Listar solo imágenes de física
npm run img -- --list fisica

# Buscar imagen por nombre
npm run img -- --search velocidad
```

#### Estructura en R2
```
Bucket: ediprofe
Domain: cdn.ediprofe.com
├── img/
│   ├── fisica/
│   │   ├── x7k9-grafica-velocidad.webp
│   │   └── a2b3-diagrama-mru.webp
│   ├── matematicas/
│   ├── quimica/
│   └── ciencias/
└── pdf/
    └── (PDFs de temas - manual)
```

#### ¿Por qué ID único?

El ID de 4 caracteres (`x7k9`, `a2b3`, etc.) garantiza:

1. **Unicidad**: Aunque subas dos `velocidad.png`, tendrán IDs diferentes
2. **Independencia**: La URL no depende de la estructura de carpetas del proyecto
3. **Flexibilidad**: Puedes reorganizar lecciones sin romper enlaces
4. **Trazabilidad**: `images-index.json` guarda el historial completo

#### Índice local (`images-index.json`)
```json
{
  "images": [
    {
      "id": "x7k9",
      "name": "grafica-velocidad.webp",
      "originalName": "grafica-velocidad.png",
      "materia": "fisica",
      "url": "https://cdn.ediprofe.com/img/fisica/x7k9-grafica-velocidad.webp",
      "uploadedAt": "2024-12-24T..."
    }
  ]
}
```

---

### SVGs generados (geometría, gráficas)

Los SVGs se generan con **Python/SymPy** y se guardan **localmente** (no en R2):

```markdown
![Radio de circunferencia](/images/geometria/circulos/radio.svg)
```

**¿Por qué local?**
- Los SVGs son pequeños (~5-20KB)
- Se generan automáticamente con renderers
- Están versionados en Git
- No necesitan optimización

**Ubicación:** `public/images/geometria/`, `public/images/analitica/`, etc.

---

### Imágenes de tablet (dibujos manuales)

Para dibujos hechos a mano en tablet:

1. **Nombrar con prefijo `t-`**: `t-diagrama-fuerzas.png`
2. **Subir a R2** (recomendado):
   ```bash
   cp t-diagrama-fuerzas.png inbox/
   npm run img
   ```
3. **O guardar local** en `public/images/{materia}/t-nombre.png`

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
3. Verificar que la extensión del archivo sea correcta (.png, .jpg)

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
4. **Para agregar dibujos de tablet:** Usa sintaxis estándar Markdown

---

## 📚 DOCUMENTOS RELACIONADOS

| Documento | Para quién | Contenido |
|-----------|------------|-----------|
| `USUARIO.md` | **Tú** | Comandos y guías prácticas |
| `PETICION.md` | Agente IA | Punto de entrada para peticiones |
| `CLAUDE.md` | Agente IA | Referencia técnica completa |
| `.agent/workflows/` | Agente IA | Workflows específicos por tipo |

