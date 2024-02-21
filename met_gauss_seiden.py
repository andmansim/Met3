#metodo de Gauss Seiden

#Extremos de x, y
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
d = int(input("Ingrese el valor de d: "))

#Número de huecos de x, y
N = int(input("Ingrese el número de huecos de X: "))
M = int(input("Ingrese el número de huecos de Y: "))

#Tamaño de los huecos
h = (b-a)/N
k = (d-c)/M 

#Matriz
w = [[]]

#Creamos los bordes de la matriz
for i in range(1, N):
    w[i][0] = 
    w[i][M] = 

for j in range(1, M):
    w[0][j] = 
    w[N][j] = 

#Rellenamos el resto de la matriz
for i in range(N):
    for k in range(M):
        w[i][k] = 0

#funcion
def f(x, y):
    return 0

#recorremos los puntos interiores de la malla
for k in range(100):#iteramos inicialmente 100, luego ya lo adapataremos
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = ( k**2 * (w[i+1][j]+w[i-1][j])+ h**2*(w[i][j+1]+w[i][j-1]) - (h*k)**2 * f(i, j))/(2*(h**2+k**2))
            
'''
Ejemplo:

'''