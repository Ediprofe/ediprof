# Estereoisomería

> **¿Pueden dos moléculas tener los mismos átomos conectados igual pero ser diferentes?** 🪞

¡Sí! La **estereoisomería** ocurre cuando las moléculas tienen la misma conectividad pero diferente **orientación en el espacio**. Es como tu mano izquierda y derecha: mismos dedos, pero no se superponen.

## 🎯 ¿Qué vas a aprender?

- La diferencia entre isomería geométrica y óptica
- Qué son los isómeros cis y trans
- Qué es un carbono quiral

---

## 📋 Resumen Rápido

| Tipo | Causa | Requisito | Ejemplo |
|------|-------|-----------|---------|
| **Geométrica (cis-trans)** | Rigidez del doble enlace | Doble enlace con 2 sustituyentes diferentes en cada C | cis-but-2-eno |
| **Óptica** | Carbono quiral | Un C con 4 sustituyentes diferentes | Ácido láctico |

---

## 📖 Isomería Geométrica (Cis-Trans)

### ¿Por qué ocurre?

El **doble enlace C=C** es rígido:
- El enlace π impide la rotación
- Los grupos quedan "congelados" en su posición
- Pueden estar del mismo lado (cis) o de lados opuestos (trans)

### Requisito

Para que exista isomería cis-trans, cada carbono del doble enlace debe tener **dos sustituyentes diferentes**.

```
    A       C          A y B son diferentes
     \     /           C y D son diferentes
      C = C            → SÍ hay isomería cis-trans
     /     \
    B       D
```

### Los isómeros cis y trans

**cis:** Los grupos "iguales" o "mayores" del **mismo lado**

```
    CH₃       CH₃
      \       /
       C  =  C
      /       \
     H         H
     
     cis-but-2-eno
```

**trans:** Los grupos "iguales" o "mayores" de **lados opuestos**

```
    CH₃       H
      \       /
       C  =  C
      /       \
     H        CH₃
     
     trans-but-2-eno
```

### Diferencias en propiedades

| Propiedad | cis-but-2-eno | trans-but-2-eno |
|-----------|---------------|-----------------|
| P. ebullición | 4°C | 1°C |
| P. fusión | -139°C | -106°C |
| Momento dipolar | Mayor | Menor |
| Estabilidad | Menor | Mayor |

> 💡 El isómero **trans** suele ser más estable porque hay menos repulsión entre los grupos grandes.

### Cuándo NO hay isomería cis-trans

```
    H         H          Ambos sustituyentes en C1 son iguales (H)
     \       /           → NO hay isomería cis-trans
      C  =  C
     /       \
   CH₃       CH₃
```

El propeno (CH₃-CH=CH₂) NO tiene isómeros cis-trans porque el C1 tiene dos H iguales.

---

## 📖 Nomenclatura E/Z

### El sistema moderno

Para casos complicados donde "cis" y "trans" no son claros, se usa el sistema **E/Z**:

- **Z** (zusammen = juntos, en alemán): Grupos de mayor prioridad del **mismo lado**
- **E** (entgegen = opuestos): Grupos de mayor prioridad de **lados opuestos**

### Reglas de prioridad (Cahn-Ingold-Prelog)

1. **Mayor número atómico = mayor prioridad**
   - I > Br > Cl > S > O > N > C > H
   
2. Si el primer átomo es igual, mira el **segundo**

### Ejemplo

```
    Cl        CH₃
      \       /
       C  =  C
      /       \
     H         H
```

En C1: Cl (Z=17) > H (Z=1) → Cl es prioritario
En C2: C (Z=6) > H (Z=1) → CH₃ es prioritario

Los grupos prioritarios (Cl y CH₃) están de lados opuestos → **E**

---

## 📖 Isomería Óptica

### ¿Qué es?

La isomería óptica ocurre cuando una molécula y su imagen especular **NO son superponibles** (como la mano izquierda y derecha).

### Carbono quiral

Un **carbono quiral** (o estereogénico) es un carbono unido a **4 sustituyentes diferentes**.

```
        a
        |
    d — C — b      Si a ≠ b ≠ c ≠ d
        |          → C es quiral
        c
```

### Ejemplo: Ácido láctico

```
        COOH
         |
   H — C — OH
         |
        CH₃
```

El carbono central tiene 4 grupos diferentes:
- COOH
- OH  
- H
- CH₃

→ Es un **carbono quiral**

### Enantiómeros

Los dos isómeros ópticos se llaman **enantiómeros**. Son imágenes especulares no superponibles.

```
    COOH          COOH
     |             |
H—C—OH        HO—C—H
     |             |
   CH₃           CH₃
   
    (R)           (S)
```

### Propiedades de los enantiómeros

