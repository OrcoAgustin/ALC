import numpy as np

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

    if isinstance(p, str):
        p = np.inf if p.strip().lower() == "inf" else float(p)

    is_inf = p == np.inf

    if x.ndim == 2:
        if is_inf:
            return np.max(np.abs(x), axis=0)
        return np.sum(np.abs(x) ** p, axis=0) ** (1 / p)

    if is_inf:
        return np.max(np.abs(x))
    return np.sum(np.abs(x) ** p) ** (1 / p)


def normaMatMC(A, q, p, Np):
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


nMC = normaMatMC(A=np.eye(2), q=2, p=1, Np=100000)


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

nMC = normaMatMC(A=np.eye(2), q=2, p="inf", Np=100000)
print(nMC[0])
print(nMC[1])

assert np.allclose(nMC[0], np.sqrt(2), atol=1e-3)
assert np.allclose(np.abs(nMC[1][0]), 1, atol=1e-3) and np.allclose(
    np.abs(nMC[1][1]), 1, atol=1e-3
)
A = np.array([[1, 2], [3, 4]])
nMC = normaMatMC(A=A, q="inf", p="inf", Np=1000000)
# pyrefly: ignore [bad-argument-type]
##assert np.allclose(nMC[0], normaExacta(A, "inf"), rtol=2e-1)
