# App MVP Wireframes (Conceptual)

## 1) Home
```mermaid
flowchart LR
  A[Header: Hola + streak] --> B[Card: Plan de hoy]
  B --> C[CTA: Iniciar sesion]
  A --> D[Progreso por area]
  D --> E[Quimica]
  D --> F[Biologia]
  D --> G[Fisica]
```

## 2) Biblioteca
```mermaid
flowchart TD
  A[Filtros] --> B[Area]
  A --> C[Unidad]
  A --> D[Modulo]
  A --> E[Nivel]
  B --> F[Lista de tarjetas]
  C --> F
  D --> F
  E --> F
```

## 3) Sesion de practica
```mermaid
flowchart TD
  A[Pregunta n/20] --> B[Timer]
  A --> C[Opciones A-D]
  C --> D[Responder]
  D --> E[Feedback inmediato]
  E --> F[Siguiente]
```

## 4) Resultado
```mermaid
flowchart LR
  A[Puntaje] --> B[Errores clave]
  B --> C[Causa probable]
  C --> D[Recomendacion siguiente]
  D --> E[Repetir bloque]
```

## Nota
Estos wireframes son de flujo y jerarquia. El UI visual final se define en Figma/Excalidraw, pero el comportamiento ya queda definido por estos bloques.
