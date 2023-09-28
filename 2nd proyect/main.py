from scipy.optimize import linprog
import matplotlib.pyplot as plt
import numpy as np

# Coeficientes de la función objetivo
c = [-40, -18]

# Matriz de coeficientes de las restricciones
A = [[16, 2], [6, 3], [1, 0], [0, 1]]

# Vector de términos independientes de las restricciones
b = [700, 612, 80, 120]

# Resolvemos el problema
res = linprog(c, A_ub=A, b_ub=b, method='highs')

print('Optimal value:', -res.fun, '\nX:', res.x)

# Para graficar
x = np.linspace(0, 100, 100)
y1 = (700-16*x)/2
y2 = (612-6*x)/3
y3 = 120

plt.figure()
plt.plot(x, y1, label='16x1+2x2<=700')
plt.plot(x, y2, label='6x1+3x2<=612')
plt.xlim((0, 100))
plt.ylim((0, 150))
plt.xlabel('x1')
plt.ylabel('x2')

# Rellenamos el área de soluciones factibles
plt.fill_between(x, np.maximum(y1, y2), y3, where=(x<=80), color='gray', alpha=0.5)
plt.legend()

# Mostramos el punto de solución óptima
plt.plot(res.x[0], res.x[1], 'ro')
plt.show()