# pyrefly
import numpy as np

#Ejercicio 1. Desarrollar una funci´on esCuadrada(A) que devuelva verdadero
#si la matriz A es cuadrada y Falso en caso contrario.

def esCuadrada(A):
    #check de que tenga al menos 1 fila
    if len(A) == 0:
        return False

    #check de filas para casos mas normales
    for fila in A:
        if len(fila) != len(A):
            return False

    return True



# 1. Caso base correcto (Matriz cuadrada 2x2)
A = np.array([[1, 2], [3, 4]])
# Esperado: True

# 2. Matriz rectangular (2x3)
B = np.array([[1, 2, 3], [4, 5, 6]])
# Esperado: False

# 3. Arreglo 1D vacío
C = np.array([])
# Esperado: False

# 4. Arreglo 2D vacío (0 filas, 0 columnas)
D = np.array([[]])
# Esperado: False

# 5. Vector unidimensional (1D de 3 elementos)
E = np.array([1, 2, 3])
# Esperado: False (Tu código original falla con TypeError acá)

# 6. Matriz cuadrada 1x1
F = np.array([[5]])
# Esperado: True

# 7. Matriz escalar / 0D
G = np.array(42)
# Esperado: False (Tu código original falla con TypeError acá)

print(esCuadrada(A))
print(esCuadrada(B))
print(esCuadrada(C))
print(esCuadrada(D))
print(esCuadrada(E))
print(esCuadrada(F))
print(esCuadrada(G))