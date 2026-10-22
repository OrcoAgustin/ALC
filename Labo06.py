import numpy as np


###aux###


def esSimetrica(A):
    A = np.asarray(A)

    if len(A) != len(A[0]):
        return False

    for i in range(len(A)):
        for j in range(len(A)):
            dif = A[i][j] - A[j][i]
            if abs(dif) > 1e-8:
                return False

    return True


def productoInterno(a, b):
    # asumimos que misma dim los vectores
    a = np.array(a)
    b = np.array(b)
    res = 0

    for i in range(len(a)):
        res += a[i] * b[i]

    return res


def matmul(a, b):
    """Implementación en Python puro de la multiplicación matricial (@)."""
    a = np.asarray(a)
    b = np.asarray(b)
    esAVector = a.ndim == 1
    esBVector = b.ndim == 1

    # Normalizar entradas a estructuras 2D para unificar la lógica
    A = [a] if esAVector else a
    B = [[x] for x in b] if esBVector else b

    filasA, colsA = len(A), len(A[0])
    filasB, colsB = len(B), len(B[0])

    if colsA != filasB:
        raise ValueError(
            f"Dimensiones incompatibles para multiplicación: ({filasA}, {colsA}) y ({filasB}, {colsB})"
        )

    # Multiplicación matricial estándar O(n^3)
    result = [
        [sum(A[i][k] * B[k][j] for k in range(colsA)) for j in range(colsB)]
        for i in range(filasA)
    ]

    # Ajustar la salida según las dimensiones de entrada (comportamiento de np.matmul)
    if esAVector and esBVector:
        return result[0][0]  # Vector 1D x Vector 1D -> Escalar (Producto punto)
    if esAVector:
        return result[0]  # Vector 1D x Matriz 2D -> Vector 1D
    if esBVector:
        return [row[0] for row in result]  # Matriz 2D x Vector 1D -> Vector 1D

    return result


def normaMC(x, p):
    x = np.asarray(x, dtype=float)
    is_inf = p == float("inf") or p == np.inf or str(p).lower() == "inf"

    # Si x es una matriz (2D)
    if x.ndim == 2:
        filas, cols = x.shape
        normas = np.zeros(cols)
        for j in range(cols):
            if is_inf:
                max_val = abs(x[0, j])
                for i in range(1, filas):
                    val = abs(x[i, j])
                    if val > max_val:
                        max_val = val
                normas[j] = max_val
            else:
                suma = 0.0
                for i in range(filas):
                    suma += abs(x[i, j]) ** p
                normas[j] = suma ** (1 / p)
        return normas

    # Si x es un vector (1D)
    if is_inf:
        max_val = abs(x[0])
        for i in range(1, len(x)):
            val = abs(x[i])
            if val > max_val:
                max_val = val
        return max_val

    suma = 0.0
    for val in x:
        suma += abs(val) ** p
    return suma ** (1 / p)


def normalizarVector(V):
    vector = np.array(V, dtype=float)
    norma = normaMC(vector, 2)
    if norma == 0:
        vectorNormal = vector
    else:
        vectorNormal = vector / norma

    return vectorNormal


def autoValor(A, v):
    # cociente de Rayleigh
    # MATEMATICA!
    return productoInterno(v, matmul(A, v))


##################################################################################################


def metpot2k(A, tol=1e-15, K=1000):
    """
    A una matriz de n x n
    tol la tolerancia en la diferencia entre un paso y el siguiente de la estimacion del
    autovector .
    K el numero maximo de iteraciones a realizarse .
    Retorna vector v, autovalor lambda y numero de iteracion realizadas k
    """
    n = len(A)
    v = np.random.rand(n)
    candidatoPrevio = normalizarVector(v)
    nuevoCandidato = candidatoPrevio

    i = 0

    while i < K:
        nuevoCandidato = matmul(A, candidatoPrevio)
        nuevoCandidato = normalizarVector(nuevoCandidato)

        # si estan alineados y ambos normalizados el producto interno da 1, osea que llegamos al criterio de corte
        dif = 1 - abs(productoInterno(nuevoCandidato, candidatoPrevio))
        if dif < tol:
            return nuevoCandidato, autoValor(A, nuevoCandidato), i + 1

        # sigue
        candidatoPrevio = nuevoCandidato
        i += 1

    return nuevoCandidato, autoValor(A, nuevoCandidato), i


