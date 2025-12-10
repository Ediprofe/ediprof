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

#### Tener en cuenta

Para la elaboración de la lecciones, ten en cuenta que el una MATERIA > CAPITULO > TEMAS > LECCIÓN, y que en cada lección se abordan diferentes conceptos, los cuales quiero que los trabajes progresivamente, uno a uno, cosa que si empiezas uno, lo explicas por su definición o introducción, luego haces un par de ejemplos de ese concepto (o más si ves que es algo muy fácil, tipo identificar los elementos en una expresión algebraica), luego pasas al otro concepto dentro de esa lección, y luego haces un par de ejemplos de ese concepto, y luego pasas al siguiente concepto, y así sucesivamente. La idea es que al final cierres con una sección tipo, 2 ejercicios por concepto en una nueva sección de esa lección que se llame tipo "Ejercicios de práctica" o "Ejercicios para practicar", o el nombre que más adecuado encuentres.


## Solicitud concreta

Te voy pasando el link de la lección en cuestión, y a partir de ahí te paso la solicitud concreta.

http://localhost:4321/matematicas/algebra/monomios-y-polinomios/operaciones-con-polinomios
En la multiplicación de polinimoios, ejemplo 12, elimina eso de la multiplicación vertical, y más bien explica el ejercicio como venías trabajando los demás.

En esta misma lección, hay una sección que se llama "Sacar Factor Común"....Quiero que la omitas, ya que la parte de factor común y demás se explica en la lección de factor común, correspondiente al tema de factorización. Ten cuidado porque en esta lección hay una sección que se llama "Potencia de unu polinomio", y esa sí quiera que la conserves.

http://localhost:4321/matematicas/algebra/monomios-y-polinomios/division-de-polinomios
En la división de polinomios, la sección llamada "División de un polinomio entre un monomio", quiero que des tres ejemplos más. De igual manera, en la sección llamada "División de polinomios (método clásico)", quiero que des dos ejemplos más. En la sección llamada "Regla de Ruffini", quiero que des 1 ejemplos más. En la sección llamada "Teorema del Resto", quiero que des tres ejemplo más. Y en la sección llamada "Ejercicios de práctica", quiero que des en total 5 ejercicios por cada sección.

IMPORTANTE: EN GENERAL QUIERO QUE PARA TODO EL TEMA DE ÁLGEBRA (http://localhost:4321/matematicas/algebra) QUE MANEJAS LA IDEA DE QUE CADA LECCIÓN (DENTRO DE UN TEMA, DENTRO DE UN CAPÍTULO, DENTRO DE UN MATERIA) SE TRABAJE CON 5 EJEMPLOS, COMO TE LA ACABÉ DE SOLICITAR. Y QUE POR FAVOR CUANDO REDACTES AL FINAL LOS EJERCICIOS DE PRÁCTICA, PROPONGAS 5 EJERCICIOS POR SECCIÓN DE ESA LECCIÓN. PERO LÓGICAMENTE HABRÁN CASOS ESPECIALES COMO POR EJEMPLO ESA INTRODUCCIÓN A LOS MONOMIOS DONDE TOCA IDENTIFICAR TÉRMINOS Y ESAS COSAS, DONDE ES TAN SENCILLO QUE SE PRESTA PARA HACER MÁS EJERCICIOS, COMO DE HECHO YA LO IMPLEMENTASTE.

EN EL TEMA DE LOS PRODUCTOS NOTABLES (http://localhost:4321/matematicas/algebra/productos-notables), la lección de introducción (http://localhost:4321/matematicas/algebra/productos-notables/introduccion-cuadrado-binomio), QUIERO QUE DES DE UNA VEZ UN TIPO RESUMEN DE LOS PRODUCTOS NOTABLES QUE VEREMOS, COMO PARA TENERLO EN LA INTRODUCCIÓN, Y DE UNA VEZ PROCEDAS CON EL TEMA EN SÍ MISMO, O PRIMER PRODUCTO NOTABLE, TAL COMO LO TIENES.

En la lección "Introducción" del tema "Factorización" (http://localhost:4321/matematicas/algebra/factorizacion/introduccion), ![alt text](image-1.png), quiero que esa parte del resumen de casos de factorización lodes ahí en el princpio. Pero sin dar ejemplos miscelaneos de una vez, ya que eso confunde. Mejor deja esa tabla resumen ahí en la introducción, sin más, solo para que quede fácil de encontrar al inicio del tema, y además, la dejas en una lección, la cual debes crear, llamada tipo "Resumen de casos de factorización" o algo así. ESE RESUMEN DE CASOS DE FACTORIZACIÓN POR FAVOR PONLO COMO UNA LECCIÓN ANTES DE HABLAR DE CASOS ESPECIALES DE FACTORIZACIÓN (http://localhost:4321/matematicas/algebra/factorizacion/casos-especiales).



http://localhost:4321/matematicas/algebra/productos-notables/binomios-conjugados
COMO INTRODUCIR RACIONALIZACIÓN