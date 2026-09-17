from numpy import shape
import numpy as np
#aux
def elim_gaussiana(A):
    if A is None:
        return None, None, 0

    cant_op = 0
    m = A.shape[0]
    n = A.shape[1]
    Ac = A.copy()
    
    if m != n:
        return None, None, 0
    
    ## desde aqui -- CODIGO A COMPLETAR
    L = np.eye(n)
    
    for k in range(n - 1):
        pivote = Ac[k, k]
        if np.isclose(pivote, 0):
            return None, None, 0    
            
        
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


#1)
def calculaLU(A):
    """
    Calcula la factorizacion LU de la matriz A y retorna las matrices L
    y U, junto con el numero de operaciones realizadas. En caso de
    que la matriz no pueda factorizarse retorna None.
    """
    resultado=elim_gaussiana(A)
    if resultado is None:
        L=None
        U=None
        cant_oper=0
    else:
        L, U, cant_oper = resultado
    
    return L, U, cant_oper 

#2)
def res_tri(L,b,inferior=True):
    """
    Resuelve el sistema Lx = b , donde L es triangular. Se puede indicar
    si es triangular inferior o superior usando el argumento
    inferior (por defecto asumir que es triangular inferior).
    """
    n = L.shape[0]
    x = np.zeros(n)

    if inferior:
        x[0]= b[0]/L[0,0] #fila 0
        for i in range(1,n):
            sumaParcial = 0
            for j in range(i):
                sumaParcial += x[j]*L[i,j]
            x[i]= (b[i]-sumaParcial)/L[i,i]
        return x
    else:
        x[n-1]= b[n-1]/L[n-1,n-1] #ultima fila n(en realidad n-1)
        for i in range(n-2,-1,-1):
            sumaParcial = 0
            for j in range(i+1,n):
                sumaParcial += x[j]*L[i,j]
            x[i]= (b[i]-sumaParcial)/L[i,i]
        return x

#3)
def inversa(A):
    """
    Calcula la inversa de A empleando la factorizacion LU
    y las funciones que resuelven sistemas triangulares.
    """
    L,U,cant_oper=calculaLU(A)
    #check por si no tiene lu
    if L is None or U is None:
        return None
    #check de "inversibilidad"
    for i in range(U.shape[0]):
        if np.isclose(U[i,i],0):
            return None
    n=L.shape[0]
    I=np.eye(n)

    #LY=I
    Y=np.zeros((n,n))        
    for i in range(n):
        Y[:,i]=res_tri(L,I[:,i])

    #UX=Y
    res=np.zeros((n,n)) #X
    for i in range(n):
        res[:,i]=res_tri(U,Y[:,i],inferior=False)

    return res
        
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(inversa(A))

#4)
def calculaLDV (A):
    """
    Calcula la factorizacion LDV de la matriz A, de forma tal que A =
    LDV, con L triangular inferior, D diagonal y V triangular
    superior. En caso de que la matriz no pueda factorizarse
    retorna None .
    """
    L,U,cant_oper=calculaLU(A)
    #check por si no tiene lu
    if L is None or U is None:
        return None , None, None
    #check por si no se puede hacer ldv
    for i in range(U.shape[0]):
        if np.isclose(U[i,i],0):
            return None, None, None
    n=np.shape(L)[0]

    #creo y relleno d con la diag de u
    D=np.zeros((n,n))
    for i in range(n):
        D[i,i]=U[i,i]

    #creo y relleno v dividiendo la fila por el factor 
    V=np.zeros((n,n))
    for i in range(n):
        V[i,:]=U[i,:]/U[i,i]

    return L,D,V
        
#5)
def esSDP(A, atol=1e-8):
    """
    Checkea si la matriz A es simetrica definida positiva (SDP) usando
    la factorizacion LDV.
    """
    L,D,V=calculaLDV(A)
    if L is None or D is None or V is None:
        return False
    for i in range(A.shape[0]):
        if np.isclose(D[i,i],0,atol=atol) or D[i,i]<0:
            return False
    return True
    
#6) Cholesky
def calculaCholesky(A,atol=1e-10):
    """
    Verifica si la matriz A es SDP y en caso afirmativo devuelve la matriz R asociada a A, tal que A = R @ R.T.
    """
    if not esSDP(A,atol):
        return None
    
    n=A.shape[0]

    L,D,V=calculaLDV(A)
    if L is None or D is None or V is None:
        return None

    R = L
    for j in range(n):
        for i in range(j, n): 
            R[i, j] = R[i, j] * np.sqrt(D[j, j])
    return R    





###Tests###
# TESTS L04-LU

# TESTS LU
print("TESTS calculaLU")

L0 = np.array([[1,0,0],
               [0,1,0],
               [1,1,1]])

U0 = np.array([[10,1,0],
               [0,2,1],
               [0,0,1]])

A =  L0 @ U0
L,U,nops = calculaLU(A)
assert(np.allclose(L,L0))
assert(np.allclose(U,U0))


L0 = np.array([[1,0,0],
               [1,1.001,0],
               [1,1,1]])

U0 = np.array([[1,1,1],
               [0,1,1],
               [0,0,1]])
A =  L0 @ U0
L,U,nops = calculaLU(A)
assert(not np.allclose(L,L0))
assert(not np.allclose(U,U0))
assert(np.allclose(L,L0,atol=1e-3))
assert(np.allclose(U,U0,atol=1e-3))
assert(nops == 13)

L0 = np.array([[1,0,0],
               [1,1,0],
               [1,1,1]])

U0 = np.array([[1,1,1],
               [0,0,1],
               [0,0,1]])

