---
description: Guía para visualizar geometría 3D (cubos, prismas, pirámides) con Three.js globs: ["src/content/**/*.md"]
---

# 🎲 Workflow: Three.js (Geometría 3D)

Three.js se usa para **geometría espacial y volúmenes** que requieren visualización tridimensional.

---

## ✅ Cuándo usar Three.js

| Caso de uso | Usar Three.js |
|-------------|---------------|
| Cubo con diagonales | ✅ SÍ |
| Prismas, pirámides | ✅ SÍ |
| Cilindros, conos, esferas | ✅ SÍ |
| Volúmenes y capacidades | ✅ SÍ |
| Rotación de sólidos | ✅ SÍ |

### ❌ NO usar Three.js para:

- Geometría 2D → GeometrySpec o Rough.js
- Gráficas 2D → ECharts
- Diagramas ilustrativos → Rough.js

---

## ⚠️ Nota de Complejidad

Three.js es la tecnología **más compleja** del sistema. Usar con cuidado y solo cuando realmente se necesite 3D.

**Nivel de confianza:** ⭐⭐⭐ (70%)

---

## 🎨 Plantilla Básica

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div id="threejs-[LECCION]-[NUMERO]" style="width: 100%; height: 400px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof THREE !== 'undefined' && document.getElementById('threejs-[LECCION]-[NUMERO]')) {
    var container = document.getElementById('threejs-[LECCION]-[NUMERO]');
    var width = container.clientWidth;
    var height = container.clientHeight;
    
    // Escena
    var scene = new THREE.Scene();
    scene.background = new THREE.Color(0xf1f5f9);
    
    // Cámara
    var camera = new THREE.PerspectiveCamera(75, width/height, 0.1, 1000);
    camera.position.set(3, 3, 3);
    camera.lookAt(0, 0, 0);
    
    // Renderer
    var renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(width, height);
    container.appendChild(renderer.domElement);
    
    // Geometría (ejemplo: cubo)
    var geometry = new THREE.BoxGeometry(2, 2, 2);
    var material = new THREE.MeshBasicMaterial({ 
      color: 0x3b82f6, 
      wireframe: true 
    });
    var cube = new THREE.Mesh(geometry, material);
    scene.add(cube);
    
    // Ejes de referencia
    var axesHelper = new THREE.AxesHelper(3);
    scene.add(axesHelper);
    
    // Animación de rotación
    function animate() {
      requestAnimationFrame(animate);
      cube.rotation.y += 0.005;
      renderer.render(scene, camera);
    }
    animate();
    
    // Responsive
    window.addEventListener('resize', function() {
      var w = container.clientWidth;
      var h = container.clientHeight;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    });
  }
});
</script>
```

---

## 📐 Geometrías Disponibles

### Cubo / Caja

```javascript
var geometry = new THREE.BoxGeometry(width, height, depth);
```

### Esfera

```javascript
var geometry = new THREE.SphereGeometry(radius, widthSegments, heightSegments);
```

### Cilindro

```javascript
var geometry = new THREE.CylinderGeometry(radiusTop, radiusBottom, height, radialSegments);
```

### Cono

```javascript
var geometry = new THREE.ConeGeometry(radius, height, radialSegments);
```

### Pirámide (usando BufferGeometry)

```javascript
// Pirámide de base cuadrada
var geometry = new THREE.BufferGeometry();
var vertices = new Float32Array([
  // Base
  -1, 0, -1,
   1, 0, -1,
   1, 0,  1,
  -1, 0,  1,
  // Ápice
   0, 2,  0
]);
// ... definir caras
```

---

## 🎨 Materiales

### Wireframe (solo aristas)

```javascript
var material = new THREE.MeshBasicMaterial({ 
  color: 0x3b82f6, 
  wireframe: true 
});
```

### Sólido con iluminación

```javascript
var material = new THREE.MeshPhongMaterial({ 
  color: 0x3b82f6,
  transparent: true,
  opacity: 0.7
});

// Requiere luz
var light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5, 5, 5);
scene.add(light);

var ambient = new THREE.AmbientLight(0x404040);
scene.add(ambient);
```

### Transparente

```javascript
var material = new THREE.MeshBasicMaterial({ 
  color: 0x3b82f6, 
  transparent: true,
  opacity: 0.5
});
```

---

## 🎨 Paleta de Colores

| Uso | Color | Hex (Three.js) |
|-----|-------|----------------|
| Figura principal | Azul | `0x3b82f6` |
| Figura secundaria | Rojo | `0xef4444` |
| Aristas | Gris oscuro | `0x374151` |
| Fondo | Gris claro | `0xf1f5f9` |

---

## 📐 Ejemplos

### Cubo con Diagonales

```javascript
// Cubo
var cubeGeom = new THREE.BoxGeometry(2, 2, 2);
var cubeMat = new THREE.MeshBasicMaterial({ color: 0x3b82f6, wireframe: true });
var cube = new THREE.Mesh(cubeGeom, cubeMat);
scene.add(cube);

// Diagonal espacial
var diagMat = new THREE.LineBasicMaterial({ color: 0xef4444 });
var diagPoints = [
  new THREE.Vector3(-1, -1, -1),
  new THREE.Vector3(1, 1, 1)
];
var diagGeom = new THREE.BufferGeometry().setFromPoints(diagPoints);
var diagonal = new THREE.Line(diagGeom, diagMat);
scene.add(diagonal);
```

### Prisma Triangular

```javascript
// Usar ExtrudeGeometry con forma triangular
var shape = new THREE.Shape();
shape.moveTo(0, 0);
shape.lineTo(2, 0);
shape.lineTo(1, 1.7);
shape.lineTo(0, 0);

var extrudeSettings = { depth: 3, bevelEnabled: false };
var geometry = new THREE.ExtrudeGeometry(shape, extrudeSettings);
```

---

## ✅ Checklist

- [ ] ID único: `threejs-[leccion]-[numero]`
- [ ] Wrapper con fondo `#f1f5f9`
- [ ] `DOMContentLoaded` wrapper
- [ ] Verificación: `if (typeof THREE !== 'undefined')`
- [ ] Cámara posicionada correctamente
- [ ] Ejes de referencia si ayuda a la comprensión
- [ ] Resize listener
- [ ] Animación suave (rotation.y += 0.005)

---

## ⚠️ Limitaciones

- **Complejidad alta**: Más propenso a errores que otras tecnologías
- **Performance**: Puede ser lento en dispositivos móviles
- **Debugging difícil**: Errores de geometría son difíciles de diagnosticar

**Recomendación:** Solo usar cuando el 3D añada valor pedagógico real.

---

## 🔗 Relacionados

- [GeometrySpec](./geometry-exact.md) - Para geometría 2D exacta
- [Rough.js](./roughjs.md) - Para diagramas 2D ilustrativos
- [Árbol de decisión](./illustration-decision.md)