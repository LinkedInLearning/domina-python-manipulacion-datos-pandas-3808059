import pandas as pd

diccionario_empleados = {
    15379 : "Hernan Maldonado",
    15419 : "Carlos Zambrano",
    15420 : "Elena Domínguez",
    46556 : "Teresa Benítez",
    46555 : "Sonia Blaco",
}

serie_empleados = pd.Series(diccionario_empleados)

print("Serie:")
print(serie_empleados)