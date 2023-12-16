import pandas as pd

diccionario_empleados = {
    15379 : "Hernan Maldonado",
    15419 : "Carlos Zambrano",
    15420 : "Elena Domínguez",
    46556 : "Teresa Benítez",
    46555 : "Sonia Blanco",
    46559 : "Ernesto García",
    15428 : "Rodrigo Torres",
    15429 : "Roberto Molina",
    47130 : "Nuria Flores",
    32117 : "Patricia Bermúdez",
    32313 : "Clara Ortiz"
}

serie_empleados = pd.Series(diccionario_empleados)

print("Serie:")
print(serie_empleados)