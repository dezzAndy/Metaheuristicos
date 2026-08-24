""" 
    # Materia: Algoritmos Metaheuristicos
    # Tarea 1: Algoritmos de optimización
    # 24/10/2026

    # Instrucciones:
    Realice un algoritmo de búsqueda, un algoritmo de ordenamiento y combinelos para obtener un 
    algoritmo de optimización rudimentario. Pruebe el codigo mediante la función de inicialización 
    poblacional adjunta:
    x[] = LN + rand() * (UN - LN)
"""
from numpy import zeros, random
from algoritmos.busqueda.binary_search_optimizador import binary_search
from algoritmos.ordenamiento.tim_sort import tim_sort

# N: número de elementos
N 	=	10000
# LN: Límite inferior
LN = -1
# UN: Límite superior
UN = 1
# x: Lista de floats
x = zeros(N)

# Inicialización
print("Inicializando arreglo...")
for i in range(N):
    x[i] = LN + random.rand() * (UN - LN)

# Aplicamos el Tim sort
print("\nOrdenando el arreglo con Tim Sort...")
tim_sort(x)

# Realmente, para encontrar los mejores elementos de un arreglo ordenado es tan simple como
# buscar el primer y último elemento del arreglo, de la siguiente manera:
print("\nPicos globales en theta(1):")
print("Elemento mayor: "    + str(x[-1]))
print("Elemento menor: "    + str(x[0]))

# Pero para efectos de la tarea, se implementó un Binary Search modificado para encontrar el
# mejor elemento mayor o menor a nuestro target.

# Tomamos un target aleatorio
target = LN + random.rand() * (UN - LN)
print("\nTarget: " + str(target))

# Buscamos el mejor elemento mayor a nuestro target
best_index = binary_search(x, target, "best")
if best_index != -1:
    print("Mejor elemento mayor a nuestro target: " + str(x[best_index]))
else:
    print("No se encontró un elemento mayor a nuestro target.")
