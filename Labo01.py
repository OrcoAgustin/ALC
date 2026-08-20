import math 

#1) Utilizar format() para verificar si la respuesta es correcta.

x = 0.1 + 0.1 + 0.1
y = 0.3
print(format(x))
print(format(y))
print(x == y)
#es correcto que de false

###############################################################################
#Ejercicio 2. Correr el siguiente programa en Python. Identificando la fuente
#del error, proponer una forma de solucionar su mal funcionamiento.

#a = 1.0
#while a != 0.1:
#    print(a)
#    a = a - 0.1
#print('fin')

#1.0  
#0.9
#0.8
#0.7000000000000001
#0.6000000000000001
#0.5000000000000001
#0.40000000000000013
#0.30000000000000016
#0.20000000000000015
#0.10000000000000014
#1.3877787807814457e-16
#recordemos que 0.1 no es exacto en python.
#usando algo que tenga en cuenta el error, isclose?
a=1.0
while math.isclose(a,0.1):
    print(a)
    a=a-0.1
print('fin')

###############################################################################
