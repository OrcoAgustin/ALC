import numpy as np

#aux
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

def norma(x, p):
    # la norma p del vector x.
    # asumo que no van a pasar p<1

    # si p es inf
    if p == float("inf") or p == np.inf or str(p).lower() == "inf":
        return np.max(np.abs(x))
    # resto de casos
    x = np.array(x)
    norma = 0
    for i in range(len(x)):
        norma += abs(x[i]) ** p
    return norma ** (1 / p)

def matmul(a, b):
    """Implementación en Python puro de la multiplicación matricial (@)."""
    is_a_1d = not isinstance(a[0], (list, tuple))
    is_b_1d = not isinstance(b[0], (list, tuple))

    # Normalizar entradas a estructuras 2D para unificar la lógica
    mat_a = [a] if is_a_1d else a
    mat_b = [[x] for x in b] if is_b_1d else b

    rows_a, cols_a = len(mat_a), len(mat_a[0])
    rows_b, cols_b = len(mat_b), len(mat_b[0])

    if cols_a != rows_b:
        raise ValueError(f"Dimensiones incompatibles para multiplicación: ({rows_a}, {cols_a}) y ({rows_b}, {cols_b})")

    # Multiplicación matricial estándar O(n^3)
    result = [
        [sum(mat_a[i][k] * mat_b[k][j] for k in range(cols_a)) for j in range(cols_b)]
        for i in range(rows_a)
    ]

    # Ajustar la salida según las dimensiones de entrada (comportamiento de np.matmul)
    if is_a_1d and is_b_1d:
        return result[0][0]  # Vector 1D x Vector 1D -> Escalar (Producto punto)
    if is_a_1d:
        return result[0]     # Vector 1D x Matriz 2D -> Vector 1D
    if is_b_1d:
        return [row[0] for row in result]  # Matriz 2D x Vector 1D -> Vector 1D

    return result

#1)
def QR_con_GS(A, tol =1e-12, retorna_nops=False ) :

    """A una matriz de n x n 
    tol la tolerancia con la que se filtran elementos nulos en R
    retorna_nops permite (opcionalmente) retornar el numero de operaciones realizado
    retorna matrices Q y R calculadas con Gram Schmidt (y como
    tercer argumento opcional, el numero de operaciones).
    Si la matriz A no es de n x n, debe retornar None
    """
    A = np.array(A, dtype=float)

    if not esCuadrada(A):
        return None

    n = len(A)
    Q = np.zeros((n, n), dtype=float)
    R = np.zeros((n, n), dtype=float)
    nops=0

    for j in range(n):
        v=A[:,j].copy()

        for i in range(j):
            vPrev = Q[:,i].copy() 
            R[i,j]= matmul(v,vPrev) 
            v=v-R[i,j]*vPrev
            nops+=2

        normaV=norma(v,2)
        nops+=1

        if normaV<tol:
            normaV=0.0
        R[j,j]=normaV
        if normaV != 0.0:
            Q[:,j]=v/normaV
        else:
            Q[:,j]=v

    #chequeas que no haya 0 en R    
    R[np.abs(R) < tol] = 0.0

    if retorna_nops:
        return Q, R, nops
    return Q, R
        
            






















def QR_con_HH(A,tol=1e-12,extras=False):
    """
    A una matriz de m x n (m>=n)
    tol la tolerancia con la que se filtran elementos nulos en R
    retorna matrices Q y R calculadas con reflexiones de Householder
    Si la matriz A no cumple m>=n, debe retornar None
    extras : bool, opcional
        Si es True, devuelve informacion extra sobre el proceso de factorizacion.
        Por defecto es False. Esto lo hacemos para poder graficar el proceso.
    Devuelve la factorizacion QR de A usando reflectores de Householder.
    Devuelve: 
        Q, R, extra_info (si extras es True)
        Q, R (si extras es False)
    extra_info es un diccionario con la clave:
        'R_matrices': lista de las matrices R en cada paso
        'Q_matrices': lista de las matrices Q en cada paso


    """
def calculaQR(A,metodo='RH',tol=1e-12):
    """
    A una matriz de n x n 
    tol la tolerancia con la que se filtran elementos nulos en R    
    metodo = ['RH','GS'] usa reflectores de Householder (RH) o Gram Schmidt (GS) para realizar la factorizacion
    retorna matrices Q y R calculadas con Gram Schmidt (y como tercer argumento opcional, el numero de operaciones)
    Si el metodo no esta entre las opciones, retorna None
    """

    
###tests###

# --- Matrices de prueba ---
A2 = np.array([[1., 2.],
               [3., 4.]])

A3 = np.array([[1., 0., 1.],
               [0., 1., 1.],
               [1., 1., 0.]])

A4 = np.array([[2., 0., 1., 3.],
               [0., 1., 4., 1.],
               [1., 0., 2., 0.],
               [3., 1., 0., 2.]])

# --- Funciones auxiliares para los tests ---
def check_QR(Q,R,A,tol=1e-10):
    # Comprueba ortogonalidad y reconstrucción
    assert np.allclose(Q.T @ Q, np.eye(Q.shape[1]), atol=tol)
    assert np.allclose(Q @ R, A, atol=tol)

# --- TESTS PARA QR_by_GS2 ---
# pyrefly: ignore [bad-unpacking, not-iterable]
Q2,R2 = QR_con_GS(A2)
check_QR(Q2,R2,A2)

# pyrefly: ignore [bad-unpacking, not-iterable]
Q3,R3 = QR_con_GS(A3)
check_QR(Q3,R3,A3)

# pyrefly: ignore [bad-unpacking, not-iterable]
Q4,R4 = QR_con_GS(A4)
check_QR(Q4,R4,A4)
print("pasaste los tests del ej 1")
"""
# --- TESTS PARA QR_by_HH ---
Q2h,R2h = QR_con_GS(A2)
check_QR(Q2h,R2h,A2)

Q3h,R3h = QR_con_HH(A3)
check_QR(Q3h,R3h,A3)

Q4h,R4h = QR_con_HH(A4)
check_QR(Q4h,R4h,A4)

# --- TESTS PARA calculaQR ---
Q2c,R2c = calculaQR(A2,metodo='RH')
check_QR(Q2c,R2c,A2)

Q3c,R3c = calculaQR(A3,metodo='GS')
check_QR(Q3c,R3c,A3)

Q4c,R4c = calculaQR(A4,metodo='RH')
check_QR(Q4c,R4c,A4)
"""