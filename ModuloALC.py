import numpy as np


#############################################################################################
##### Laboratorio 1 #########################################################################
#############################################################################################
# Recibe dos numeros x e y, y calcula el error de aproximar x usando y en float64
def error(x, y):
    return abs(x - y)


#############################################################################################
# Recibe dos numeros x e y, y calcula el error relativo de aproximar x usando y en float64


def errorRelativo(x, y):
    if x == 0:
        return error
    else:
        return abs(x - y) / abs(x)


#############################################################################################
# Devuelve True si ambas matrices son iguales y False en otro caso.
# Considerar que las matrices pueden tener distintas dimensiones, ademas de distintos valores.


def matricesIguales(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if not (np.isclose(A[i][j], B[i][j])):
                return False
    return True


###### Pruebas de laboratorio 1 ##############################################################


def sonIguales(x, y, atol=1e-08):
    return np.allclose(error(x, y), 0, atol=atol)


def main():
    assert not sonIguales(1, 1.1)
    assert sonIguales(1, 1 + np.finfo("float64").eps)
    assert not sonIguales(1, 1 + np.finfo("float32").eps)
    assert not sonIguales(np.float16(1), np.float16(1) + np.finfo("float32").eps)
    assert sonIguales(np.float16(1), np.float16(1) + np.finfo("float16").eps, atol=1e-3)

    assert np.allclose(errorRelativo(1, 1.1), 0.1)
    assert np.allclose(errorRelativo(2, 1), 0.5)
    assert np.allclose(errorRelativo(-1, -1), 0)
    assert np.allclose(errorRelativo(1, -1), 2)

    assert matricesIguales(np.diag([1, 1]), np.eye(2))
    assert matricesIguales(
        np.linalg.inv(np.array([[1, 2], [3, 4]])) @ np.array([[1, 2], [3, 4]]),
        np.eye(2),
    )
    assert not matricesIguales(np.array([[1, 2], [3, 4]]).T, np.array([[1, 2], [3, 4]]))
    print("corrio")


#############################################################################################
##### Laboratorio 2 #########################################################################
#############################################################################################
# Recibe un angulo theta y retorna una matriz de 2x2
# que rota un vector dado en un angulo theta


def rota(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


#############################################################################################
# Recibe una tira de numeros s y retorna una matriz cuadrada de n x n, donde n es el tamano de s.
# La matriz escala la componente i de un vector de Rn en un factor s[i]


def escala(s):
    if len(s) == 0:
        raise ValueError("s no puede ser una tira de tamaño 0")
    res = np.zeros((len(s), len(s)))
    for i in range(len(s)):
        res[i, i] = s[i]
    return res


#############################################################################################
# Recibe un ángulo theta y una tira de números s,
# y retorna una matriz de 2x2 que rota el vector en un ángulo theta
# y luego lo escala en un factor s.

"""
def rota_y_escala(theta, s):
    rotado = rota(theta)
    escalado = escala(s)
    return escalado @ rotado


"""
# version sin funciones


def rota_y_escala(theta, s):

    # Recibe un ángulo theta y una tira de números s, y retorna una matriz de 2 x 2 que rota el vector en un ángulo theta y luego lo escala en un factor s

    escalado = np.zeros((2, 2))
    escalado[0][0] = s[0]
    escalado[1][1] = s[1]
    rotacion = np.array(
        [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
    )

    res = np.array(escalado @ rotacion)
    return res


#############################################################################################
# Recibe un ángulo theta, una tira de números s (en R2), y un vector b en R2.
# Retorna una matriz de 3x3 que rota el vector en un ángulo theta,
# luego lo escala en un factor s y por último lo mueve en un valor fijo b.


def afin(theta, s, b):
    res = np.zeros((3, 3))
    res[0:2, 0:2] = rota_y_escala(theta, s)
    res[0:2, 2] = b
    res[2, 2] = 1
    return res


"""
version sin funciones 

def afin(theta,s,b):
  
  % Recibe un ángulo theta, una tira de números s (en R2), y un vector b en (R2) y retorna una matriz de 3 x 3 que rota el vector en un ángulo theta, luego lo escala en un factor s y por último lo muevo en un valor fijo b

  escalado = np.zeros((len(s), len(s)))
  for i in range(len(s)):
      escalado[i, i] = s[i]
  rotacion = np.array(
        [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
  rotayescala = escalado @ rotacion
  res = np.zeros((3, 3))
  res[0:2, 0:2] = rotayescala
  res[0:2, 2] = b
  res[2, 2] = 1
  return res


"""


#############################################################################################
# Recibe un vector v (en R2), un ángulo theta,
# una tira de números s (en R2), y un vector b en R2.
# Retorna el vector w resultante de aplicar la transformación afín a v.


def trans_afin(v, theta, s, b):
    A = afin(theta, s, b)
    vExtendida = np.array([v[0], v[1], 1])
    res = A @ vExtendida
    return np.array([res[0], res[1]])


"""
version sin funciones 
def trans_afin(v,theta,s,b):
  
  % Recibe un vector v (en R2), un ángulo theta, una tira de números s (en R2), y un vector b en (R2) y retorna el vector w resultante de aplicar la transformacion afin a v
  
  escalado = np.zeros((len(s), len(s)))
  for i in range(len(s)):
      escalado[i, i] = s[i]
  rotacion = np.array(
        [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
  rotayescala = escalado @ rotacion
  afin = np.zeros((3, 3))
  afin[0:2, 0:2] = rotayescala
  afin[0:2, 2] = b
  afin[2, 2] = 1
  
  vExtendida =np.array([v[0],v[1],1])
  res = afin @ vExtendida
  return np.array([res[0],res[1]])
"""

###### Pruebas de laboratorio 2 ##############################################################
# Tests  para rota
assert np.allclose(rota(0), np.eye(2))
assert np.allclose(rota(np.pi / 2), np.array([[0, -1], [1, 0]]))
assert np.allclose(rota(np.pi), np.array([[-1, 0], [0, -1]]))

# Tests para escala
assert np.allclose(escala([2, 3]), np.array([[2, 0], [0, 3]]))
assert np.allclose(escala([1, 1, 1]), np.eye(3))
assert np.allclose(escala([0.5, 0.25]), np.array([[0.5, 0], [0, 0.25]]))

# Tests para rotayescala
assert np.allclose(rota_y_escala(0, [2, 3]), np.array([[2, 0], [0, 3]]))
assert np.allclose(rota_y_escala(np.pi / 2, [1, 1]), np.array([[0, -1], [1, 0]]))
assert np.allclose(rota_y_escala(np.pi, [2, 2]), np.array([[-2, 0], [0, -2]]))

# Tests para afin
assert np.allclose(afin(0, [1, 1], [1, 2]), np.array([[1, 0, 1], [0, 1, 2], [0, 0, 1]]))

assert np.allclose(
    afin(np.pi / 2, [1, 1], [0, 0]), np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
)

assert np.allclose(afin(0, [2, 3], [1, 1]), np.array([[2, 0, 1], [0, 3, 1], [0, 0, 1]]))

# Tests para trans_afin
assert np.allclose(
    trans_afin(np.array([1, 0]), np.pi / 2, [1, 1], [0, 0]), np.array([0, 1])
)
assert np.allclose(trans_afin(np.array([1, 1]), 0, [2, 3], [0, 0]), np.array([2, 3]))
assert np.allclose(
    trans_afin(np.array([1, 0]), np.pi / 2, [3, 2], [4, 5]), np.array([4, 7])
)


#############################################################################################
##### Laboratorio 3 #########################################################################
#############################################################################################


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


#############################################################################################
"""
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
"""


def normaliza(X, p):
    # Recibe X, una lista de vectores no vacios , y un escalar p. Devuelve
    # una lista donde cada elemento corresponde a normalizar los
    # elementos de X con la norma p.

    res = []
    for x in X:
        res.append(x / norma(x, p))
    return res


#############################################################################################


import numpy as np


def normaMatMC(A, q, p, Np):
    n = A.shape[1]
    X = np.random.rand(n, Np)
    normaX = X / norma(X, p)
    Y = A @ normaX
    normaY = norma(Y, p)
    maximaNorma = 0
    id = 0
    for i in range(Np):
        if normaY[i] > maximaNorma:
            maximaNorma = normaY[i]
            id = i
    x_opt = normaX[:, id]

    return maximaNorma, x_opt


#############################################################################################


def normaExacta(A, p=[1, "inf"]):
    es_escalar = not isinstance(p, (list, tuple, np.ndarray))
    if es_escalar:
        p = [p]

    A = np.asarray(A, dtype=float)
    res = []

    for norma_tipo in p:
        if norma_tipo == 1:
            res.append(float(np.max(np.sum(np.abs(A), axis=0))))
        elif norma_tipo in ["inf", float("inf"), np.inf]:
            res.append(float(np.max(np.sum(np.abs(A), axis=1))))
        else:
            return None

    return res[0] if es_escalar else res


normaExacta(A=np.array([[1, -2, 3], [-4, 5, -6]]))
#############################################################################################


def condMC(A, p):
    # Devuelve el numero de condicion de A usando la norma inducida p.
    return 0


#############################################################################################


def condExacta(A, p):
    # Que devuelve el numero de condicion de A a partir de la formula de
    # l a ecuacion (1) usando la norma p.
    return 0


#############################################################################################
# pruebas labo 3
# Tests norma
assert np.allclose(norma(np.array([1, 1]), 2), np.sqrt(2))
assert np.allclose(norma(np.array([1] * 10), 2), np.sqrt(10))
assert norma(np.random.rand(10), 2) <= np.sqrt(10)
assert norma(np.random.rand(10), 2) >= 0

# Tests normaliza
for x in normaliza([np.array([1] * k) for k in range(1, 11)], 2):
    assert np.allclose(norma(x, 2), 1)
for x in normaliza([np.array([1] * k) for k in range(2, 11)], 1):
    print(not np.allclose(norma(x, 2), 1))
for x in normaliza([np.random.rand(k) for k in range(1, 11)], "inf"):
    assert np.allclose(norma(x, "inf"), 1)


# Tests normaExacta

assert np.allclose(normaExacta(np.array([[1, -1], [-1, -1]]), 1), 2)
assert np.allclose(normaExacta(np.array([[1, -2], [-3, -4]]), 1), 6)
assert np.allclose(normaExacta(np.array([[1, -2], [-3, -4]]), "inf"), 7)
assert normaExacta(np.array([[1, -2], [-3, -4]]), 2) is None
assert normaExacta(np.random.random((10, 10)), 1) <= 10
assert normaExacta(np.random.random((4, 4)), "inf") <= 4

# Test normaMC

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
assert np.allclose(nMC[0], normaExacta(A, "inf"), rtol=2e-1)
"""
# Test condMC

A = np.array([[1, 1], [0, 1]])
A_ = np.linalg.solve(A, np.eye(A.shape[0]))
normaA = normaMatMC(A, 2, 2, 10000)
normaA_ = normaMatMC(A_, 2, 2, 10000)
condA = condMC(A, 2, 10000)
assert np.allclose(normaA[0] * normaA_[0], condA, atol=1e-3)

A = np.array([[3, 2], [4, 1]])
A_ = np.linalg.solve(A, np.eye(A.shape[0]))
normaA = normaMatMC(A, 2, 2, 10000)
normaA_ = normaMatMC(A_, 2, 2, 10000)
condA = condMC(A, 2, 10000)
assert np.allclose(normaA[0] * normaA_[0], condA, atol=1e-3)

# Test condExacta

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
"""
