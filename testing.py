import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 500, 1000)
x2 = np.linspace(0, 500, 1000)
x2_1 = (2000 - 4*x1)/6
x2_2 = np.zeros_like(x1)
x2_3 = np.minimum(300, np.zeros_like(x1) + 1e10)
x2_4 = np.maximum(0, 300 - x1)

plt.plot(x1, x2_1, label='4x1 + 6x2 <= 2000')
plt.plot(x1, x2_2, label='x1 <= 400')
plt.plot(x1, x2_3, label='x2 <= 300')
plt.plot(x1, x2_4, label='x2 >= 0')

plt.show()