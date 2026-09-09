import numpy as np


def norma(x, p):
    x = np.asarray(x, dtype=float)
    is_inf = p == float("inf") or p == np.inf or str(p).lower() == "inf"

    if is_inf:
        maximo = abs(x[0])
        for i in range(1, len(x)):
            if abs(x[i]) > maximo:
                maximo = abs(x[i])
        return maximo

    return sum(abs(xi) ** p for xi in x) ** (1 / p)


def normaMatMC(A, q, p, Np):
    n = A.shape[1]
    maximaNorma = -1.0
    x_opt = np.zeros(n)

    candidatos = []

    # 1. Vectores de la base canónica
    for i in range(n):
        for signo in [1, -1]:
            x = np.zeros(n)
            x[i] = signo
            candidatos.append(x)

    # 2. Vértices del hipercubo si q es infinito
    if str(q).lower() in ["inf", "infinity"]:
        for i in range(2**n):
            x = np.array([1 if (i >> j) & 1 else -1 for j in range(n)], dtype=float)
            candidatos.append(x)

    # Evaluación de candidatos determinísticos
    for x in candidatos:
        norm_x = norma(x, q)
        if norm_x > 0:
            x = x / norm_x
            val = norma(A @ x, p)
            if val > maximaNorma:
                maximaNorma = val
                x_opt = np.array(x)

    # 3. Bucle de Monte Carlo con vectores aleatorios
    for _ in range(Np):
        if q == 2:
            x = np.random.randn(n)
        elif q == 1:
            x = np.random.laplace(0, 1, n)
        else:
            x = np.random.uniform(-1, 1, n)

        norm_x = norma(x, q)
        if norm_x == 0:
            continue
        x = x / norm_x

        val = norma(A @ x, p)
        if val > maximaNorma:
            maximaNorma = val
            x_opt = np.array(x)

    return maximaNorma, x_opt


def normaExacta(A, p=[1, "inf"]):
    pCorrecto = p == [1, "inf"]
    if not pCorrecto:
        return None

    A = np.asarray(A, dtype=float)
    res = []

    for norma_tipo in p:
        if norma_tipo == 1:
            res.append(float(np.max(np.sum(np.abs(A), axis=0))))
        else:
            res.append(float(np.max(np.sum(np.abs(A), axis=1))))

    return res


"""
nMC = normaMatMC(A=np.eye(2), q=2, p=1, Np=100000)
assert np.allclose(nMC[0], 1, atol=1e-3)
assert np.allclose(np.abs(nMC[1][0]), 1, atol=1e-3) or np.allclose(
    np.abs(nMC[1][1]), 1, atol=1e-3
)
assert np.allclose(np.abs(nMC[1][0]), 0, atol=1e-3) or np.allclose(
    np.abs(nMC[1][1]), 0, atol=1e-3
)

nMC = normaMatMC(A=np.eye(2), q=2, p="inf", Np=100000)
assert np.allclose(nMC[0], np.sqrt(2), atol=1e-3)
assert np.allclose(np.abs(nMC[1][0]), 1, atol=1e-3) and np.allclose(
    np.abs(nMC[1][1]), 1, atol=1e-3
)

A = np.array([[1, 2], [3, 4]])
nMC = normaMatMC(A=A, q="inf", p="inf", Np=1000000)
# pyrefly: ignore [bad-argument-type]
assert np.allclose(nMC[0], normaExacta(A, "inf"), rtol=2e-1)
"""


def normaMC(x, p):
    x = np.asarray(x, dtype=float)
    is_inf = p == float("inf") or p == np.inf or str(p).lower() == "inf"

    # Si x es una matriz (2D)
    if x.ndim == 2:
        filas, cols = x.shape
        normas = np.zeros(cols)
        for j in range(cols):
            if is_inf:
                max_val = 0.0
                for i in range(filas):
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
        return np.max(np.abs(x))
    return np.sum(np.abs(x) ** p) ** (1 / p)


def normaMatMC2(A, q, p, Np):
    n = A.shape[1]
    X = np.random.rand(n, Np)
    normaX = X / normaMC(X, p)
    Y = A @ normaX
    print(Y)
    normas = normaMC(Y, q)
    maxNorma = 0
    id = 0
    for i in range(Np):
        if normas[i] > maxNorma:
            maxNorma = normas[i]
            id = i
    return maxNorma, normaX[:, id]


nMC = normaMatMC2(A=np.eye(2), q=2, p=1, Np=100000)


assert np.allclose(nMC[0], 1, atol=1e-3)
assert np.allclose(np.abs(nMC[1][0]), 1, atol=1e-3) or np.allclose(
    np.abs(nMC[1][1]), 1, atol=1e-3
)
assert np.allclose(np.abs(nMC[1][0]), 1, atol=1e-3) or np.allclose(
    np.abs(nMC[1][1]), 1, atol=1e-3
)
assert np.allclose(np.abs(nMC[1][0]), 0, atol=1e-3) or np.allclose(
    np.abs(nMC[1][1]), 0, atol=1e-3
)

nMC = normaMatMC2(A=np.eye(2), q=2, p="inf", Np=100000)
print(nMC[0])
print(nMC[1])

assert np.allclose(nMC[0], np.sqrt(2), atol=1e-3)
assert np.allclose(np.abs(nMC[1][0]), 1, atol=1e-3) and np.allclose(
    np.abs(nMC[1][1]), 1, atol=1e-3
)
A = np.array([[1, 2], [3, 4]])
nMC = normaMatMC(A=A, q="inf", p="inf", Np=1000000)
# pyrefly: ignore [bad-argument-type]
assert np.allclose(nMC[0], normaExacta(A, "inf"), rtol=2e-1)
