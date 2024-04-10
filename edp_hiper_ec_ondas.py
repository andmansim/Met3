#Edp eliptica
#Diferencias progresivas (diferencias finitas)
#Ec de Ondas
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Extremos de x, y
a = 0
b = int(input("Ingrese el valor de b, xf: ")) 
c = 0 
d = int(input("Ingrese el valor de d, tf: "))

#Número de huecos de x, y. Los elegimos nosotros
#Se puede poner 400 en uno y que no sean iguales
N = int(input("Ingrese el número de huecos de X: "))
M = int(input("Ingrese el número de huecos de T: "))

#velocidad
v = float(input("Ingrese la velocidad: "))


#Tamaño de los huecos
h = (b - a) / N
k = (d - c) / M 
p = (v * k) / h #para no escribir todo esto abajo

#Matriz
# Inicializar matriz w con dimensiones N x M
w = np.zeros((N + 1, M + 1))


#funcion inicial y de frontera
def f(x):
    #Cambia dependiendo del ejercicio
    #x = (a+i*h)
    dreturn 10*x*(5-x)


def g(x):  
    #Cambia dependiendo del ejercicio
    return (250/4) - 10*x*(5-x)
    

#Creamos los bordes de la matriz
for i in range(1, N):
    #Cambian dependiendo del ejercicio
    w[i][0] = f(a + i*h)
    w[i][M] = w[i][0] + k*g(a + h*i)

for j in range(1, M):
    #Cambian dependiendo del ejercicio
    w[0][j] = 0
    w[N][j] = 0



#recorremos los puntos interiores de la malla

for j in range(1, M):
    for i in range(1, N):
            w[i][j+1] = 2 *(1 - p**2) * w[i][j] + (p**2)*(w[i + 1][j] + w[i - 1][j]) - w[i][j-1]
            
        


#Mostramos la grafica de la matriz
#definir coordenadas
x = np.linspace(a, b, N + 1)
y = np.linspace(b, d, M + 1)
X, Y = np.meshgrid(x, y)


#graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, w.T, cmap='viridis') #el .T es para que se adapte a los valores

#etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#mostramos
plt.show()

'''
hay una velocidad máxima, donde es h/k a partir de esta velocidad el método no es estable
Siempre hay que calcularla para no pasarnos de ella

Ec de ondas

Si no nos pone las condiciones iniciales ni de contorno --> se quedan como están
Eje1: 
    f(x) = x(b-x)
    g(x) = 0
    b=5, d = 10, v=0.5, N=40, M=400 

Eje2:
    f(x) = x     x < b/2
    f(x) = b-x   x > b/2
    g(x) = 0

Eje3:
    g(x) = sen(x) b = pi
    f(x) = 0

Eje4:
    g(x)= 0
    f(x) = X[1,3] = 0   distinto de [1, 3]
                    1   1 <= x <= 3 
    b = 6, d = 24, N = 600, M = 2400 v = 0.5
    Las ondas se propagan siguiendo x = -vt, x = vt

Eje5:
    Queremos formar ondas no estacionarias
    f(x) = 0
    g(x) = 0
    w[0][j] = 3*sin(k*j) 
'''
