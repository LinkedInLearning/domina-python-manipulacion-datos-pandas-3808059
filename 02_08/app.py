import pandas as pd

archivo = 'inventario.xlsx'
df = pd.read_excel(archivo)
print(df)

num_filas, num_columnas = df.shape
print(f"Número de filas: {num_filas}. Número de columnas: {num_columnas}")

valores_faltantes_columnas = df.isna().sum()
print("Número de valores faltantes en cada columna:")
print(valores_faltantes_columnas)

valores_faltantes_filas = df.isna().sum(axis=1)
print("Número de valores faltantes en cada fila:")
print(valores_faltantes_filas)

df = df.dropna(axis=1, thresh=len(df) - 19)
valores_faltantes_columnas = df.isna().sum()
print("Número de valores faltantes en cada columna:")
print(valores_faltantes_columnas)

print("Eliminar filas con 8 o más registros faltantes")
df = df.dropna(thresh=df.shape[1] - 6)

valores_faltantes_filas = df.isna().sum(axis=1)
print("Número de valores faltantes en cada fila:")
print(valores_faltantes_filas)


