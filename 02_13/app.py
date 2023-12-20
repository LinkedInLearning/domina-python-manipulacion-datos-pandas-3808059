import pandas as pd

archivo = 'empleados.csv'
df_empleados = pd.read_csv(archivo, delimiter=";")

print("Dataframe original:")
print(df_empleados)

df_empleados = df_empleados[df_empleados['Experiencia'] >= 5]
print("Dataframe con empleados de 5 o más años de experiencia:")
print(df_empleados)