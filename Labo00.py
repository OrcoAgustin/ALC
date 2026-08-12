# pyrefly
from numpy._typing import _nested_sequence
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
            if i < j:
                U[i][j] = 0
            
    return U

######################################################################################################
#Ejercicio 3. Desarrollar una funci´on triangInf(A) que devuelva la matriz L
#correspondiente a la matriz Triangular Inferior de A sin su diagonal.

def triangInf(A):#check cuadrado
    if not esCuadrada(A):
        raise ValueError("La matriz no es cuadrada")

    #creamos matriz L resultado
    L = np.array(A)

    for i in range(len(L)):
        for j in range(len(L)):
            if i == j:
                L[i][j] = 0
            if i > j:
                L[i][j] = 0
            
    return L

######################################################################################################
#Ejercicio 4. Desarrollar una funci´on diagonal(A) que devuelva la matriz D
#correspondiente a la matriz diagonal de A.

def diagonal(A):

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