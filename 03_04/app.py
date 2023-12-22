import pandas as pd
import matplotlib.pyplot as plt

archivo = 'empleados.csv'
df_empleados = pd.read_csv(archivo, delimiter=";")

print("Dataframe original:")
print(df_empleados)

df_empleados['Edad'].hist(bins=5, edgecolor='black', grid=False)
plt.title('Distribución de edades')
plt.xlabel('Grupos de edad')
plt.ylabel('Frecuencia')
plt.show()