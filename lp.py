import matplotlib.pyplot as plt
import numpy as np

"""
Aquí, x1 y x2 son las variables de decisión. x1 representa la cantidad de alimento A y x2 representa la cantidad de alimento B. Las ecuaciones x2_1, x2_2, x2_3, y x2_4 representan las restricciones del problema.
"""

x1 = np.linspace(0, 500, 1000)
x2_1 = (2000 - 4*x1)/6
x2_2 = np.zeros_like(x1)
x2_3 = np.minimum(300, np.zeros_like(x1) + 1e10)
x2_4 = np.maximum(0, 300 - x1)

"""
Estas líneas grafican las restricciones del problema en un gráfico 2D.
"""

plt.plot(x1, x2_1, label='4x1 + 6x2 <= 2000')
plt.plot(x1, x2_2, label='x1 <= 400')
plt.plot(x1, x2_3, label='x2 <= 300')
plt.plot(x1, x2_4, label='x2 >= 0')

"""
Estas líneas rellenan el área factible del gráfico, que es el área que satisface todas las restricciones.
"""

plt.fill_between(x1, 0, x2_3, where=x1<=400, alpha=0.2)
plt.fill_between(x1, x2_4, 300, where=x1<=400, alpha=0.2)
plt.fill_between(x1, x2_4, x2_1, where=(x2_1<=300) & (x1<=400), alpha=0.2)

plt.xlim(0, 500)
plt.ylim(0, 500)
plt.xlabel('Cantidad de alimento A')
plt.ylabel('Cantidad de alimento B')
plt.legend()
plt.show()

"""
Estas líneas encuentran los puntos de intersección de las restricciones, que son los posibles puntos de solución.
"""

intersections = []
for i in range(len(x1)):
    if x2_1[i] <= 300 and x1[i] <= 400:
        intersections.append((x1[i], x2_1[i]))
    if x1[i] == 400:
        intersections.append((x1[i], 0))
    if x2_4[i] == 300:
        intersections.append((0, x2_4[i]))

"""
Estas líneas calculan el valor de la función objetivo (Z) para cada punto de intersección y encuentran la solución óptima, que es el punto que maximiza la función objetivo.
"""

Z_values = []
for point in intersections:
    Z = 8*point[0] + 10*point[1]
    Z_values.append(Z)

optimal_solution = intersections[np.argmax(Z_values)]
optimal_profit = np.max(Z_values)

print(f"La solución óptima es producir {optimal_solution[0]} unidades del alimento A y {optimal_solution[1]} unidades del alimento B, lo que generará ganancias máximas de ${optimal_profit}")