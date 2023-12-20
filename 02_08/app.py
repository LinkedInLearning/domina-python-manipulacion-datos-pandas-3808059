import pandas as pd

archivo = 'inventario.xlsx'
df = pd.read_excel(archivo)
print(df)

num_filas, num_columnas = df.shape
print(f"Número de filas: {num_filas}. Número de columnas: {num_columnas}")