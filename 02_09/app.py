import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

archivo = 'empleados.csv'
df = pd.read_csv(archivo, delimiter=";")

num_filas, num_columnas = df.shape
print(f"Número de filas: {num_filas}. Número de columnas: {num_columnas}")

valores_faltantes_columnas = df.isna().sum()
print("Número de valores faltantes en cada columna:")
print(valores_faltantes_columnas)

media_edad = df['Edad'].mean(skipna=True)
print(f"La media de edad es: {media_edad}")

print("Reemplazar valores faltantes por la media")
df['Edad'] = df['Edad'].fillna(media_edad)
print(df)
