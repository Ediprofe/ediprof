# CONTEXTO DEL PROYECTO


## Contexto general

### Tu rol
Me estás ayudando a generar las lecciones de clase que son archivos .md que se renderizan en mi página web. o puedes bien, tomar el rol de planeador docente para ayudarme a estructurar el árbol de carpetas y archivos .md que se van a generar. Así las cosas, tu rol puede ser dependiendo lo que te solicite, de generador de contenidos (lecciones .md), o de planeador docente (árbol de carpetas y archivos .md).

### Estamos en fase de cliente docente
Ten en cuenta que ahora mismo estamos en plan no de programador del sitio sino de cliente docente que se encarga de generar los contenidos para la página web. Estos contenidos son cargados dentro de la carpeta src/content/.

### Estructura de carpetas y archivos
La carpeta src/content/ tiene unas materias, las cuales son matemáticas, física, química y ciencias. Cada materia tiene capítulos, cada capítulo tiene temas, y cada tema tiene lecciones. De modo que la división de carpetas y archivos sigue esta estructura, haciendo la claridad que cada archivo .md corresponde a una lección.

### Para la generación de las lecciones

#### Estilo de las lecciones

Fíjate por ejemplo en el estilo que manejan mis lecciones en la carpeta src/content/matematicas/01-aritmetica/05-proporcionalidad/03-regla-de-tres-simple.md, es decir, con un estilo sencillo, fácilmente entendible, progresivo, que trabaja una idea por vez, y la pone en práctica con ejemplos, y luego ahí sí trabaja con otra idea o subsección dentro de la misma lección.

#### Expresiones con latex
Ten en cuenta que estoy usando kathex para renderizar los archivos .md, por lo que las ecuaciones en bloque son del tipo

$$

$$

Las ecuaciones inline son del tipo $, al igual que las ecuaciones en tabla.

Esto es importante para que las ecuaciones se rendericen correctamente. No usar expresiones del tipo [] o () para las ecuaciones. Guíate de las expresiones que se usan en los archivos .md existentes, por ejemplo en la carpeta src/content/matematicas/01-aritmetica/02-teoria-de-numeros, o en la carpeta src/content/fisica/02-cinematica/02-escalares-y-vectores, por dar un ejemplo.

Por favor, en los títulos de cada sección de una lección, no les metas código de latex, ya que se renderiza mal (latex crudo), tanto en la tabla de contenidos como en la barra de navegación lateral. Así que por favor tenlo en cuenta.

#### Tener en cuenta

Para la elaboración de la lecciones, ten en cuenta que el una MATERIA > CAPITULO > TEMAS > LECCIÓN, y que en cada lección se abordan diferentes conceptos, los cuales quiero que los trabajes progresivamente, uno a uno, cosa que si empiezas uno, lo explicas por su definición o introducción, luego haces un par de ejemplos de ese concepto (o más si ves que es algo muy fácil, tipo identificar los elementos en una expresión algebraica), luego pasas al otro concepto dentro de esa lección, y luego haces un par de ejemplos de ese concepto, y luego pasas al siguiente concepto, y así sucesivamente. La idea es que al final cierres con una sección tipo, 2 ejercicios por concepto en una nueva sección de esa lección que se llame tipo "Ejercicios de práctica" o "Ejercicios para practicar", o el nombre que más adecuado encuentres.


## Solicitud concreta

Genera las lecciones correspondientes a ls siguientes temas. POR FAVOR NO GENERES TODAVÍA GRÁFICOS O ILUSTRACIONES QUE TÚ CONSIDERES NECESITEN EL USO DE LAS LIBRERIAS INSTALADAS chart.js o jsxgraph, ya que estos gráficos serán añadidos una vez tengamos las lecciones que tú generes aprobadas. Sin embargo, sí quiero que hagas alusión a estos gráficos, pero sin todavía generarlos, a menos que sean represnetaciones que te baste generar con código markdown..

GENERA TAMBIÉN LOS _meta.json que correspondan, asimismo como se generaron en lecciones anteriores de otros temas, por ejemplo de este mismo capitulo (ALGEBRA)

### TEMA 5: FRACCIONES ALGEBRAICAS

#### LECCIÓN 1: Máximo común divisor (MCD)

#### LECCIÓN 2: Mínimo común múltiplo (MCM)

#### LECCIÓN 3: Simplificación de fracciones algebraicas

#### LECCIÓN 4: Suma y resta de fracciones con denominador común

#### LECCIÓN 5: Suma y resta de fracciones con denominadores diferentes

#### LECCIÓN 6: Multiplicación de fracciones algebraicas

#### LECCIÓN 7: División de fracciones algebraicas

