import numpy as np


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


assert np.allclose(normaExacta(np.array([[1, -1], [-1, -1]]), 1), 2)
assert np.allclose(normaExacta(np.array([[1, -2], [-3, -4]]), 1), 6)
assert np.allclose(normaExacta(np.array([[1, -2], [-3, -4]]), "inf"), 7)
assert normaExacta(np.array([[1, -2], [-3, -4]]), 2) is None
assert normaExacta(np.random.random((10, 10)), 1) <= 10
assert normaExacta(np.random.random((4, 4)), "inf") <= 4
