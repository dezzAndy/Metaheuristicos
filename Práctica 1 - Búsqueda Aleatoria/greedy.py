"""
    Implementación de algoritmo de búsqueda aleatoria greedy
"""

from numpy import zeros, random

UN = 1
LN = -1
N = 10
X = zeros(N)
EXIST = 0

# Inicialización
print("Inicializando arreglo...")
for i in range(N):
    X[i] = LN + random.rand() * (UN - LN)

for i in range(N):
    if X[i] >= 0.9:
        EXIST = 1
        X_best = X[i]
        break
if EXIST == 1:
    print(f"Best: {X_best}")
else:
    print("No hay we")