# Alejandra Rivera Valenzuela NC 0200
# Array indexing in NumPy
import numpy as np
print("---Indexación en Arreglos 1D (Unidimensional)-0200---")
n0120 = np.array([10, 20, 30, 40, 50])
print(n0120)
print(n0120[0])   # Accede al primer elemento -> 10
print(n0120[3])   # Accede al cuarto elemento -> 40
print(n0120[-1])  # Accede al último elemento -> 50
print(n0120[-2])  # Accede al penúltimo elemento -> 40
print("---Indexación en Arreglos 2D (Bidimensional / Matriz)-0200---")
n0120 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n0120)
print(n0120[0, 0])   # Fila 0, Columna 0 -> 10
print(n0120[1, 2])   # Fila 1, Columna 2 -> 60
print(n0120[-1, -1]) # Última fila, Última columna -> 60
print(n0120[-2, -2]) # Penúltima fila, Penúltima columna -> 20
print("---Indexación en Arreglos 3D (Tridimensional)-0200---")
# Arreglo 3D de forma 2x(2x3)
n0120 = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(n0120)
print(n0120[0, 0, 0]) # Bloque 0, Fila 0, Columna 0 -> 10
print("Alejandra Rivera Valenzuela NC 0200")
