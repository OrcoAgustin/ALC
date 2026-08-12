# pyrefly
import numpy as np

#Ejercicio 1. Desarrollar una funci´on esCuadrada(A) que devuelva verdadero
#si la matriz A es cuadrada y Falso en caso contrario.

def esCuadrada(A):
    #check de que tenga al menos 1 fila
    if not isinstance(A,list) or len(A) == 0:
        return False

    #check de filas para casos mas normales
    for fila in A:
        if not isinstance(fila, list) or len(fila) != len(A):
            return False

    return True


