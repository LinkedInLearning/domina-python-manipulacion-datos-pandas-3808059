import pandas as pd

salariosAnuales = [50230.0, 55123.0, 60089.0, 75020.0, 100987.0, 202345.0, 89000.0, 61200.0, 55300.0, 73400.0, 9520.0, 870000.0]
serie_salarios = pd.Series(salariosAnuales)
print(serie_salarios)

print("Total salarios:")
total_salarios = serie_salarios.sum()
print(total_salarios)

print("Promedio de salarios:")
promedio_salarios = serie_salarios.mean()
print(promedio_salarios)

print("Salario Máximo:")
maximo_salarios = serie_salarios.max()
print(maximo_salarios)

print("Salario Mínimo:")
minimo_salarios = serie_salarios.min()
print(minimo_salarios)

print("Mediana Salario:")
mediana_salarios = serie_salarios.median()
print(mediana_salarios)