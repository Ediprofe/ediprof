---
description: Generar actividades institucionales (Énfasis Bilingüe o ODS) a partir de URLs de localhost
---

# Workflow: /guia

## Uso

```
/guia bilingue [URL(s) de localhost]
/guia ods [URL(s) de localhost]
```

## Ejemplos

```bash
# Una lección:
/guia bilingue http://localhost:4321/ciencias/la-celula/introduccion-a-la-celula/niveles-de-organizacion

# Un tema completo (todas las lecciones):
/guia ods http://localhost:4321/ciencias/la-celula/introduccion-a-la-celula

# Varias lecciones:
/guia bilingue 
  http://localhost:4321/ciencias/la-celula/introduccion-a-la-celula/que-es-la-celula
  http://localhost:4321/ciencias/la-celula/introduccion-a-la-celula/tipos-de-celulas
```

---

## Pasos del Workflow

### 1. Identificar contenido fuente
- Parsear las URLs para obtener las rutas de los archivos `.md`
- Leer el contenido de cada lección indicada
- Si es un tema (sin lección específica), leer TODAS las lecciones del tema

### 2. Generar actividad según el tipo

#### Para `bilingue`:
Generar Markdown con estas secciones (formato compatible con Word):

| Sección | Contenido |
|---------|-----------|
| **Vocabulario Clave** | Tabla English / Español / Pronunciación (10 términos del tema) |
| **Reading Challenge** | Párrafo en inglés (80-100 palabras) resumiendo el tema + traducción al español |
| **Actividad** | Ejercicio de completar espacios o emparejar (formato texto, NO interactivo) |
| **Micro-Reto** | Instrucción para que el estudiante produzca algo (frase o dibujo etiquetado) |

#### Para `ods`:
1. **Sugerir ODS:** Analizar el contenido y proponer 1-2 ODS relacionados
2. **Pedir confirmación** al usuario antes de generar
3. Generar Markdown con estas secciones:

| Sección | Contenido |
|---------|-----------|
| **ODS Relacionado** | Número, nombre y breve descripción del ODS |
| **Conexión con el Tema** | Explicación de cómo el contenido se relaciona con el ODS |
| **Reflexión Guiada** | 2-3 preguntas para que el estudiante reflexione |
| **Micro-Acción** | Una acción concreta y realizable que el estudiante puede hacer |

### 3. Guardar el archivo
- Ruta: `guias-docente/[AÑO]-[SEMESTRE]/[tipo]-[tema].md`
- Ejemplo: `guias-docente/2026-S1/bilingue-celula.md`

### 4. Notificar al usuario
- Mostrar el archivo generado para revisión
- Indicar cómo exportar: `npm run export` → Guías docentes

---

## Exportar a Word

1. Ejecutar `npm run export`
2. Elegir: "📋 Guías docentes institucionales"
3. Seleccionar el archivo `.md` generado
4. Se exporta con plantilla `bitacora.docx`
5. Archivo `.docx` se guarda en `~/Desktop/`

---

## Referencia: Los 17 ODS

| # | Nombre | Temas relacionados comunes |
|---|--------|---------------------------|
| 1 | Fin de la pobreza | Economía, estadísticas sociales |
| 2 | Hambre cero | Biología, nutrición, ecosistemas |
| 3 | Salud y bienestar | Célula, cuerpo humano, medicina |
| 4 | Educación de calidad | Cualquier tema educativo |
| 5 | Igualdad de género | Historia, sociedad |
| 6 | Agua limpia y saneamiento | Química del agua, ecosistemas |
| 7 | Energía asequible y no contaminante | Física, energía, electricidad |
| 8 | Trabajo decente y crecimiento económico | Matemáticas financieras |
| 9 | Industria, innovación e infraestructura | Tecnología, física |
| 10 | Reducción de las desigualdades | Estadísticas, matemáticas |
| 11 | Ciudades y comunidades sostenibles | Urbanismo, geometría |
| 12 | Producción y consumo responsables | Química, física, biología |
| 13 | Acción por el clima | Física, química ambiental |
| 14 | Vida submarina | Biología marina, ecosistemas |
| 15 | Vida de ecosistemas terrestres | Biología, ecología, célula |
| 16 | Paz, justicia e instituciones sólidas | Ética, geometría de proporciones |
| 17 | Alianzas para lograr los objetivos | Colaboración, estadísticas |