#### LECCIÓN 8: Combinación de operaciones con fracciones

#### LECCIÓN 9: Fracciones complejas

### TEMA 6: POTENCIACIÓN

#### LECCIÓN 1: Introducción

#### LECCIÓN 2: Propiedades de las potencias (I)

#### LECCIÓN 3: Propiedades de las potencias (II)

#### LECCIÓN 4: Propiedades de las potencias (III)

#### LECCIÓN 5: Simplificación de potencias

#### LECCIÓN 6: Facotrial de un número

#### LECCIÓN 7: Binomio de Newton

#### LECCIÓN 8: Triángulo de Pascal

### TEMA 7: RADICACIÓN

#### LECCIÓN 1: Introducción

#### LECCIÓN 2: Propiedades de los radicales (I)

#### LECCIÓN 3: Propiedades de los radicales (II)

#### LECCIÓN 4: Simplificación de radicales

#### LECCIÓN 5: Introducción de factores

#### LECCIÓN 6: Suma y resta de radicales

#### LECCIÓN 7: Multiplicación de radicales

#### LECCIÓN 8: División de radicales

#### LECCIÓN 9: Racionalización


### TEMA 8: NÚMEROS COMPLEJOS

#### LECCIÓN 1: Introducción
Hablar acá sobre números imaginarios, con una situación del mundo real, donde se vea el sentido de los números imaginarios, y lo demás que consideres. Introduce los números imaginarios luego también con la o las definiciones que correspondan, manteniendo total coherencia con las demas lecciones de este mismo tema, para que no haya solapamiento de temas, a no ser que se quiera hacer un repaso.

#### LECCIÓN 2: Sumando y restando números imaginarios

#### LECCIÓN 3: Potencias de i

#### LECCIÓN 4: Multiplicación y división de números imaginarios

#### LECCIÓN 5: Números complejos

#### LECCIÓN 6: Suma y resta de números complejos

#### LECCIÓN 7: Multiplicación de un complejo por un escalar

#### LECCIÓN 8: Multiplicación de números compplejos

#### LECCIÓN 9: División de números complejos

#### LECCIÓN 10: Representación de números complejos en el plano

#### LECCIÓN 11: Módulo de un complejo

#### LECCIÓN 12: Conjugado de un complejo


### TEMA 9: FUNCIONES LINEALES

#### LECCIÓN 1: Introducción
Hablar sobre la importancia de las funciones lineales y su aplicación en la vida cotidiana. Dar un abrebocas del tema.

#### LECCIÓN 2: Plano cartesiano
Hablar sobre el plano cartesiano y la localización de puntos en el plano.

#### LECCIÓN 3: Función lineal
Introducir el tema de manera práctica, con ejemplos de la experiencia cotidiana,para luego hablar de definiciones o conceptos introductorios, con todos sus elementos.

Hablar de la pendiente, el intercepto y la ecuación de la recta. En cuanto a la pendiente, de si es negativo o es positiva o es cero, y en cuanto al intercepto, de si es negativo o es positivo o es cero. Aprovechar e incluir en esta sección de manera didáctica y efectiva, el caso de función constante. 

TEN EN CUENTA QUE LO QUE VA EN ESTA LECCIÓN CONFORMA UN SOLO TEMA CON LAS DEMÁS LECCIONES DE ESTE MISMO TEMA, PARA QUE NO HAY SOLAPAMIENTO DE TEMAS, A NO SER QUE SE QUIERA HACER UN REPASO. TEN EN CUENTA QUE EN ESTE CAPÍTULO DE ÁLGEBRA, SE ESTÁ HABLANDO DE FUNCIONES HASTA EL PUNTO NECESARIO PARA COMPRENDER LO DE ECUACIONES, Y OTROS TEMAS QUE NECECITAN DE ESTE CONTEXTO, RAZÓN POR LA CUAL TE PIDO NO EXTENDERTE HACIA TEMAS COMO FUNCION INYECTIVA, HALLAR DOMINIOS APLICANDO DESIGUALDADES, NI HABLAR DE FUNCIONES TRASCENDENTES, NI HABLAR DE FUNCIONES INVERSA, YA QUE ESTOS OTROS TEMAS SE HABLARÁN EN DETALLE EN OTROS CAPÍTULOS.

#### LECCIÓN 4: Representación gráfica de funciones lineales

#### LECCIÓN 5: Rectas paralelas y perpendiculares

#### LECCIÓN 6: Resolución de problemas


### TEMA 10: ECUACIONES LINEALES

#### LECCIÓN 1: Introducción
Qué es una igualdad, qué es una ecuación, qué es despejar una ecuación, muchos ejemplos con el despeje de ecuaciones, muchos ejemplos también de identificar si la ecuación es lineal o no.

