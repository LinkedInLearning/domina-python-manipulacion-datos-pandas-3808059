import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_estudiantes = pd.read_csv('estudiantes.csv')
print(df_estudiantes)

matriz_correlacion = df_estudiantes.corr()

correlacion_promedio = matriz_correlacion['promedio']
print("Correlación con el promedio obtenido en el curso")
print(correlacion_promedio)

sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlación')
plt.show()