#Edp hiperbólica
import numpy as np

#Extremos de x, y
a = 0
b = int(input("Ingrese el valor de b, xf: "))
c = 0 
d = int(input("Ingrese el valor de d, tf: "))
#velocidad
v = float(input("Ingrese la velocidad: "))
#Número de huecos de x, y. Los elegimos nosotros
N = int(input("Ingrese el número de huecos de X: "))
M = int(input("Ingrese el número de huecos de T: "))


#Tamaño de los huecos
h = b/N
k = d/M 
p = v*h/k #para no escribir todo esto abajo

#Matriz
# Inicializar matriz w con dimensiones N x M
w = [[0 for j in range(M+1)] for i in range(N+1)]


#funcion inicial y de frontera
def f(x):
    #Cambia dependiendo del ejercicio
    #x = (a+i*h)
    return x*(b-x)

def g(x):  
    #Cambia dependiendo del ejercicio
    return 0

#Creamos los bordes de la matriz
for i in range(1, N):
    #Cambian dependiendo del ejercicio
    w[0][i] = f(h*i)
    w[M][i] = w[0][i] + k*g(h*i)

for j in range(1, M):
    #Cambian dependiendo del ejercicio
    w[j][0] = 0
    w[j][N] = 0



#recorremos los puntos interiores de la malla
for i in range(1, N):
    for j in range(1, M):
        w[j+1][i] = 2*(1 - p**2)*w[j][i] + (p**2)*(w[j][i+1] + w[j][i-1]) - w[j-1][i]
        
'''
Ec de ondas
Eje1: 
    f(x) = x(b-x)
    g(x) = 0
    b=5, d = 10, v=0.5, N=40, M=400 

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