| Propiedad | ¿Son iguales? |
|-----------|---------------|
| Punto de fusión | Sí |
| Punto de ebullición | Sí |
| Solubilidad | Sí |
| Rotación de luz polarizada | **No** (opuesta) |
| Actividad biológica | **No** (puede ser muy diferente) |

### Actividad óptica

Los enantiómeros rotan el plano de luz polarizada:
- **Dextrógiro (+):** Rota hacia la derecha
- **Levógiro (-):** Rota hacia la izquierda

### Nomenclatura R/S

Se usa el sistema Cahn-Ingold-Prelog:

1. Ordenar sustituyentes por prioridad (mayor número atómico primero)
2. Orientar la molécula con el grupo de menor prioridad hacia atrás
3. Recorrer los otros tres grupos en orden de prioridad:
   - Si el recorrido es **horario** → configuración **R** (rectus)
   - Si es **antihorario** → configuración **S** (sinister)

---

## 📖 Importancia Biológica

### Ejemplos en la naturaleza

| Compuesto | Isómero | Efecto |
|-----------|---------|--------|
| **Limoneno** | R-(+) | Olor a naranja |
| | S-(-) | Olor a limón |
| **Carvona** | R-(+) | Olor a menta verde |
| | S-(-) | Olor a alcaravea |
| **Glucosa** | D | Es la que usamos para energía |
| | L | No la metabolizamos |

### Fármacos

> ⚠️ **Caso talidomida:** Un enantiómero aliviaba náuseas del embarazo, el otro causaba malformaciones fetales. Hoy se exige conocer la actividad de cada enantiómero.

---

## 💡 Tips para recordar

> **"CIS = miSmo lado"** (la "i" de cis = "igual")
> **"TRANS = a TRAVés"** (lados opuestos)

> **"Carbono QUIRAL = 4 grupos DIFERENTES"**

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
¿Cuáles de las siguientes moléculas tienen isomería cis-trans?

a) CH₂=CH₂ (eteno)
b) CH₃-CH=CH-CH₃ (but-2-eno)
c) CH₂=CH-CH₃ (propeno)
d) CH₃-CH=CH-Cl (1-cloropropeno)

<details>
<summary>Ver solución</summary>

| Molécula | ¿Tiene cis-trans? | Razón |
|----------|-------------------|-------|
| a) CH₂=CH₂ | **No** | Ambos C tienen 2 H iguales |
| b) CH₃-CH=CH-CH₃ | **Sí** | Cada C tiene H y CH₃ (diferentes) |
| c) CH₂=CH-CH₃ | **No** | C1 tiene dos H iguales |
| d) CH₃-CH=CH-Cl | **Sí** | C tiene H y CH₃; otro C tiene H y Cl |

</details>

---

### Ejercicio 2
Dibuja los isómeros cis y trans del 1,2-dicloroeteno.

<details>
<summary>Ver solución</summary>

**cis-1,2-dicloroeteno:**
```
    Cl        Cl
      \      /
       C = C
      /      \
     H        H
     
Los dos Cl del mismo lado
```

**trans-1,2-dicloroeteno:**
```
    Cl        H
      \      /
       C = C
      /      \
     H        Cl
     
Los dos Cl de lados opuestos
```

</details>

---

### Ejercicio 3
Identifica el carbono quiral (si existe) en:

a) CH₃-CH₂-OH (etanol)
b) CH₃-CHOH-CH₃ (propan-2-ol)
c) CH₃-CHOH-COOH (ácido láctico)

<details>
<summary>Ver solución</summary>

| Molécula | ¿Carbono quiral? | Razón |
|----------|------------------|-------|
| a) Etanol | **No** | Ningún C tiene 4 grupos diferentes |
| b) Propan-2-ol | **No** | El C central tiene 2 grupos CH₃ iguales |
| c) Ácido láctico | **Sí** | El C central tiene: H, OH, CH₃, COOH (todos diferentes) |

</details>

---

### Ejercicio 4
¿Por qué es importante en farmacología conocer la estereoquímica de un medicamento?

<details>
<summary>Ver solución</summary>

Es importante porque los **enantiómeros pueden tener efectos biológicos muy diferentes**:

1. **Receptores biológicos son quirales:** Las enzimas y receptores distinguen entre enantiómeros

2. **Efectos posibles:**
   | Enantiómero A | Enantiómero B |
   |---------------|---------------|
   | Activo (terapéutico) | Inactivo |
   | Activo | Tóxico |
   | Activo | Menos activo |

3. **Ejemplos:**
   - Ibuprofeno: solo el S es activo
   - Talidomida: uno curaba, otro causaba malformaciones
   - Omeprazol: uno es 10x más activo que el otro

4. **Por eso:** Hoy en día, los medicamentos quirales deben ser estudiados como mezclas racémicas O producidos como enantiómero puro.

</details>
