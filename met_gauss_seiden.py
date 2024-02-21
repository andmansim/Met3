#metodo de Gauss Seiden

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
w = [[0 for j in range(M)] for i in range(N)]


#funcion
def f(x, y):
    return None

#Rellenamos el resto de la matriz
for i in range(N):
    for k in range(M):
        w[i][k] = 0

#Creamos los bordes de la matriz
for i in range(1, N):
    #Cambian dependiendo del ejercicio
    print(i)
    w[i][0] = 0
    w[i][M] = 0

for j in range(1, M):
    #Cambian dependiendo del ejercicio
    w[0][j] = 0
    w[N][j] = 1



#recorremos los puntos interiores de la malla
for k in range(100):#iteramos inicialmente 100, luego ya lo adapataremos
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = ( k**2 * (w[i+1][j]+w[i-1][j])+ h**2*(w[i][j+1]+w[i][j-1]) - (h*k)**2 * f(i, j))/(2*(h**2+k**2))
            
'''
Ejemplo: Laplaciano, la A es el gradiente
Au = 0 0<x<1, 0<y<1
u(0,y) = u(x,0) = u(x,1) = 0
u(1,y) = 1
'''