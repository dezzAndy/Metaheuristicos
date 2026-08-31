"""
    Implementación de algoritmo de optimización greedy con busqueda aleatoria
"""
import random
import numpy as np
import matplotlib.pyplot as plt

def ob_f_1(x):
    """
    Función Objetivo: 5cos(x)+cos(5x)

    Args:
        Numero float aleatorio
    Returns:
        Resultados de la funcion evaluada
    """
    return 5 * np.cos(x) + np.cos(5 * x)

def ob_f_2(x):
    """
    Función Objetivo: (8sin(x) + sec(2x))^2 

    Args:
        Numero float aleatorio
    Returns:
        Resultados de la funcion evaluada
    """
    return np.power((8 * np.sin(x) + (1 / (np.cos(2 * x)))), 2)

# Hiperparametros
num_iter    = 100
range_min   = -10
range_max   = 10

# Parametros
mejor_x     = None
mejor_fitness   = float("inf")

# Lista de mejores
mejores = []

for i in range(num_iter):
    x = random.uniform(range_min, range_max)
    f = ob_f_2(x)

    if f < mejor_fitness:
        mejor_x = x
        mejor_fitness = f
    mejores.append(mejor_fitness)

# Mostrar mejores valores
print("Mejor Valor Encontrado")
print("x = ", mejor_x)
print("f(x) = ", mejor_fitness)

# Grafica plt
plt.plot(mejores, marker="o", markersize=3)
plt.xlabel("Iteración")
plt.ylabel("Mejor Fitness Encontrado")
plt.title("Mejores Fitness encontrados en Búsqueda aleatoria greedy")
plt.grid(True)
plt.show()
