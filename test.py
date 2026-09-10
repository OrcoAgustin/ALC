def test_esCuadrada():
    # Caso matriz cuadrada válida (lista de listas)
    assert esCuadrada([[1, 2], [3, 4]]) == True
    # Caso matriz cuadrada válida (np.ndarray)
    assert esCuadrada(np.array([[1, 0], [0, 1]])) == True
    # Caso matriz no cuadrada (rectángular)
    assert esCuadrada([[1, 2, 3], [4, 5, 6]]) == False
    # Caso vector unidimensional
    assert esCuadrada([1, 2, 3]) == False
    print("test_esCuadrada: OK")


def test_triangSup():
    # Matriz de prueba 3x3
    A = [[2.0, 1.0, 1.0],
         [4.0, 3.0, 3.0],
         [8.0, 7.0, 9.0]]
    
    # La eliminación gaussiana de A resulta en:
    # U_completa = [[2, 1, 1], [0, 1, 1], [0, 0, 2]]
    # Sin la diagonal principal debe quedar:
    # U_esperada = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
    
    esperado = np.array([[0.0, 1.0, 1.0],
                         [0.0, 0.0, 1.0],
                         [0.0, 0.0, 0.0]])
    
    resultado = triangSup(A)
    
    # Verificar que el resultado es correcto dentro de un margen razonable
    assert np.allclose(resultado, esperado)
    
    # Verificar que la matriz A original NO fue mutada
    assert A[0][0] == 2.0
    
    # Test con pivote nulo inicial (requiere intercambio de filas)
    A_pivote_cero = [[0.0, 2.0],
                     [3.0, 1.0]]
    resultado_pivote = triangSup(A_pivote_cero)
    esperado_pivote = np.array([[0.0, 1.0],
                                [0.0, 0.0]])
    assert np.allclose(resultado_pivote, esperado_pivote)
    
    print("test_triangSup: OK")


if __name__ == "__main__":
    test_esCuadrada()
    test_triangSup()