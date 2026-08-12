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
    
    #gaussiana
    for p in range(len(U)):
        valorDiag = U[p][p]
        for i in range(p+1, len(U)):
            #k = escalar para anular la columna debajo del punto de la diag
            k = U[i][p] / valorDiag
            for j in range(p, len(U)):
                U[i][j] -= k * U[p][j]

    #preguntar si entendiste bien lo de hacer 0 la diag
    for i in range(len(U)):
        U[i][i] = 0

    return U

######################################################################################################
#Ejercicio 3. Desarrollar una funci´on triangInf(A) que devuelva la matriz L
#correspondiente a la matriz Triangular Inferior de A sin su diagonal.

##depsues de charlar un rato con claudio me parece que hay algo raro aca. revisar despues
