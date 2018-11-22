import numpy as np

N = 6

#Definir el vector de los punto en I
I = np.array([0.5, 1, 2, 4, 8, 12])

#Definir los puntos del vecto V
V = np.array([160, 120, 94, 75, 62, 56])

def F_a (a,b,c):
    sum = 0
    aux = 0
    for i in range (0,N):
        aux = I[i]**b
        sum += (aux**2)
    
    return -sum

z = np.array([1,1,1])  # Z[0]

print (F_a(z[0],z[1],z[2]))