import numpy as np


def normaExacta(A, p=[1, "inf"]):
    A = np.asarray(A, dtype=float)

    if isinstance(p, str):
        p = np.inf if p.strip().lower() == "inf" else float(p)

    if p == 1:
        return float(np.max(np.sum(np.abs(A), axis=0)))
    elif p == np.inf:
        return float(np.max(np.sum(np.abs(A), axis=1)))
    else:
        raise ValueError("normaExacta solo admite p=1 o p=inf")


def condExacta(A, p):
    # Que devuelve el numero de condicion de A a partir de la formula de
    # l a ecuacion (1) usando la norma p.
    normaA = normaExacta(A, p)
    aInversa = np.linalg.inv(A)
    normaAInversa = normaExacta(aInversa, p)
    return normaA * normaAInversa


A = np.random.rand(10, 10)
A_ = np.linalg.solve(A, np.eye(A.shape[0]))
normaA = normaExacta(A, 1)
normaA_ = normaExacta(A_, 1)
condA = condExacta(A, 1)
assert np.allclose(normaA * normaA_, condA)

A = np.random.rand(10, 10)
A_ = np.linalg.solve(A, np.eye(A.shape[0]))
normaA = normaExacta(A, "inf")
normaA_ = normaExacta(A_, "inf")
condA = condExacta(A, "inf")
assert np.allclose(normaA * normaA_, condA)
