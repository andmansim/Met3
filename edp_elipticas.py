#metodo de Gauss-Seiden
#Diferencias regresivas (un metodo de diferencias finitas)
import numpy as np
#Extremos de x, y
a = int(input("Ingrese el valor de a, x0: "))
b = int(input("Ingrese el valor de b, xf: "))
c = int(input("Ingrese el valor de c, y0: "))
d = int(input("Ingrese el valor de d, yf: "))

#Número de huecos de x, y. Los elegimos nosotros
N = int(input("Ingrese el número de huecos de X: "))
M = int(input("Ingrese el número de huecos de Y: "))

b = np.pi
d = np.pi
#Tamaño de los huecos
h = (b-a)/N
k = (d-c)/M 

#Matriz
# Inicializar matriz w con dimensiones N x M
w = np.zeros((N + 1, M + 1))


#funcion
def f(i, j):
    #las x = (a+i*h)
    #las y = (c+j*k)
    return 0

#Creamos los bordes de la matriz
for i in range(1, N):
    #Cambian dependiendo del ejercicio
    #las x = (a+i*h)
    w[i][0] = 0
    w[i][M] = 0

for j in range(1, M):
    #Cambian dependiendo del ejercicio
    #las y = (c+j*k)
    w[0][j] = (c+j*k)
    w[N][j] = (c+j*k)



#recorremos los puntos interiores de la malla
for o in range(100):#iteramos inicialmente 100, luego ya lo adapataremos
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = ( k**2 * (w[i+1][j] + w[i-1][j])+ h**2 * (w[i][j+1] + w[i][j-1]) - (h*k)**2 * f(i, j))/(2*(h**2 + k**2))
            

#Mostramos la grafica de la matriz
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#definir coordenadas
x = np.linspace(a, b, N+1)
y = np.linspace(c, d, M+1)
X, Y = np.meshgrid(x, y)


#graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, w.T, cmap='viridis')

#etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#mostramos
plt.show()

'''
Nos va a preguntar la interpretación gráfica de las EDP
El laplaciano minimiza la energía, es decir, el calor se va a ir a los bordes. 
Un ejemplo de esto es una lona estirada, donde al tensionar dandole una forma no horizontal, 
esta se quede da una forma que minimiza la energía. 
Las series de fourier extendienden la solución, hay que tener cuidadito. 

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
Eje 4: Ecuación de Poisson
Au = xy(1-x)(1-y) 0<x<1, 0<y<1
u(0,y) = 0, u(1,y) = 0
u(x,0) = 0, u(x,1) = 0

Eje5: Laplaciano
Au = 0 0<x<pi, 0<y<pi
u(0,y) = 0, u(pi,y) = 0
u(x,0) = y, u(x,pi) = y

'''
