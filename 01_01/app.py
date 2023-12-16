import pandas as pd

diccionario_empleados = {
    15379 : "hmaldonado@kinetecoinc.com",
    15419 : "czambrano@kinetecoinc.com",
    15420 : "edomínguez@kinetecoinc.com",
    46556 : "tbenítez@kinetecoinc.com",
    46555 : "sblanco@kinetecoinc.com",
    46559 : "egarcía@kinetecoinc.com",
    15428 : "rtorres@kinetecoinc.com",
    15429 : "rmolina@kinetecoinc.com",
    47130 : "nflores@kinetecoinc.com",
    32117 : "pbermúdez@kinetecoinc.com",
    32313 : "cortiz@kinetecoinc.com"
}

serie_empleados = pd.Series(diccionario_empleados)

print(serie_empleados)
print(type(serie_empleados))
