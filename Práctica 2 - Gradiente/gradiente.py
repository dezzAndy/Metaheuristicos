"""
Gradiente Descendente para Rosenbrock
"""
import numpy as np
import matplotlib.pyplot as plt

def rosenbrock(x, y):
    """
    Función de Rosenbrock
    """
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

def gradiente_rosenbrock(x: float, y: float, lr=0.001, iteraciones=10000):
    """
    Gradiente Descendente para Rosenbrock
    """
    historial_costo = []

    for _ in range(iteraciones):
        costo = rosenbrock(x, y)
        historial_costo.append(costo)
        # Derivadas parciales de la función de Rosenbrock
        dx = -2 * (1 - x) - 400 * x * (y - x ** 2)
        dy = 200 * (y - x ** 2)
        # Actualización de pesos
        x = x - lr * dx
        y = y - lr * dy

    return x, y, historial_costo

def gradiente(x: float, y: float, lr = 0.01, iteraciones: int = 10000):
    """
    Gradiente Descendente para regresión lineal
    """
    n = len(y)
    m = 0.0
    b = 0.0
    historial_costo = []

    for _ in range(iteraciones):
        # función objetivo
        y_pred = m * x + b
        costo = 1 / n * np.sum((y - y_pred) ** 2) # Calculo error cuadrático medio
        historial_costo.append(costo)
        dm = (-2 / n) * np.sum(x * (y - y_pred)) # Derivadas
        db = (-2 / n) * np.sum(y - y_pred)
        m = m - lr * dm
        b = b - lr * db
    return m, b, historial_costo

np.random.seed(42)
# Inicialización de datos para el posterior gradiente descendente
X_INICIAL = -1.0
Y_INICIAL = 2.0

x_opt, y_opt, costo_hist = gradiente_rosenbrock(X_INICIAL, Y_INICIAL, lr=0.000005, iteraciones=500)

print(f"X óptimo: {x_opt:.4f}") # Debería acercarse a 1.0
print(f"Y óptima: {y_opt:.4f}") # Debería acercarse a 1.0
print(f"Costo final: {costo_hist[-1]:.6f}") # Debería acercarse a 0.0

plt.plot(costo_hist, marker="o", markersize=3)
plt.xlabel("Iteración")
plt.ylabel("Mejor Fitness Encontrado")
plt.title("Gradiente")
plt.grid(True)
plt.show()
