#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eliminacion Gausianna
"""
import numpy as np

def elim_gaussiana(A):
    cant_op = 0
    m=A.shape[0]
    n=A.shape[1]
    Ac = A.copy()
    
    if m!=n:
        print('Matriz no cuadrada')
        return
    
    ## desde aqui -- CODIGO A COMPLETAR
    L = np.eye(n)
    
    for k in range(n - 1):
        pivote = Ac[k, k]
        if np.isclose(pivote, 0):
            print(f"Pivote nulo en la etapa {k}")
            return None, None, cant_op
        
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


def main():
    n = 7
    B = np.eye(n) - np.tril(np.ones((n,n)),-1) 
    B[:n,n-1] = 1
    print('Matriz B \n', B)
    
    L,U,cant_oper = elim_gaussiana(B)
    
    print('Matriz L \n', L)
    print('Matriz U \n', U)
    print('Cantidad de operaciones: ', cant_oper)
    print('B=LU? ' , 'Si!' if np.allclose(np.linalg.norm(B - L@U, 1), 0) else 'No!')
    print('Norma infinito de U: ', np.max(np.sum(np.abs(U), axis=1)) )

if __name__ == "__main__":
    main()
    
    
