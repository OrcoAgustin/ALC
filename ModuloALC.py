import numpy as np

#############################################################################################
##### Laboratorio 1 #########################################################################
#############################################################################################
#1)Recibe dos numeros x e y, y calcula el error de aproximar x usando y en float64
def error(x,y):
    return abs(x-y)
    #preguntar si se refiere a esto

#Recibe dos numeros x e y, y calcula el error relativo de aproximar x usando y en float64    

def errorRelativo(x,y):
    if x==0:
        raise ZeroDivisionError("El valor de x no puede ser 0")
    else:
        return abs(x-y)/abs(x)
        
#############################################################################################
#Devuelve True si ambas matrices son iguales y False en otro caso.
#Considerar que las matrices pueden tener distintas dimensiones, ademas de distintos valores.

def matricesIguales(A,B):
    
    try:
        return np.allclose(A, B)
    except ValueError:
        # preguntar si vale usar el all close de np
        return False
    
#############################################################################################
#pruebas

def sonIguales(x,y,atol=1e-08):
    return np.allclose(error(x,y),0,atol=atol)

def main():
    assert(not sonIguales(1,1.1))
    assert(sonIguales(1,1 + np.finfo('float64').eps))
    assert(not sonIguales(1,1 + np.finfo('float32').eps))
    assert(not sonIguales(np.float16(1),np.float16(1) + np.finfo('float32').eps))
    assert(sonIguales(np.float16(1),np.float16(1) + np.finfo('float16').eps,atol=1e-3))

    assert(np.allclose(errorRelativo(1,1.1),0.1))
    assert(np.allclose(errorRelativo(2,1),0.5))
    assert(np.allclose(errorRelativo(-1,-1),0))
    assert(np.allclose(errorRelativo(1,-1),2))

    assert(matricesIguales(np.diag([1,1]),np.eye(2)))
    assert(matricesIguales(np.linalg.inv(np.array([[1,2],[3,4]]))@np.array([[1,2],[3,4]]),np.eye(2)))
    assert(not matricesIguales(np.array([[1,2],[3,4]]).T,np.array([[1,2],[3,4]])))  
    print("corrio")

#############################################################################################
##### Laboratorio 2 #########################################################################
#############################################################################################


