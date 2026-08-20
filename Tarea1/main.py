"""
    Modulo principal que ejecuta los algoritmos de busqueda y ordenamiento.
"""
from random import randint, choice
from algoritmos.busqueda.linear_search import linear_search
from algoritmos.busqueda.binary_search import binary_search
from algoritmos.busqueda.jump_search import jump_search
from algoritmos.ordenamiento.merge_sort import merge_sort
from algoritmos.ordenamiento.tim_sort import tim_sort
from algoritmos.ordenamiento.insertion_sort import insertion_sort

"""
# Genera un array de 20 números aleatorios entre 1 y 100
arr1 = [randint(1, 100) for _ in range(20)]
print("Array 1 Original:\n", arr1)

# ordena el array con Tim Sort
tim_sort(arr1)
print("Array 1 Ordenado con Tim Sort:\n", arr1)

# Busca un elemento aleatorio en el array ordenado usando búsqueda binaria
print("Búsqueda binaria")
target = choice(arr1)
index = binary_search(arr1, target)
if index != -1:
    print(f"El elemento {target} encontrado en el índice {index}")
else:
    print(f"Elemento {target} no encontrado")

# Genera otro array de 20 números aleatorios entre 1 y 100
arr2 = [randint(1, 100) for _ in range(20)]
print("Array 2 Original:\n", arr2)

target = choice(arr2)
# Con la busqueda lineal, busca un elemento aleatorio en el array desordenado
print("Búsqueda lineal")
index = linear_search(arr2, target)
if index != -1:
    print(f"El elemento {target} encontrado en el índice {index}")
else:
    print(f"Elemento {target} no encontrado")

# ordena el array con Merge Sort
merge_sort(arr2, 0, len(arr2) - 1)
print("Array 2 Ordenado con Merge Sort:\n", arr2)

index = jump_search(arr2, target)
if index != -1:
    print(f"El elemento {target} encontrado en el índice {index}")
else:
    print(f"Elemento {target} no encontrado")

arr3 = [randint(1, 100) for _ in range(20)]
print("Array 3 Original:\n", arr3)
insertion_sort(arr3, 0, len(arr3) - 1)
print("Array 3 Ordenado con Insertion Sort:\n", arr3)"""

import numpy as np
# n: número de ejecuciones
n 	=	10000
# ln: Límite inferior
ln = -1
# up: Límite superior
up = 1
# x: Lista de floats
x = np.zeros(n)

# Inicialización
for i in range(n):
	x[i] = ln + np.random.rand() * (up - ln) 

# Imprimimos los 10 primeros numeros del array
for i in range(10):
    print(x[i])

# Guardamos el primer elemento del arreglo desordenado para buscarlo posteriormente
prim_elmt = x[0]
print(f"Elemento:{prim_elmt}")

# Aplicamos el insertion sort
insertion_sort(x, 0, len(x) - 1)

# 
res = binary_search(x, elemento_rand)
print(f"Elemento:{x[res]} en el indice: {res}")

print("Hola")
for i in range(10):
    print(x[i])