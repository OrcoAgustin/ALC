# pyrefly
import numpy as np


######################################################################################################
#Ejercicio 1. Desarrollar una funci´on esCuadrada(A) que devuelva verdadero
#si la matriz A es cuadrada y Falso en caso contrario.

def esCuadrada(A):
    #normalizamos las entradas
    array = np.array(A)
    #teoricamente esto asegura que tengan el mismo largo todas las filas, no hace falta el loop anyways we keep it 

    if np.size(array) == 0:
        return False

    for filas in array:
        if len(array) != np.size(filas):
            return False 
    
    return True 

######################################################################################################
#Ejercicio 2. Desarrollar una funci´on triangSup(A) que devuelva la matriz U
#correspondiente a la matriz Triangular Superior de A sin su diagonal.

def triangSup(A):
    #check cuadrado
    if not esCuadrada(A):
        raise ValueError("La matriz no es cuadrada")

    #creamos matriz U resultado
    U = np.array(A)
    
    #entiendo que no hay que hacer gaussiana y solamente ponerlo con 0 abajo de la diag
    for i in range(len(U)):
        for j in range(i, len(U)):
            if i == j:
                U[i][j] = 0
            if i > j:
                U[i][j] = 0
            
    return U

######################################################################################################
#Ejercicio 3. Desarrollar una funci´on triangInf(A) que devuelva la matriz L
#correspondiente a la matriz Triangular Inferior de A sin su diagonal.

def triangInf(A):
    #check cuadrado
    if not esCuadrada(A):
        raise ValueError("La matriz no es cuadrada")

    #creamos matriz L resultado
    L = np.array(A)

    for i in range(len(L)):
        for j in range(len(L)):
            if i == j:
                L[i][j] = 0
            if i < j:
                L[i][j] = 0
            
    return L

######################################################################################################
#Ejercicio 4. Desarrollar una funci´on diagonal(A) que devuelva la matriz D
#correspondiente a la matriz diagonal de A.

def diagonal(A):
    if not esCuadrada(A):
            raise ValueError("La matriz no es cuadrada")
    
    D = np.array(A) 
    for i in range(len(D)):
        for j in range(len(D)):
            if i != j:
                D[i][j]=0
    
    return D        

######################################################################################################
#Ejercicio 5. Desarrollar una funci´on traza(A) que calcule la traza de una
#matriz cualquiera A    
#traza = suma de la diag

def traza(A):
    res=0
    if not esCuadrada(A):
        raise ValueError("La matriz no es cuadrada")

    for i in range(len(A)):
        res+= A[i][i]

    return res

######################################################################################################
#Ejercicio 6. Desarrollar una funci´on traspuesta(A) que devuelva la matriz
#traspuesta de A.

def traspuesta(A):
    if not A or not A[0]:
        raise ValueError("La matriz no puede estar vacía")

    AT = np.empty((len(A[0]), len(A)))

    for i in range(len(A)):
        for j in range(len(A[0])):
            AT[j][i] = A[i][j]
    
    return AT

######################################################################################################
#Ejercicio 7. Desarrollar una funci´on esSimetrica(A) que devuelve True si la
#matriz A es sim´etrica y False en caso contrario.

def esSimetrica(A):
    if not A or not A[0]:
        raise ValueError("La matriz no puede estar vacía")

    if not esCuadrada(A):
        raise ValueError("La matriz no es cuadrada")

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i][j] != A[j][i]:
                return False
            
    return True

######################################################################################################
#Ejercicio 8. Desarrollar una funci´on calcularAx(A,x) que recibe una matriz
#A de tama˜no n × m y un vector x de largo m y devuelve un vector b de largo n
#resultado de la multiplicaci´on vectorial de la matriz y el vector.

def calcularAx(A, x):
    if not A or not A[0] or len(x)==0:
        raise ValueError("La matriz A y el vector x no pueden estar vacios")

    if len(x) !=len(A[0]):
        raise ValueError("Dimensiones incompatibles")

    b=np.zeros(len(A))

    for i in range(len(A)):
        valorF = 0
        for j in range(len(A[0])):
            valorF += A[i][j] * x[j]
        b[i] = valorF

    return b

######################################################################################################
#Ejercicio 9. Desarrollar una funci´on intercambiarFilas(A, i, j), 
#que intercambie las filas i y la j de la matriz A. El intercambio tiene que ser in-place.

def intercambiarFilas(A, i, j):
    if not A or not A[0]:
        raise ValueError("La matriz A no es valida")

    if i >= len(A) or i < 0:
        raise ValueError("no existe fila I")
    
    if j >= len(A) or j < 0:
        raise ValueError("no existe fila J")

    for k in range(len(A[0])):
        vTemp=A[i][k]
        A[i][k]=A[j][k]
        A[j][k]=vTemp
    #in place no devuelve nada

######################################################################################################
#Ejercicio 10. Desarrollar una funci´on sumar_fila_multiplo(A, i, j, s)que
#a la fila i le sume la fila j multiplicada por un escalar s. Esta es una operaci´on
#elemental clave en la eliminaci´on gaussiana. La operaci´on debe ser in-place.

