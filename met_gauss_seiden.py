#metodo de Gauss-Seiden

#Extremos de x, y
a = int(input("Ingrese el valor de a, x0: "))
b = int(input("Ingrese el valor de b, xf: "))
c = int(input("Ingrese el valor de c, y0: "))
d = int(input("Ingrese el valor de d, yf: "))

#Número de huecos de x, y. Los elegimos nosotros
N = int(input("Ingrese el número de huecos de X: "))
M = int(input("Ingrese el número de huecos de Y: "))

#Tamaño de los huecos
h = (b-a)/N
k = (d-c)/M 

#Matriz
# Inicializar matriz w con dimensiones N x M
w = [[0 for j in range(M+1)] for i in range(N+1)]


#funcion
def f(x, y):
    return 0


#Creamos los bordes de la matriz
for i in range(1, N):
    #Cambian dependiendo del ejercicio
    #las x = (a+i*h)
    w[i][0] = 0
    w[i][M] = (a+i*h)**2

for j in range(1, M):
    #Cambian dependiendo del ejercicio
    #las y = (c+j*k)
    w[0][j] = 1-(c+k*j)**2
    w[N][j] = 1



#recorremos los puntos interiores de la malla
for o in range(100):#iteramos inicialmente 100, luego ya lo adapataremos
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = ( k**2 * (w[i+1][j] + w[i-1][j])+ h**2 * (w[i][j+1] + w[i][j-1]) - (h*k)**2 * f(i, j))/(2*(h**2 + k**2))
            
'''
Nos va a preguntar la interpretación gráfica de las EDP
El laplaciano minimiza la energía, es decir, el calor se va a ir a los bordes. 
Un ejemplo de esto es una lona estirada, donde al tensionar dandole una forma no horizontal, 
esta se quede da una forma que minimiza la energía. 
Eje1: Laplaciano, la A es la divergencia del gradiente, la A = gradiente ^2
Au = 0 0<x<1, 0<y<1
u(0,y) = u(x,0) = u(x,1) = 0
u(1,y) = 1

Eje2: Laplaciano, la A es el gradiente
Au = 0 0<x<1, 0<y<1 
u(x,0) = 0, u(x,1) = x**2
u(0,y) = 1-y**2, u(1,y) = 1

Eje3: Laplaciano, la A es el gradiente
Au = 2u 0<x<1, 0<y<1
u(0,y) = 0, u(1,y) = 1
u(x,0) = 0, u(x,1) = 0

#la u es la w 
'''

#Mostramos la grafica de la matriz
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#definir coordenadas
x = np.linspace(a, b, N+1)
y = np.linspace(c, d, M+1)
X, Y = np.meshgrid(x, y)
Z = np.array(w)

#graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

#etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#mostramos
plt.show()

