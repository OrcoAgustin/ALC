import numpy as np

def elim_gaussiana(A):
    if A is None:
        return -1
        
    A = np.array(A, dtype=float)
    
    m, n = A.shape
    if m!=n:
        return -1
 
    Ac = A.copy()  # esta es la Ae(k) que se va actualizando en cada paso
 
    nops = 0  # contador de operaciones aritméticas
 
    # Contadores separados por si se quieren inspeccionar por separado
    n_sumas_restas = 0
    n_mult = 0
    n_div = 0
 
    for k in range(n - 1):
        # pivote de la etapa k
        pivote = Ac[k, k]
        if pivote == 0:                                             
            return -1 
 
        for i in range(k + 1, n):
            # --- cálculo del multiplicador (va en la parte triangular
            # inferior, reemplazando al cero que "debería" quedar) ---
            Ac[i, k] = Ac[i, k] / pivote
            n_div += 1
 
            multiplicador = Ac[i, k]
 
            # --- actualización de la fila i, sólo columnas j > k
            # (las columnas <= k ya quedaron fijas: en col k está el
            # multiplicador, y a la izquierda ya son ceros de etapas
            # anteriores) ---
            for j in range(k + 1, n):
                Ac[i, j] = Ac[i, j] - multiplicador * Ac[k, j]
                n_mult += 1
                n_sumas_restas += 1
 
    nops = n_sumas_restas + n_mult + n_div
 
    # Separamos L y U
    L = np.zeros((n, n))
    U = np.zeros((n, n))
 
    for i in range(n):
        for j in range(n):
            if i == j:
                L[i, j] = 1.0          # diagonal de L
                U[i, j] = Ac[i, j]     # diagonal de U
            elif i > j:
                L[i, j] = Ac[i, j]     # parte triangular inferior -> L
            else:
                U[i, j] = Ac[i, j]     # parte triangular superior -> U
 
    return L, U, nops


def calculaLU(A):
    """Calcula la factorización LU de la matriz A y retorna las matrices L
    y U, junto con el número de operaciones realizadas. En caso de que la
    matriz no pueda factorizarse retorna None."""
   
    res= elim_gaussiana(A)
    if res == -1:
        return None, None, 0
    else:
        return res
    
print("TESTS calculaLU")

L0 = np.array([[1,0,0],
               [0,1,0],
               [1,1,1]])

U0 = np.array([[10,1,0],
               [0,2,1],
               [0,0,1]])

A =  L0 @ U0
L,U,nops = calculaLU(A)
assert(np.allclose(L,L0))
assert(np.allclose(U,U0))


L0 = np.array([[1,0,0],
               [1,1.001,0],
               [1,1,1]])

U0 = np.array([[1,1,1],
               [0,1,1],
               [0,0,1]])
A =  L0 @ U0
L,U,nops = calculaLU(A)
assert(not np.allclose(L,L0))
assert(not np.allclose(U,U0))
assert(np.allclose(L,L0,atol=1e-3))
assert(np.allclose(U,U0,atol=1e-3))
assert(nops == 13)

L0 = np.array([[1,0,0],
               [1,1,0],
               [1,1,1]])

U0 = np.array([[1,1,1],
               [0,0,1],
               [0,0,1]])

A =  L0 @ U0
L,U,nops = calculaLU(A)
assert(L is None)
assert(U is None)
assert(nops == 0)

assert(calculaLU(None) == (None, None, 0))

assert(calculaLU(np.array([[1,2,3],[4,5,6]])) == (None, None, 0))

print("-----ÉXITO!!!!\n")

