import numpy as np
# Alejandra Rivera Valenzuela NC 0200
# Creación de un arreglo unidimensional de valores
data = np.array([12, 55, 34, 89, 45, 67, 23, 90, 11, 78, 50, 62, 30, 88, 41])
print("--- Arreglo Original ---")
print(data)
# Máscara booleana y filtrado simple (valores > 50)
mask = data > 50
print("\nMáscara booleana (data > 50):")
print(mask)
filtered_data = data[mask]
print("\nValores mayores a 50:")
print(filtered_data)
# Filtrado compuesto con operadores bit a bit (& = Y, | = O)
complex_filter = data[(data > 30) & (data < 80)]
print("\nValores mayores a 30 Y menores a 80:")
print(complex_filter)
# Obtener los índices numéricos donde se cumple la condición
indices = np.where(data > 50)
print("\n--- Índices donde los valores son > 50 ---")
print(indices[0])
# Reemplazo condicional: np.where(condición, valor_si_cierto, valor_si_falso)
# Asigna 1 si es mayor a 50, o 0 en caso contrario
binary_array = np.where(data > 50, 1, 0)
print("\nArreglo binario (1 si >50, 0 de lo contrario):")
print(binary_array)
# Reemplazar directamente los valores originales que cumplan la condición
data_modified = np.where(data > 50, 999, data)
print("\nArreglo reemplazando valores >50 por 999:")
print(data_modified)
# Matriz 2D que incluye valores nulos (Not a Number)
matrix_with_nan = np.array([
    [10.0, np.nan, 30.0],
    [40.0, 50.0, np.nan],
    [70.0, 80.0, 90.0]
])
print("\n--- Matriz con datos faltantes (NaN) ---")
print(matrix_with_nan)
# Detección de NaNs mediante máscara
nan_mask = np.isnan(matrix_with_nan)
print("\nMáscara booleana de valores NaN:")
print(nan_mask)
# Cálculo de estadísticas ignorando NaNs (np.nanmean)
mean_value = np.nanmean(matrix_with_nan)
print(f"\nPromedio de la matriz (ignorando NaNs): {mean_value:.2f}")
# Imputación / Limpieza: reemplazar NaNs con la media del arreglo
cleaned_matrix = np.nan_to_num(matrix_with_nan, nan=mean_value)
print("\nMatriz limpia (NaNs reemplazados por el promedio):")
print(cleaned_matrix)
print("Alejandra Rivera Valenzuela NC 0200")
