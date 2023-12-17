import pandas as pd
serie_empleados = pd.Series({
    15379 : "hmaldonado@kinetecoinc.com",
    15419 : None,
    15420 : "edomínguez@kinetecoinc.com",
    46556 : "tbenítez@kinetecoinc.com",
    46555 : "sblanco@kinetecoinc.com",
    46559 : None,
    15428 : "rtorres@kinetecoinc.com",
    15429 : "rmolina@kinetecoinc.com",
    47130 : None,
    32117 : None,
    32313 : "cortiz@kinetecoinc.com"
})

print(serie_empleados)

print("Identificar valores faltantes")
print(serie_empleados.isna())

print("Total de valores faltantes")
print(serie_empleados.isna().sum())