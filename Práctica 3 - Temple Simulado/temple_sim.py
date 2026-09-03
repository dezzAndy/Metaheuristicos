"""
    Implementación del algoritmo Temple Simulado
"""
import numpy as np
import math
import random
import matplotlib.pyplot as plt

# Definición de funciones

def ackley(x, y):
    """
        Función de Ackley.
        
        Args:
            x: Coordenada X.
            y: Coordenada Y.

        Returns:
            Función evaluada.
    """
    return -20 * np.exp(-0.2 * np.sqrt((x**2 + y**2) / 2) - np.exp(np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y) / 2) + 0.2 + np.exp(1))


#def peaks(x, y):
 #   return 3*(1-x)**2 * np.exp(-(x**2) - (y+1)**2) - 10*(x/5 - x**3 - y**5) * np.exp(-x**2 - y**2) - 1/3*np.exp(-(x + 1) ** 2 - y**2)

# Función objetivo que toma un vector
def objective_function(position):
    x, y = position
    return ackley(x, y)

# Límites del espacio de búsqueda
lower_bound = np.array([-3, -3])
upper_bound = np.array([3, 3])

# Generar vecino dentro de los límites
def neighbor(position, step_size=0.5):
    new_position = position + np.random.uniform(-step_size, step_size, size=2)
    return np.clip(new_position, lower_bound, upper_bound)

# Probalidad de aceptación
def acceptance_probability(current_energy, neighbor_energy, temperature):
    if neighbor_energy < current_energy:
        return 1.0
    return math.exp((current_energy - neighbor_energy) / temperature)

# Similitud Anneling con historial posiciones
def simulated_annealing(initial_solution, initial_tempeture, cooling_rate, max_iterations):
    current_solution = initial_solution
    current_energy = objective_function(current_solution)

    best_solution = current_solution
    best_energy = current_energy

    temperature = initial_tempeture
    path = [current_solution.copy()] # Guarda la trayectoria

    for iteration in range(max_iterations):
        new_solution = neighbor(current_solution)
        new_energy = objective_function(new_solution)
        if acceptance_probability(current_energy, new_energy, temperature) > random.random():
            current_solution = new_solution
            current_energy = new_energy
            path.append(current_solution.copy())

        if current_energy < best_energy:
            best_solution = current_solution
            best_energy = current_energy

        temperature *= cooling_rate

    return best_solution, best_energy, path

# ---------------------
# Parámetros
# ---------------------

initial_solution = np.random.uniform(lower_bound, upper_bound)
initial_temperature = 1000
cooling_rate = 0.95
max_iterations = 1000

# Ejecutar algoritmo
best_solution, best_energy, path = simulated_annealing(
    initial_solution,
    initial_temperature,
    cooling_rate,
    max_iterations
)

# ---------------------
# Visualización
# ---------------------

# Crear malla para el gráfico
x = np.linspace(lower_bound[0], upper_bound[0], 300)
y = np.linspace(lower_bound[1], upper_bound[1], 300)
X, Y = np.meshgrid(x, y)
Z = ackley(X, Y)

# Convertir trayectoria a arrays
path = np.array(path)
px, py = path[:, 0], path[:, 1]

plt.figure(figsize=(10, 8))
# Contornos de la función
contour = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(label='f(x, y)')

# Ruta seguida por el algoritmo
plt.plot(px, py, color='white', linestyle='-', linewidth=2, label='Trayectoria')

# Punto inicial
plt.plot(px[0], py[0], 'o', color='red', label='Inicio')

# Mejor solución
plt.plot(best_solution[0], best_solution[1], 'x', color='cyan', markersize=10, label='Mejor solución')

plt.title("Simulated Annealing (Minimización)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.xlim(lower_bound[0], upper_bound[0])
plt.ylim(lower_bound[1], upper_bound[1])
plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection = "3d")

ax.plot(px[0], py[0], 'o', color = 'red', label = 'Inicio')
ax.plot(best_solution[0], best_solution[1], 'x', color = 'cyan', markersize = 10, label = 'Mejor solución')
ax.plot(px, py, color='white', linestyle = '-', linewidth=2, label='Trayectoria')

plt.show()

# ---------------------
# Resultado final
# ---------------------
print("\nRESULTADO FINAL:")
print(f"Mejor solución encontrada: x = {best_solution[0]:.5f}, y = {best_solution[1]:.5f}")
print(f"Valor mínimo de f(x, y) = {best_energy:.5f}")