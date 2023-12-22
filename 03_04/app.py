import pandas as pd
import matplotlib.pyplot as plt

archivo = 'empleados.csv'
df_empleados = pd.read_csv(archivo, delimiter=";")

print("Dataframe original:")
print(df_empleados)