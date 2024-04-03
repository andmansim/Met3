# Met3
https://github.com/andmansim/Met3.git

REVISAR APUNTES ESTOS Y MIRAR CON EJES HECHOS EN EL CUARDERNO

En el examen tenemos que hacer todos los pasos. Él nos dice si es regresivo o progresivo, pero nosotros lo ponemos en función de w y despejamos el q toque. 
Regresivo despejamps wij (Gauss-Seidel)
Progresivo despejamos wij+1 (Evolución o Gauss)
No tenemos en cuenta el error. 

Siempre que sea regresiva se hace como si fuese lineal, es decir, al pasar todo a w, podemos tratar como un sistema lineal, donde se despeja la wij o despejamos la wij+1. 
Met de Gauss-Seidel es despejar el wij, iteramos el sistema lineal. 
Evolución es cuando despejamos wij+1

Si no dice nada por el met que queramos, si hay dos opciones el nos puede indicar una. 
Hay que explicar que pasa según lo que nos salga. 
Nos puede pedir las caractirísticas de la EDP, o indicar que características está siguiendo. 
Evolucion para las hiperbólicas y algunas parabólicas

Un prog de evolución no necesita datod de contorno en toda la región, en el caso de los otros si necesitamos datos de contorno en toda la región. Por eso en las elipticas hay más datos de contorno. 
El paso 2 de las aproximaciones nos lo tenemos que aprender en cierta manera para después sustituir. 
Siempre que en la edp haya una derivada parcial podemos hacer dif regresivas o progresivas. 

Las segundas derivadas son siempre el mismo cociente en las primeras no, estas cambian. 
Progresiva, cogemos el valor a posteriori. No hace falta aplicar gauss seidel dado que calculamos el punto posterior en función de los anteriores, no hace falta iterar. (Cuando iteremaos es cuando tenemos 3 for en la zona de las wij). 
Regresiva, las usamos para cambiar la edp donde aprox lo que vale la solu pero en j-1, donde aquí cambia un poco dado que ahora vamos hacia atrás. No tenemos ningún punto posterior dado que obtenemos 3 en un mismo timpo temporal --> se resuelve todo con gauss seidel, iterando y convergiendo la solución cada vez que lo hacemos. Todo esto es un sist lineal donde el punto central de la dig prin es el ij 
En este caso el paso 2 cambia. 

Después de plantear la ec discretizada hemos visto dos met en hiperbolicas. 
La matriz del met de gauss la sacamos de las ecuaciones. Tenemos una incognita y ec. para cada punto de la malla donde cada una es distinta pq los subindices son distintos. Todas las ec son lineales. 

Met de gauss es despejar la coord principal en funcion de las otras, lo de seidel es iterar usando las más recientes. 

Diferencias finitas progresivas:

Si se despeja el valor en el punto siguiente (wij+1) en función de los valores anteriores, se denomina método de diferencias finitas progresivas.
Este enfoque se utiliza en problemas donde la solución en un punto depende de los valores previos, común en ecuaciones de tipo evolutivo como las ecuaciones de ondas.
Diferencias finitas regresivas:

Cuando se despeja el valor en el punto anterior (wij-1) en función de los valores posteriores, se trata de un método de diferencias finitas regresivas.
Este método se emplea en problemas donde la solución en un punto depende de los valores futuros, por ejemplo, en ciertos casos de ecuaciones evolutivas.
Método de Gauss-Seidel:

En el método de Gauss-Seidel, se actualiza el valor actual (wij) utilizando los valores anteriores y posteriores en un proceso iterativo para converger hacia la solución.
Este método se aplica en la resolución de sistemas de ecuaciones lineales en problemas estacionarios como la ecuación de Poisson.

# Examen 10/04/2024
EN el control 10/04/2024 discretizamos, cambiamos derivadas, saber cómo resolverlo si como GS o ec Evolución, progreamarlo y resolverlo. LE mandaremos el prog y la imagen. 

# Discretizar en hiperbólicas
aplicamos el polinomio de Taylor en varios puntos, (i+1, j+1), (i+1, j-1), (i-1, j-1), (i-1, j+1). Después lo que hacemos es sumar todas las ecuaciones que obteníamos para obtener la derivada cruzada sola y sin nada más. No hace falta hacer el proceso entero, con aprenderse la fórmula final vale. 
Después sustituimos la derivada cruzada en la edp y transformamos las cosas en w, después lo hacemos por gauss-seidel, no se puede hacer de evolución --> no es progresiva. Dado que calculamos puntos en un entorno cerrado. 