#### LECCIÓN 2: Ecuaciones lineales con una incógnita

#### LECCIÓN 3: Ecuaciones lineales con agrupación de signos y productos

#### LECCIÓN 4: Ecuaciones lineales con fracciones algebraicas

#### LECCIÓN 5: Ecuaciones lineales con valor absoluto

#### LECCIÓN 6: Ecuaciones lineales con literales

#### LECCIÓN 7: Despeje de fórmulas

### TEMA 11: SISTEMAS DE ECUACIONES LINEALES
#### LECCIÓN 1: Introducción
Hablar sobre la importancia de los sistemas de ecuaciones y su aplicación en la vida cotidiana. Dar un abrebocas del tema, con una aplicación práctica, donde se vea el sentido de los sistemas de ecuaciones.

#### LECCIÓN 2: Ecuación lineal
Tener en cuenta hablar aquí sobr ela gráfica de la ecuación linea, y lo demás que consideres.

#### LECCIÓN 3: Sistema de dos ecuaciones lineales con dos variables
Introducir el tema con una situación del mundo real, donde se vea el sentido de los sistemas de ecuaciones. También ten en cuenta que esta lección debe estar en total coherencia con las demas lecciones de este mismo tema, para que no haya solapamiento de temas, a no ser que se quiera hacer un repaso.

#### LECCIÓN 4: Sistema 2x2 por método gráfico

#### LECCIÓN 5: Sistema 2x2 por sustitución

#### LECCIÓN 6: Sistema 2x2 por igualación

#### LECCIÓN 7: Sistema 2x2 por eliminación

#### LECCIÓN 8: Sistema 2x2 por determinantes

#### LECCIÓN 8: Resolución de problemas

#### LECCIÓN 9: Sistemas de ecuaciones lineales con tres variables

#### LECCIÓN 10: Sistema 3x3 por eliminación

#### LECCIÓN 11: Sistema 3x3 por determinantes

#### LECCIÓN 12: Resolución de problemas

### TEMA 12: FUNCIONES Y ECUACIONES CUADRÁTICAS
### LECCIÓN 1: Introducción
Introducir el tema de manera práctica, con ejemplos de la experiencia cotidiana,para luego hablar de definiciones o conceptos introductorios, con todos sus elementos.

Gráfica de una función cuadrática, sus elementos: dominio, rango, simetría, eje de simetría, interceptos con los ejes, vértice.

TEN EN CUENTA QUE LO QUE VA EN ESTA LECCIÓN CONFORMA UN SOLO TEMA CON LAS DEMÁS LECCIONES DE ESTE MISMO TEMA, PARA QUE NO HAYa SOLAPAMIENTO DE TEMAS, A NO SER QUE SE QUIERA HACER UN REPASO. TEN EN CUENTA QUE EN ESTE CAPÍTULO DE ÁLGEBRA, SE ESTÁ HABLANDO DE FUNCIONES HASTA EL PUNTO NECESARIO PARA COMPRENDER LO DE ECUACIONES, Y OTROS TEMAS QUE NECECITAN DE ESTE CONTEXTO, RAZÓN POR LA CUAL TE PIDO NO EXTENDERTE HACIA TEMAS COMO FUNCION INYECTIVA, HALLAR DOMINIOS APLICANDO DESIGUALDADES, NI HABLAR DE FUNCIONES TRASCENDENTES, NI HABLAR DE FUNCIONES INVERSAS, YA QUE ESTOS OTROS TEMAS SE HABLARÁN EN DETALLE EN OTROS CAPÍTULOS.

### LECCIÓN 2: Tipos de funciones cuadráticas
Según los valores a, b y c en la expresión y = ax2 + bx + c. 

### LECCIÓN 3: CEROS DE UNA FUNCIÓN CUADRÁTICA

Caso 1: La parábola corta al eje x en un punto.
Caso 2: La parábola corta al eje x en dos puntos.
Caso 3: La parábola no corta al eje x.

### LECCIÓN 4: ECUACIÓN CUADRÁTICA
Conceptos generales y definiciones introductorias.
Ecuaciones incompletas y completas

### LECCIÓN 5: SOLUCIÓN DE ECUACIONES CUADRÁTICAS
Qué es resolver una ecuación cuadrática
Solución de ecuaciones cuadráticas incompletas
Solución de ecuaciones cuadráticas completas
Tener en cuenta que las soluciones de ecuaciones cuadráticas comnpletas sea resuelve por factorización, por completación de cuadrados y por fórmula general.

### LECCIÓN 6: TIPOS DE SOLUCIONES DE UNA ECUACIÓN CUADRÁTICA

