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
v = float(input("Ingrese la conductividad: "))


#Tamaño de los huecos
h = (b - a) / N
k = (d - c) / M 


#Matriz
# Inicializar matriz w con dimensiones N x M
w = np.zeros((N + 1, M + 1))


#funcion inicial y de frontera
def f(x):
    #Cambia dependiendo del ejercicio
    #x = (a+i*h)
    return 0


#Creamos los bordes de la matriz
for i in range(1, N):
    #Cambian dependiendo del ejercicio
    w[i][0] = f(a + h*i)
    w[i][1] = 0

for j in range(1, M):
    #Cambian dependiendo del ejercicio
    w[0][j] = 0
    w[N][j] = 0



#recorremos los puntos interiores de la malla

for j in range(1, M):
    for i in range(1, N):
            w[i][j+1] = (1-2*k*v**2/h**2)*w[i][j] + (k*v**2/h**2)*(w[i+1][j] + w[i-1][j]) 
        
'''
La v es alfa de la teoría
Eje1:
    f(x) = e**-(x-b/2)**2
    b = 5 
    d = 10
    N = 40
    M = 400
    v = 
'''

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