A =  L0 @ U0
L,U,nops = calculaLU(A)
assert(L is None)
assert(U is None)
assert(nops == 0)

assert(calculaLU(None) == (None, None, 0))

assert(calculaLU(np.array([[1,2,3],[4,5,6]])) == (None, None, 0))

print("-----ÉXITO!!!!\n")


## TESTS res_tri
print("TESTS res_tri")

A = np.array([[1,0,0],
              [1,1,0],
              [1,1,1]])

b = np.array([1,1,1])
assert(np.allclose(res_tri(A,b),np.array([1,0,0])))

b = np.array([0,1,0])
assert(np.allclose(res_tri(A,b),np.array([0,1,-1])))

b = np.array([-1,1,-1])
assert(np.allclose(res_tri(A,b),np.array([-1,2,-2])))

b = np.array([-1,1,-1])
assert(np.allclose(res_tri(A,b,inferior=False),np.array([-1,1,-1])))

A = np.array([[3,2,1],[0,2,1],[0,0,1]])
b = np.array([3,2,1])
assert(np.allclose(res_tri(A,b,inferior=False),np.array([1/3,1/2,1])))

A = np.array([[1,-1,1],[0,1,-1],[0,0,1]])
b = np.array([1,0,1])
assert(np.allclose(res_tri(A,b,inferior=False),np.array([1,1,1])))
print("-----ÉXITO!!!!\n")


# Test inversa
print("TESTS inversa")

def esSingular(A):
    try:
        # pyrefly: ignore [missing-attribute]
        np.linalg.inv(A)
        return False
    except:
        return True

# Por que no siempre es invertible, hacemos varios tests
ntest = 10
for i in range(ntest):
    # pyrefly: ignore [missing-attribute]
    A = np.random.random((4,4))
    A_ = inversa(A)
    if not esSingular(A):
        # pyrefly: ignore [missing-attribute]
        inversaConNumpy = np.linalg.inv(A)
        assert(A_ is not None)
        assert(np.allclose(inversaConNumpy,A_))
    else: 
        assert(A_ is None)

# Matriz singular devería devolver None
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
assert(inversa(A) is None)

print("-----ÉXITO!!!!\n")


# Test LDV:
print("TESTS calculaLDV")

L0 = np.array([[1,0,0],[1,1.,0],[1,1,1]])
D0 = np.diag([1,2,3])
V0 = np.array([[1,1,1],[0,1,1],[0,0,1]])
A =  L0 @ D0 @ V0
L,D,V = calculaLDV(A)
assert(np.allclose(L,L0))
assert(np.allclose(D,D0))
assert(np.allclose(V,V0))


L0 = np.array([[1,0,0],[1,1.001,0],[1,1,1]])
D0 = np.diag([3,2,1])
V0 = np.array([[1,1,1],[0,1,1],[0,0,1.001]])
A =  L0 @ D0  @ V0
L,D,V = calculaLDV(A)
assert(np.allclose(L,L0,1e-3))
assert(np.allclose(D,D0,1e-3))
assert(np.allclose(V,V0,1e-3))

print("-----ÉXITO!!!!\n")

# TESTS SDP
print("TESTS esSDP")

L0 = np.array([[1,0,0],[1,1,0],[1,1,1]])
D0 = np.diag([1,1,1])
A = L0 @ D0 @ L0.T
assert(esSDP(A))

D0 = np.diag([1,-1,1])
A = L0 @ D0 @ L0.T
assert(not esSDP(A))

D0 = np.diag([1,1,1e-16])
A = L0 @ D0 @ L0.T
assert(not esSDP(A))

L0 = np.array([[1,0,0],
               [1,1,0],
               [1,1,1]])
D0 = np.diag([1,1,1])
V0 = np.array([[1,0,0],
               [1,1,0],
               [1,1+1e-3,1]]).T
A = L0 @ D0 @ V0
assert(esSDP(A,1e-3))

print("-----ÉXITO!!!!\n")
print("---FINALIZADO LABO 4!---")

# TESTS Cholesky
print("TESTS calculaCholesky")

# 1. Test básico con matriz simétrica y definida positiva conocida
L0 = np.array([[2, 0, 0],
               [1, 3, 0],
               [4, 2, 1]])
A = L0 @ L0.T
L = calculaCholesky(A)
assert(L is not None)
assert(np.allclose(L, L0))
# Verificar que L es triangular inferior
assert(np.allclose(L, np.tril(L)))


# 2. Test con matriz construida a partir de L0
L0 = np.array([[1, 0, 0],
               [0.5, 1.001, 0],
               [1, 1, 1]])
A = L0 @ L0.T
L = calculaCholesky(A)

assert(L is not None)
assert(np.allclose(L, L0))       

# 3. Test con matriz no simétrica (debe fallar y devolver None)
A_no_simetrica = np.array([[4, 2, 1],
                           [1, 3, 0],
                           [4, 2, 1]])
assert(calculaCholesky(A_no_simetrica) is None)


# 4. Test con matriz simétrica pero NO definida positiva (autovalores negativos o nulos)
# Matriz con determinante negativo / autovalores no estrictamente positivos
A_no_dp = np.array([[1, 2, 1],
                    [2, 1, 2],
                    [1, 2, 1]])
assert(calculaCholesky(A_no_dp) is None)


# 5. Test con entradas inválidas
assert(calculaCholesky(None) is None)
# Matriz rectangular
assert(calculaCholesky(np.array([[1, 2, 3], [4, 5, 6]])) is None)

print("-----ÉXITO CHOLESKY!!!!\n")