def sumarFilaMultiplo(A, i, j, s):
    if not A or not A[0]:
        raise ValueError("La matriz A no es valida")

    if i >= len(A) or i < 0:
        raise ValueError("no existe fila I")
    
    if j >= len(A) or j < 0:
        raise ValueError("no existe fila J")

    for k in range(len(A)):
        A[i][k] += A[j][k] * s

######################################################################################################
#Ejercicio 11. Desarrollar una funci´on esDiagonalmenteDominante(A) que de
#vuelva True si una matriz cuadrada A es estrictamente diagonalmente dominante. 
#Esto ocurre si para cada fila, el valor absoluto del elemento en la diagonal
#es mayor que la suma de los valores absolutos de los dem´as elementos en esa fila

#aux
def abs(n):
    if n < 0:
        n = -n
    return n

def esDiagonalmenteDominante(A):
    if not esCuadrada(A):
        raise ValueError("matriz no valida")

    for i in range(len(A[0])):
        sumaFila = 0
        vDiag = abs(A[i][i])
        for j in range(len(A[0])):
            if j !=i:
                sumaFila =+ A[i][j]
        if sumaFila>vDiag:
            return False

    return True                 

######################################################################################################
#Ejercicio 12. Desarrollar una funci´on matrizCirculante(v) que genere una
#matriz circulante a partir de un vector. En una matriz circulante la primer fila
#es igual al vector v, y en cada fila se encuentra una permutaci´on c´ıclica de la
#fila anterior, moviendo los elementos un lugar hacia la derecha

def matrizCirculante(v):
    base = [[0 for _ in range(len(v))] for _ in range(len(v))]

    A = np.array(base)
    A[0]=v

    for i in range(1, len(A)):
        ultimo=v.pop()
        v.insert(0,ultimo)
        A[i] = v
    return A

######################################################################################################
#Ejercicio 13. Desarrollar una funci´on matrizVandermonde(v), donde v ∈ Rn
#y se devuelve la matriz de Vandermonde V ∈ Rn×n cuya fila i-´esima corresponde
#con la potencias (i − 1)-´esima de los elementos de v.

#aux
def potencia(n, p):
    potencia=1
    for i in range(p):
        potencia=potencia*n
    return potencia

def matrizVandermonde(v):
    base = [[0 for _ in range(len(v))] for _ in range(len(v))]
    A=np.array(base)

    for i in range(len(v)):
        fila = []
        for j in range(len(v)):
            fila.append(potencia(v[j],i))
        A[i]=fila
    return A

#esto se puede recontra optimizar pero por ahora va
######################################################################################################
#Ejercicio 14. Desarrollar una funci´on numeroAureo(n) que estime el n´umero
#aureo ϕ como Fk+1/Fk, siendo Fk el k-´esimo n´umero de la sucesi´on de Fibonacci.
#Para esto, formulen la sucesi´on de Fibonacci Fk+1 = Fk +Fk−1 de forma matricial,
# usando la semilla F0 = 0,F1 = 1. Grafique el valor aproximado de ϕ en
# funci´on del n´umero de pasos de la sucesi´on considerado.

#def numeroAureo(n):

######################################################################################################
#Ejercicio 15. Desarrollar una funci´on matrizFiboncacci(n), que genera una
#matriz A de n×n, y cada aij = Fi+j, siendo Fk el k-´esimo n´umero de la sucesi´on
#de Fibonacci (considerando F0 = 0,F1 = 1).

#aux
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1: 
        return 1
    x1, x2 = 0, 1
    for i in range(2,n +1):
      x1, x2 = x2, x1 + x2
    return x2
        
def matrizFiboncacci(n):
    if n<0:
        raise ValueError("n menor que 0")

    base = [[0 for _ in range(n)] for _ in range(n)]
    A=np.array(base)
    
    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j] = fibonacci(i+j)

    return A

######################################################################################################
#Ejercicio 16. Desarrollar una funci´on matrizHilbert(n), que genera una matriz
# de Hilbert H de n×n, y cada hij = 1/(i+j+1).

def matrizHilbert(n):
    if n<=0:
        raise ValueError("n menor que 1")
    
    H=np.empty((n,n), dtype=float)
    #vale esto de aca arriba? preguntar

    for i in range(len(H)):
        for j in range(len(H)):
            H[i][j] = 1.0/(i+j+1)

    return H

######################################################################################################
#Ejercicio 17. Usando las funciones previamente desarrolladas donde sea posible, 
#escriba una rutina que calcule los valores entre-1 y 1 de los siguientes
#polinomios:
#x^5 −x^4+x^3−x^2+x−1
#x^2 +3
#x^10 −2
#Grafique el valor de los polinomios en el rango indicado, y calcule la cantidad
#de operaciones necesarias y el espacio en memoria para generar 100 puntos
#equiespaciados entre-1 y 1. ¿C´omo crecen estos valores con n? ¿Qu´e modificar´ıa
#para hacer el c´alculo m´as eficiente?

######################################################################################################
#Ejercicio 18. Modificar la funci´on row_echelon de manera que evalue en cada
#pivot si no hay otro elemento de la misma columna con m´odulo mayor (en valor
#absoluto). En caso afirmativo hacer el swap de las filas. Esta operatoria permite
#tener mayor estabilidad num´erica