### LECCIÓN 7: ECUACIONES REDUCIBLES A CUADRÁTICAS

### LECCIÓN 8: PROBLEMAS DE APLICACIÓN

### TEMA 13: FUNCIONES EXPONENCIALES Y LOGARÍTMICAS

#### LECCIÓN 1: Función exponencial
Introducir el tema de manera práctica, con ejemplos de la experiencia cotidiana,para luego hablar de definiciones o conceptos introductorios, con todos sus elementos.

Función exponencial, sus características, hablar de dominio, rango, asíntotas...en fin, lo que vaya acá. Gráfica...y luego una tabla resumen con las propiedades de los exponentes.

TEN EN CUENTA QUE LO QUE VA EN ESTA LECCIÓN CONFORMA UN SOLO TEMA CON LAS DEMÁS LECCIONES DE ESTE MISMO TEMA, PARA QUE NO HAYA SOLAPAMIENTO DE TEMAS, A NO SER QUE SE QUIERA HACER UN REPASO. TEN EN CUENTA QUE EN ESTE CAPÍTULO DE ÁLGEBRA, SE ESTÁ HABLANDO DE FUNCIONES HASTA EL PUNTO NECESARIO PARA COMPRENDER LO DE ECUACIONES, Y OTROS TEMAS QUE NECECITAN DE ESTE CONTEXTO, RAZÓN POR LA CUAL TE PIDO NO EXTENDERTE HACIA TEMAS COMO FUNCION INYECTIVA, HALLAR DOMINIOS APLICANDO DESIGUALDADES, NI HABLAR DE FUNCIONES TRASCENDENTES, NI HABLAR DE FUNCIONES INVERSAS, YA QUE ESTOS OTROS TEMAS SE HABLARÁN EN DETALLE EN OTROS CAPÍTULOS.

#### LECCIÓN 2: Función logarítmica
Introducir el tema de manera práctica, con ejemplos de la experiencia cotidiana,para luego hablar de definiciones o conceptos introductorios, con todos sus elementos.

Función logarítmica, sus características..lo que corresponda acá...la gráfica y todo eso... luego una tabla resumen con las propiedades de los logaritmos.

TEN EN CUENTA QUE LO QUE VA EN ESTA LECCIÓN CONFORMA UN SOLO TEMA CON LAS DEMÁS LECCIONES DE ESTE MISMO TEMA, PARA QUE NO HAYA SOLAPAMIENTO DE TEMAS, A NO SER QUE SE QUIERA HACER UN REPASO. TEN EN CUENTA QUE EN ESTE CAPÍTULO DE ÁLGEBRA, SE ESTÁ HABLANDO DE FUNCIONES HASTA EL PUNTO NECESARIO PARA COMPRENDER LO DE ECUACIONES, Y OTROS TEMAS QUE NECECITAN DE ESTE CONTEXTO, RAZÓN POR LA CUAL TE PIDO NO EXTENDERTE HACIA TEMAS COMO FUNCION INYECTIVA, HALLAR DOMINIOS APLICANDO DESIGUALDADES, NI HABLAR DE FUNCIONES TRASCENDENTES, NI HABLAR DE FUNCIONES INVERSAS, YA QUE ESTOS OTROS TEMAS SE HABLARÁN EN DETALLE EN OTROS CAPÍTULOS.

#### LECCIÓN 3: Ecuaciones exponenciales y logarítmicas


### TEMA 14: PROGRESIONES

#### LECCIÓN 1: Introducción
Introducir el tema de manera práctica, con ejemplos de la experiencia cotidiana,para luego hablar de definiciones o conceptos introductorios, como qué es una sucesión, qué es una serie, qué es una progresión y esas cosas...

#### LECCIÓN 2: Progresión aritmética
Introduce apropiadamente.
Término general, primer término, diferencia común, número de términos, suma de los primeros términos, interpolación de medios aritméticos. Media aritmética o promedio aritmético.

### LECCIÓN 3: Progresión geométrica
Introduce apropiadamente.
Término general, primer término, razón, número de términos, suma de los primeros términos, interpolación de medios geométricos, progresión geométrica infinita, interés compuesto, depreciación.



# RETROALIMENTACIÓN

AL FINAL DE ESTA LECCIÓN http://localhost:4321/matematicas/algebra/ecuaciones-lineales/despeje-ecuaciones, QUIERO QUE LE INTEGRES LO DE ESTA LECCIÓN http://localhost:4321/matematicas/algebra/ecuaciones-lineales/despeje-formulas

y ELIMINAS LA LECCIÓN INTEGRADA (http://localhost:4321/matematicas/algebra/ecuaciones-lineales/despeje-formulas)
