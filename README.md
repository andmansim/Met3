# Met3
https://github.com/andmansim/Met3.git

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

Después de plantear la ec discretizada hemos visto dos met en hiperbolicas, 