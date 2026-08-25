import math 
import matplotlib.pyplot as plt
import numpy as np
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
#3)
#Comparen el resultado de hacer 0.3 + 0.25 con el de hacer 0.3 − 0.25. ¿En
#ambos casos obtienen el resultado esperado? ¿Por qu´e?
print(0.3 + 0.25)
print(0.3 - 0.25)
print(format(0.3,'.20f'))
print(format(0.25,'.20f'))
print(format(0.3-0.25,'.20f'))

#el 0.3 no se representa bien = 0.29999999999999998890. mientras que 0.25 si xq es pot de 2

#Escriban el n´umero 0.25 en base 2. ¿C´omo queda expresado en t´erminos
#de su mantisa y exponente?
#0.25= 1.01 * 2^-2
#mantisa = 1
#exponente = -2

# Escriban el n´umero 0.3 en base 2. ¿Qu´e dificultades aparecen al escribir
#0.3 en binario? ¿Se puede escribir exactamente con una mantisa finita?
#0.3 = 00111110100110011001100110011010 pero esto tiene error  de aprox 0.000000011920928955078125

###############################################################################
#Ejercicio 4 (No tan distintos). En este punto exploraremos expresiones que
#son aparentemente iguales.

#¿Cu´anto da (√2)^2 − 2?
#Simb´olicamente sabemos que el resultado es 0, pero ¿qu´e ocurre en python?
#Importen la librer´ıa numpy (import numpy as np) para emplear la funci´on
#np.sqrt y calculen np.sqrt(2)**2-

print(np.sqrt(2)**2-2)
# Dominio
# Dominio centrado en 0 en escala de micro-intervalo
x = np.linspace(-1e-7, 1e-7, 2000)

# Ambas fórmulas
y_inestable = np.sqrt(2 * (x**2) + 1) - 1
y_estable = (2 * (x**2)) / (np.sqrt(2 * (x**2) + 1) + 1)

# Graficar
plt.figure(figsize=(9, 5))
plt.plot(
    x,
    y_inestable,
    color='crimson',
    linewidth=1.5,
    label=r'$y = \sqrt{2x^2+1}-1$',
)
plt.plot(
    x,
    y_estable,
    color='teal',
    linewidth=2,
    linestyle='--',
    label=r'$y = \frac{2x^2}{\sqrt{2x^2+1}+1}$',
)

# Ejes y formato
plt.axhline(0, color='black', linewidth=0.6, linestyle=':')
plt.axvline(0, color='black', linewidth=0.6, linestyle=':')
plt.grid(True, linestyle=':', alpha=0.6)

plt.title(
    r'Comparación cerca de $x = 0$ ($|x| \leq 10^{-7}$)', fontsize=12
)
plt.xlabel('x', fontsize=11)
plt.ylabel('y', fontsize=11)
plt.legend(loc='upper center', fontsize=10)

plt.tight_layout()
plt.show()

#claramente conviene usar la segunda ecuacion
###############################################################################
#5)
#(Acumulaci´on del error). Calculen algebr´aicamente el l´ımite cuando
#n → ∞ de esta sucesi´on

def acumulacionDeError():
    l = []
    x = np.sqrt(2)
    sqrt2 = np.sqrt(2)

    for i in range(65):
        l.append(x)
        x = (x * x) / sqrt2

    return graficarError(l)

def graficarError(l):
    fig, ax = plt.subplots()
    ax.plot(l, color="blue", linestyle="--", label="Error de aproximación")
    ax.set_yscale('log')
    ax.set_title("Acumulación de Error")
    ax.set_xlabel("Iteración (n)")
    ax.set_ylabel("Valor de $x_n$ (Escala Logarítmica)")
    ax.legend()
    ax.grid(True, which="both", ls=":", alpha=0.5)

    plt.show()


acumulacionDeError()

###############################################################################
#6)Ejercicio 6 (Series). Comparen el resultado de calcular

#referenciar pdf para series

#para n = 6, 7, usando precisi´on de 64 y 32 bits. Para eso, aprovechen la siguiente
#pieza de c´odigo

n = 7
s = np.float32(0)
for i in range(1,10**n+1):
    s = s + np.float32(1/i)
print('suma en 64 = ', s)

limit = 5 *10**6

s = np.float32(0)
for i in range(1,5*10**n+1):
    if i==limit:
        print("s:" + format(s,'.20f'))
    s = s + np.float32(1/i)
print('suma en 32 = ', s)


#0.0000000596
#0.0000001
#0.0000001192