def diagRH(A, tol=1e-15, K=1000):
    """
    A una matriz simetrica de n x n
    t ol la tolerancia en la diferencia entre un paso y el siguiente de la estimacion del
    autovector .
    K el numero maximo de iteraciones a realizarse
    retorna matriz de autovectores S y matriz de autovalores D, tal que A = S D S.T
    Si la matriz A no es simetrica , debe retornar None
    """

    A = np.asarray(A)

    n = len(A)
    if not esSimetrica(A):
        return None

    # caso base
    if n == 1:
        return np.array([[1.0]]), np.array(A, dtype=float)

    # caso recursivo
    v1, lambda1, p = metpot2k(A, tol, K)

    # aca haces el paso de householder
    e1 = np.zeros(n)
    e1[0] = 1.0
    u = e1 - v1  # vector que une e1 con v1
    uu = productoInterno(u, u)
    if uu < 1e-12:
        # PI = 0 ent u casi nulo ent esta bien el e1
        H = np.eye(n)
    else:
        # H = I - 2 u uᵀ / (uᵀu)
        H = np.eye(n) - 2 * (u.reshape(n, 1) * u.reshape(1, n)) / uu

    # preparo paso siguiente
    M = np.asarray(matmul(matmul(H, A), H))
    B = M[1:, 1:]

    # recursion
    # pyrefly: ignore[not-iterable]
    S2, D2 = diagRH(B, tol, K)

    # armo S
    STemp = np.eye(n, dtype=float)
    for i in range(1, n):
        for j in range(1, n):
            STemp[i][j] = S2[i - 1][j - 1]
    S = np.asarray(matmul(H, STemp))

    # armo D
    D = np.zeros((n, n), dtype=float)
    D[0][0] = lambda1
    i = 1
    for i in range(1, n):
        D[i][i] = D2[i - 1][i - 1]

    return S, D


##################TESTSSSSSSS
# ############################

S = np.vstack(
    [
        np.array([2, 1, 0]) / np.sqrt(5),
        np.array([-1, 2, 5]) / np.sqrt(30),
        np.array([1, -2, 1]) / np.sqrt(6),
    ]
).T

# Pedimos que pase el 95% de los casos
exitos = 0
for i in range(100):
    D = np.diag(np.random.random(3) + 1) * 100
    A = S @ D @ S.T
    v, l, _ = metpot2k(A, 1e-15, 1e5)
    if np.abs(l - np.max(D)) < 1e-8:
        exitos += 1
assert exitos > 95
print("Test 1 OK:", exitos, "/ 100")


# Test con HH
exitos = 0
for i in range(100):
    v = np.random.rand(9)
    # v = np.abs(v)
    # v = (-1) * v
    ixv = np.argsort(-np.abs(v))
    D = np.diag(v[ixv])
    I = np.eye(9)
    H = I - 2 * np.outer(v.T, v) / (np.linalg.norm(v) ** 2)  # matriz de HouseHolder

    A = H @ D @ H.T
    v, l, _ = metpot2k(A, 1e-15, 1e5)
    # max_eigen = abs(D[0][0])
    if abs(l - D[0, 0]) < 1e-8:
        exitos += 1
assert exitos > 95
print("Test 2 OK:", exitos, "/ 100")


def normaExacta(A, p=[1, "inf"]):
    is_inf = p == "inf" or p == np.inf or p == float("inf")
    pCorrecto = p == [1, "inf"] or p == 1 or is_inf
    if not pCorrecto:
        return None

    A = np.asarray(A, dtype=float)

    n1 = float(np.max(np.sum(np.abs(A), axis=0)))
    ninf = float(np.max(np.sum(np.abs(A), axis=1)))
    res = [n1, ninf]

    if p == 1:
        return res[0]
    elif is_inf:
        return res[1]
    else:
        return res


# Tests diagRH
D = np.diag([1, 0.5, 0.25])
S = np.vstack(
    [
        np.array([1, -1, 1]) / np.sqrt(3),
        np.array([1, 1, 0]) / np.sqrt(2),
        np.array([1, -1, -2]) / np.sqrt(6),
    ]
).T

A = S @ D @ S.T
# pyrefly: ignore[not-iterable]
SRH, DRH = diagRH(A, tol=1e-15, K=1e5)
assert np.allclose(D, DRH)
assert np.allclose(np.abs(S.T @ SRH), np.eye(A.shape[0]), atol=1e-7)


# Pedimos que pase el 95% de los casos
exitos = 0
for i in range(100):
    A = np.random.random((5, 5))
    A = 0.5 * (A + A.T)
    # pyrefly: ignore[not-iterable]
    S, D = diagRH(A, tol=1e-15, K=1e5)
    ARH = S @ D @ S.T
    e = normaExacta(ARH - A, p="inf")
    # pyrefly: ignore[unsupported-operation]
    if e < 1e-5:
        exitos += 1
assert exitos >= 95
