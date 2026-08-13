# pyrefly
import numpy as np


######################################################################################################
#Ejercicio 1. Desarrollar una funci´on esCuadrada(A) que devuelva verdadero
#si la matriz A es cuadrada y Falso en caso contrario.

def esCuadrada(A):
    #normalizamos las entradas
    array = np.array(A)
    #teoricamente esto asegura que tengan el mismo largo todas las filas, no hace falta el loop anyways we keep it 

    if np.size(array) == 0:
        return False

    for filas in array:
        if len(array) != np.size(filas):
            return False 
    
    return True 

######################################################################################################
#Ejercicio 2. Desarrollar una funci´on triangSup(A) que devuelva la matriz U
#correspondiente a la matriz Triangular Superior de A sin su diagonal.

def triangSup(A):
    #check cuadrado
    if not esCuadrada(A):
        raise ValueError("La matriz no es cuadrada")

    #creamos matriz U resultado
    U = np.array(A)
    
    #entiendo que no hay que hacer gaussiana y solamente ponerlo con 0 abajo de la diag
    for i in range(len(U)):
        for j in range(i, len(U)):
            if i == j:
                U[i][j] = 0
            if i > j:
                U[i][j] = 0
            
    return U

######################################################################################################
#Ejercicio 3. Desarrollar una funci´on triangInf(A) que devuelva la matriz L
#correspondiente a la matriz Triangular Inferior de A sin su diagonal.

def triangInf(A):
    #check cuadrado
    if not esCuadrada(A):
        raise ValueError("La matriz no es cuadrada")

    #creamos matriz L resultado
    L = np.array(A)

    for i in range(len(L)):
        for j in range(len(L)):
            if i == j:
                L[i][j] = 0
            if i < j:
                L[i][j] = 0
            
    return L

######################################################################################################
#Ejercicio 4. Desarrollar una funci´on diagonal(A) que devuelva la matriz D
#correspondiente a la matriz diagonal de A.

def diagonal(A):
    if not esCuadrada(A):
            raise ValueError("La matriz no es cuadrada")
    
    D = np.array(A) 
    for i in range(len(D)):
        for j in range(len(D)):
            if i != j:
                D[i][j]=0
    
    return D        

######################################################################################################
#Ejercicio 5. Desarrollar una funci´on traza(A) que calcule la traza de una
#matriz cualquiera A    
#traza = suma de la diag

def traza(A):
    res=0
    if not esCuadrada(A):
        raise ValueError("La matriz no es cuadrada")

    for i in range(len(A)):
        res+= A[i][i]

    return res

######################################################################################################
#Ejercicio 6. Desarrollar una funci´on traspuesta(A) que devuelva la matriz
#traspuesta de A.

def traspuesta(A):
    if not A or not A[0]:
        raise ValueError("La matriz no puede estar vacía")

    AT = np.empty((len(A[0]), len(A)))

    for i in range(len(A)):
        for j in range(len(A[0])):
            AT[j][i] = A[i][j]
    
    return AT

######################################################################################################
#Ejercicio 7. Desarrollar una funci´on esSimetrica(A) que devuelve True si la
#matriz A es sim´etrica y False en caso contrario.

def esSimetrica(A):
    if not A or not A[0]:
        raise ValueError("La matriz no puede estar vacía")

    if not esCuadrada(A):
        raise ValueError("La matriz no es cuadrada")

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i][j] != A[j][i]:
                return False
            
    return True

######################################################################################################
#Ejercicio 8. Desarrollar una funci´on calcularAx(A,x) que recibe una matriz
#A de tama˜no n × m y un vector x de largo m y devuelve un vector b de largo n
#resultado de la multiplicaci´on vectorial de la matriz y el vector.

def calcularAx(A, x):
    if not A or not A[0] or len(x)==0:
        raise ValueError("La matriz A y el vector x no pueden estar vacios")

    if len(x) !=len(A[0]):
        raise ValueError("Dimensiones incompatibles")

    b=np.zeros(len(A))

    for i in range(len(A)):
        valorF = 0
        for j in range(len(A[0])):
            valorF += A[i][j] * x[j]
        b[i] = valorF

    return b

######################################################################################################
#Ejercicio 9. Desarrollar una funci´on intercambiarFilas(A, i, j), 
#que intercambie las filas i y la j de la matriz A. El intercambio tiene que ser in-place.

def intercambiarFilas(A, i, j):
    if not A or not A[0]:
        raise ValueError("La matriz A no es valida")

    if i >= len(A) or i < 0:
        raise ValueError("no existe fila I")
    
    if j >= len(A) or j < 0:
        raise ValueError("no existe fila J")

    for k in range(len(A[0])):
        vTemp=A[i][k]
        A[i][k]=A[j][k]
        A[j][k]=vTemp
    #in place no devuelve nada