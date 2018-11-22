import numpy as np

N = 6

#Definir el vector de los punto en I
I = np.array([0.5, 1, 2, 4, 8, 12])

#Definir los puntos del vecto V
V = np.array([160, 120, 94, 75, 62, 56])

def F (a,b,c):
    sum = 0
    for i in range (0,N):
        A = V[i] - (a*(I[i]**b)) + c
        B = I[i]**b
        sum += (A*B)
    return sum

def G (a,b,c):
    sum = 0
    for i in range (0,N):
        A = V[i] - (a*(I[i]**b)) + c
        B = I[i]**(b-1)
        sum += (A*B)
    return sum

def H (a,b,c):
    sum = 0
    for i in range (0,N):
        A = V[i] - (a*(I[i]**b)) + c
        sum += A
    return sum

def F_a (a,b,c):
    sum = 0
    aux = 0
    for i in range (0,N):
        aux = I[i]**b
        sum += (aux**2)
    
    return -sum

def F_b (a,b,c):
    sum = 0

    for i in range (0,N):
        
        A = V[i] - (a * I[i]) - c
        A = A * b
        A = A * (I[i] ** (b-1))

        B = a * b
        B = B * (I[i] ** b)
        B = B * (I[i] ** (b-1))
        
        sum += A-B

    return sum

def F_c (a,b,c):
    sum = 0

    for i in range (0,N):
        sum += (I[i]**b)

    return -sum

def G_a (a,b,c):
    sum = 0

    for i in range (0,N):
        A = I[i]**b
        B = I[i]**(b-1)

        sum += A*B

    return -sum

def G_b (a,b,c):
    sum = 0

    for i in range (0,N):
        A = V[i] - (a*(I[i]**b) - c)
        A = A * (b-1)
        A = A * (I[i]**(b-2))

        B = a * b
        B = B * (I[i]**(2*(b-1)))

        sum += A-B

    return sum

def G_c (a,b,c):
    sum = 0

    for i in range (0,N):
        
        sum += (I[i]**(b-1))

    return -sum

def H_a (a,b,c):
    sum = 0
    for i in range (0,N):
        sum += (I[i]**b)
    return -sum

def H_b (a,b,c):
    sum = 0
    for i in range (0,N):
        A = I[i]**(b-1)
        A = A*a*b
        sum += A
    return -sum

def H_c (a,b,c):
    sum = 0
    for i in range (0,N):
        sum += 1
    return -sum


# Matriz Jacobiano 
def Jacobiano (mF, mG, mH):
    mJ = np.empty(3,3)
    # Rellenando la matriz
    for i in range (0,3):
        mJ[0][i] = mF[i]

    for i in range (0,3):
        mJ[1][i] = mG[i]
    
    for i in range (0,3):
        mJ[2][i] = mH[i]
    
    return mJ

    
z = np.array([1,1,1])  # Z[0]

n1 = F_a(z[0],z[1],z[2])
n2 = F_a(z[0],z[1],z[2])
n3 = F_a(z[0],z[1],z[2])
