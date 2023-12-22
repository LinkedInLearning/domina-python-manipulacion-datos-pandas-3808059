import pandas as pd

archivo = 'empleados.csv'
df_empleados = pd.read_csv(archivo, delimiter=";")

print("Dataframe original:")
print(df_empleados)

total_elementos = df_empleados.size
print("Número total de elementos:", total_elementos)

dimensiones = df_empleados.shape
print("Filas:", dimensiones[0])
print("Columnas:", dimensiones[1])

num_dimensiones = df_empleados.ndim
print("Número de dimensiones:", num_dimensiones)

print("Eliminar columnas para reducir la dimensionalidad")
df_empleados = df_empleados.drop(['Estado_Civil', 'Edad'], axis=1)
print(df_empleados)

print("Eliminar filas para reducir la dimensionalidad")
df_empleados = df_empleados[df_empleados['Salario'] < 2000]
print(df_empleados)

dimensiones = df_empleados.shape
print("Filas:", dimensiones[0])
print("Columnas:", dimensiones[1])