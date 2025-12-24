# Sistema de Imágenes con Cloudflare R2

## Resumen

Las imágenes PNG se optimizan localmente (→ WebP) y se suben a Cloudflare R2 con un ID único automático. Esto permite:

- ✅ URLs permanentes (nunca se rompen)
- ✅ Reorganizar el proyecto sin afectar imágenes
- ✅ Optimización automática (~80% reducción)
- ✅ CDN global incluido

## Configuración Inicial (Una sola vez)

### 1. Crear Bucket R2 en Cloudflare

1. Ve a [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Selecciona tu cuenta → R2 Object Storage
3. Click "Create bucket"
4. Nombre: `ediprof-cdn`
5. Ubicación: Automatic

### 2. Configurar Dominio Público

1. En el bucket, ve a "Settings" → "Public access"
2. Click "Connect Domain"
3. Ingresa: `cdn.ediprofe.com`
4. Cloudflare configurará el DNS automáticamente

### 3. Instalar y Configurar Wrangler

```bash
# Instalar wrangler globalmente
npm install -g wrangler

# Autenticarse (abre navegador)
wrangler login

# Verificar conexión
wrangler r2 bucket list
```

### 4. Actualizar Configuración del Script

Edita `scripts/upload-to-r2.mjs` y cambia:

```javascript
const CONFIG = {
  r2Bucket: 'ediprof-cdn',           // Tu bucket
  cdnDomain: 'cdn.ediprofe.com',     // Tu dominio
  // ...
};
```

## Uso Diario

### Subir una imagen

```bash
# 1. Guarda la imagen en inbox/
cp ~/Downloads/mi-grafica.png inbox/

# 2. Sube con el comando
npm run img mi-grafica.png -- --materia fisica

# 3. Pega el markdown (ya está en el clipboard)
# Cmd+V en tu archivo .mdx
```

### Buscar imágenes existentes

```bash
# Listar todas
npm run img -- --list

# Listar por materia
npm run img -- --list fisica

# Buscar por nombre
npm run img -- --search velocidad
```

## Estructura en R2

```
ediprof-cdn/
└── images/
    ├── fisica/
    │   ├── a3x9-grafica-velocidad.webp
    │   └── k7m2-tiro-parabolico.webp
    ├── matematicas/
    ├── quimica/
    └── ciencias/
```

## URLs Generadas

```
https://cdn.ediprofe.com/images/fisica/a3x9-grafica-velocidad.webp
                          ^^^^^^ ^^^^^^ ^^^^ ^^^^^^^^^^^^^^^^^^
                          bucket materia ID   nombre descriptivo
```

## Índice Local

El archivo `images-index.json` mantiene un registro de todas las imágenes subidas:

```json
{
  "images": [
    {
      "id": "a3x9",
      "name": "grafica-velocidad.webp",
      "materia": "fisica",
      "date": "2024-12-24",
      "size": "35KB",
      "url": "https://cdn.ediprofe.com/images/fisica/a3x9-grafica-velocidad.webp"
    }
  ]
}
```

## Preguntas Frecuentes

### ¿Qué pasa si subo dos imágenes con el mismo nombre?

Cada una recibe un ID diferente, no hay conflicto:
- `a3x9-velocidad.webp`
- `k7m2-velocidad.webp`

### ¿Puedo reorganizar mi proyecto?

Sí. Las URLs de las imágenes no dependen de la estructura de carpetas del proyecto.

### ¿Cuánto cuesta?

- **Gratis**: 10GB almacenamiento + 10M lecturas/mes
- Con 46,000 imágenes optimizadas (~2GB), sigues en tier gratis

### ¿Qué pasa con los PDFs?

Usa la misma lógica. Crea una carpeta `pdfs/` en el bucket:

```bash
wrangler r2 object put ediprof-cdn/pdfs/fisica/introduccion.pdf --file="mi-archivo.pdf"
```
