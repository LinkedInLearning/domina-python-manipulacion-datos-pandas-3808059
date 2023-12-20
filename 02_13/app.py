import pandas as pd

archivo = 'empleados.csv'
df_empleados = pd.read_csv(archivo, delimiter=";")

print("Dataframe original:")
print(df_empleados)