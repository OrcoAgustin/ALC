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
        raise ZeroDivisionError("El valor de x no puede ser 0")
    else:
        return abs(x - y) / abs(x)


#############################################################################################
# Devuelve True si ambas matrices son iguales y False en otro caso.
# Considerar que las matrices pueden tener distintas dimensiones, ademas de distintos valores.


def matricesIguales(A, B):

    try:
        return np.allclose(A, B)
    except ValueError:
        # preguntar si vale usar el all close de np
        return False


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


def rota_y_escala(theta, s):
    rotado = rota(theta)
    escalado = escala(s)
    return escalado @ rotado


"""
version sin funciones

def rota_y_escala(theta, s):
    
    %Recibe un ángulo theta y una tira de números s, y retorna una matriz de 2 x 2 que rota el vector en un ángulo theta y luego lo escala en un factor s
    
    escalado = np.zeros((len(s), len(s)))
    for i in range(len(s)):
        escalado[i, i] = s[i]
    rotacion = np.array(
        [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
    )
    res = np.array(escalado @ rotacion)
    return res
"""


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


def transafin(v, theta, s, b):
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

# Tests para transafin
assert np.allclose(
    transafin(np.array([1, 0]), np.pi / 2, [1, 1], [0, 0]), np.array([0, 1])
)
assert np.allclose(transafin(np.array([1, 1]), 0, [2, 3], [0, 0]), np.array([2, 3]))
assert np.allclose(
    transafin(np.array([1, 0]), np.pi / 2, [3, 2], [4, 5]), np.array([4, 7])
)
