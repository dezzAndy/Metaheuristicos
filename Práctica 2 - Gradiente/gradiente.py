import numpy as np
import matplotlib.pyplot as plt

def Gradiente(x, y, LR = 0.01, iter = 10000):
    n = len(y)
    m = 0.0
    b = 0.0
    historial_costo = []

    for i in range(iter):
        # función objetivo
        y_pred = m * x * 8 * np.sin(x) + b
        # y_pred = m * x + b
        costo = 1 / n * np.sum(x * (y - y_pred) ** 2) # Calculo error cuadrático medio
        historial_costo.append(costo)
        dm = (-2 / n) * np.sum(x * (y - y_pred)) # Derivadas
        db = (-2 / n) * np.sum(y - y_pred)
        m = m - LR * dm
        b = b = LR * db
    return m, b, historial_costo

np.random.seed(42)
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([5, 7, 9, 11, 13], dtype=float)

m_opt, b_opt, costo_hist = Gradiente(X, Y, LR=0.000005, iter=500)

print(f"Pendiente óptimo (m): {m_opt:.4f}")
print(f"Intersección óptima (b): {b_opt:.4f}")
print(f"Costo final: {costo_hist[-1]:.6f}")

plt.plot(costo_hist, marker="o", markersize=3)
plt.xlabel("Iteración")
plt.ylabel("Mejor Fitness Encontrado")
plt.title("Gradiente")
plt.grid(True)
plt.show()

# agregar grafico //
# cambiar linea 10