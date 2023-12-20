import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

archivo = 'empleados.csv'
df = pd.read_csv(archivo, delimiter=";")

num_filas, num_columnas = df.shape
print(f"Número de filas: {num_filas}. Número de columnas: {num_columnas}")