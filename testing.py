import numpy as np


# aux
def elim_gaussiana(A):
    if A is None:
        return None, None, 0

    cant_op = 0
    m = A.shape[0]
    n = A.shape[1]
    Ac = A.copy()

    if m != n:
        return None, None, 0

    ## desde aqui -- CODIGO A COMPLETAR
    L = np.eye(n)

    for k in range(n - 1):
        pivote = Ac[k, k]
        if np.isclose(pivote, 0):
            return None, None, 0

        for i in range(k + 1, n):
            # 1 división para el multiplicador
            m_ik = Ac[i, k] / pivote
            cant_op += 1

            L[i, k] = m_ik
            Ac[i, k] = 0.0  # El elemento debajo del pivote se hace 0

            # Actualización del resto de la fila i
            for j in range(k + 1, n):
                Ac[i, j] -= m_ik * Ac[k, j]
                cant_op += 2  # 1 multiplicación + 1 resta

    U = Ac

    ## hasta aqui, calculando L, U y la cantidad de operaciones sobre
    ## la matriz Ac

    return L, U, cant_op


# 1)
def calculaLU(A):
    """
    Calcula la factorizacion LU de la matriz A y retorna las matrices L
    y U, junto con el numero de operaciones realizadas. En caso de
    que la matriz no pueda factorizarse retorna None.
    """
    resultado = elim_gaussiana(A)
    if resultado is None:
        L = None
        U = None
        cant_oper = 0
    else:
        L, U, cant_oper = resultado

    return L, U, cant_oper


# 4)
def calculaLDV(A):
    """
    Calcula la factorizacion LDV de la matriz A, de forma tal que A =
    LDV, con L triangular inferior, D diagonal y V triangular
    superior. En caso de que la matriz no pueda factorizarse
    retorna None .
    """
    L, U, cant_oper = calculaLU(A)
    # check por si no tiene lu
    if L is None or U is None:
        return None, None, None
    # check por si no se puede hacer ldv
    for i in range(U.shape[0]):
        if np.isclose(U[i, i], 0):
            return None, None, None
    n = np.shape(L)[0]

    # creo y relleno d con la diag de u
    D = np.zeros((n, n))
    for i in range(n):
        D[i, i] = U[i, i]

    # creo y relleno v dividiendo la fila por el factor
    V = np.zeros((n, n))
    for i in range(n):
        V[i, :] = U[i, :] / U[i, i]

    return L, D, V


# 5)
def esSDP(A, atol=1e-8):
    """
    Checkea si la matriz A es simetrica definida positiva (SDP) usando
    la factorizacion LDV.
    """
    L, D, V = calculaLDV(A)
    if L is None or D is None or V is None:
        return False
    for i in range(A.shape[0]):
        if np.isclose(D[i, i], 0, atol=atol) or D[i, i] < 0:
            return False
    return True


print("-----Check de sdp\n")

D0 = np.diag([1, -1, 1])
print(esSDP(D0))
# False
D0 = np.diag([1, 1, 1e-16])
print(esSDP(D0))
# False
L0 = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
D0 = np.diag([1, 1, 1])
V0 = np.array([[1, 0, 0], [1, 1, 0], [1, 1 + 1e-3, 1]]).T
A = L0 @ D0 @ V0
print(esSDP(A, 1e-3))
# True
A = np.array([[4.0, 2.0], [2.0, 3.0]])
print(esSDP(A))
# True
A = np.array([[1.0, 2.0], [3.0, 4.0]])
print(esSDP(A))
# False

print("-----ÉXITO SDP!!!!\n")
