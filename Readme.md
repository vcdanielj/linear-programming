| -- PROGRAMACIÓN LINEAL -- |
 
La programación lineal es un procedimiento matemático cuyo fin es optimimzar una función objetivo siguiendo una serie de restricciones en base a las variables utilizadas

En este repositorio veremos una implementación de la programación lineal utilizando el método gráfico


| -- EJERCICIO DE PROGRAMACIÓN LINEAL -- |

Una empresa de producción de alimentos quiere maximizar sus ganancias. 

Produce dos tipos de alimentos: A y B. El alimento A tiene un costo de producción de $4 por unidad y se vende por $8 por unidad. El alimento B tiene un costo de producción de $6 por unidad y se vende por $10 por unidad. 

La empresa tiene un presupuesto limitado de $2000 para la producción de ambos tipos de alimentos. Además, la empresa tiene una capacidad limitada de producción: puede producir como máximo 400 unidades del alimento A y 300 unidades del alimento B. ¿Cuántas unidades de cada tipo de alimento debe producir la empresa para maximizar sus ganancias?


| -- RESOLUCIÓN DEL EJERCICIO EN PYTHON -- |

El código comienza importando las librerías necesarias para graficar y hacer cálculos matemáticos en Python.

Luego, se definen las restricciones del problema en términos de ecuaciones lineales y se utiliza la función linspace de NumPy para generar 1000 puntos de igual separación entre 0 y 500 en el eje x1. Estos puntos se utilizan para calcular los valores correspondientes de x2 en cada restricción.

A continuación, se utiliza la función plot de Matplotlib para graficar cada restricción y se utiliza la función fill_between para rellenar las áreas correspondientes a las restricciones que se solapan. Esto produce un gráfico que muestra todas las restricciones del problema y sus intersecciones.

Después, se utiliza un bucle for para encontrar todas las intersecciones de las restricciones. Estas intersecciones se almacenan en una lista llamada intersections.

Finalmente, se utiliza otro bucle for para evaluar la función objetivo en cada intersección y encontrar la solución óptima. La solución óptima es la intersección que produce el valor máximo de la función objetivo. El código imprime la solución óptima y el valor correspondiente de la función objetivo.


| -- RECURSOS UTILIZADOS -- | 

Para la realización del ejercicio se hizo uso de:
    Python 3.10.7
    numpy 1.23.5
    matplotlib 3.6.2
