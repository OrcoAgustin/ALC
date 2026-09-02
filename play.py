import numpy as np


def rota_y_escala(theta, s):
    """
    % Recibe un ángulo theta y una tira de números s, y retorna una matriz de 2 x 2 que rota el vector en un ángulo theta y luego lo escala en un factor s
    """
    escalado = np.zeros((len(s), len(s)))
    for i in range(len(s)):
        escalado[i, i] = s[i]
    rotacion = np.array(
        [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
    )
    res = np.array(escalado @ rotacion)
    return res


# Tests para rotayescala
assert np.allclose(rota_y_escala(0, [2, 3]), np.array([[2, 0], [0, 3]]))
assert np.allclose(rota_y_escala(np.pi / 2, [1, 1]), np.array([[0, -1], [1, 0]]))
assert np.allclose(rota_y_escala(np.pi, [2, 2]), np.array([[-2, 0], [0, -2]]))
# Rotación de 90° con escala anisotrópica (prueba el orden S @ R)
assert np.allclose(rota_y_escala(np.pi / 2, [2, 3]), np.array([[0, -2], [3, 0]]))
# Ángulo de 45° con s = [sqrt(2), sqrt(2)]
assert np.allclose(
    rota_y_escala(np.pi / 4, [np.sqrt(2), np.sqrt(2)]), np.array([[1, -1], [1, 1]])
)

# Rotación horaria (-90°)
assert np.allclose(rota_y_escala(-np.pi / 2, [1, 1]), np.array([[0, 1], [-1, 0]]))

# Identidad completa (neutro)
assert np.allclose(rota_y_escala(0, [1, 1]), np.eye(2))
assert np.allclose(rota_y_escala(2 * np.pi, [1, 1]), np.eye(2))
# Reflexión sobre eje Y sin rotación
assert np.allclose(rota_y_escala(0, [-1, 1]), np.array([[-1, 0], [0, 1]]))

# Colapso de dimensión (escala 0 en X)
assert np.allclose(rota_y_escala(0, [0, 2]), np.array([[0, 0], [0, 2]]))
# Transformación aplicada a un vector
v = np.array([1, 0])
M = rota_y_escala(np.pi / 2, [3, 5])
assert np.allclose(M @ v, np.array([0, 5]))
