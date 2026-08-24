"""
    Modulo principal que ejecuta los algoritmos de busqueda y ordenamiento.
"""
from numpy import random, zeros

#from random import randint, choice
#from algoritmos.busqueda.linear_search import linear_search
from algoritmos.busqueda.binary_search import binary_search
#from algoritmos.busqueda.jump_search import jump_search
#from algoritmos.ordenamiento.merge_sort import merge_sort
from algoritmos.ordenamiento.tim_sort import tim_sort
#from algoritmos.ordenamiento.insertion_sort import insertion_sort

# N: número de ejecuciones
N 	=	10000
# LN: Límite inferior
LN = -1
# UN: Límite superior
UN = 1
# x: Lista de floats
x = zeros(N)

# Inicialización
for i in range(N):
    x[i] = LN + random.rand() * (UN - LN)

# Imprimimos los 10 primeros numeros del array
print("Primeros 10 elementos del arreglo desordenado:")
for i in range(10):
    print(x[i])

# Guardamos el primer elemento del arreglo desordenado para buscarlo en el arreglo ordenado
prim_elmt = x[0]
print("\nPrimer elemento del arreglo actual:")
print(f"Elemento:{prim_elmt}")

# Aplicamos el insertion sort
print("\nOrdenando el arreglo con Tim Sort...")
tim_sort(x)

#insertion_sort(x, 0, len(x) - 1)

# Imprimimos los 10 primeros numeros del array ordenado
print("\nPrimeros 10 elementos del arreglo ordenado:")
for i in range(10):
    print(x[i])

RES = binary_search(x, prim_elmt)
print(f"Elemento:{x[RES]} en el indice: {RES}")
