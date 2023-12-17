from numpy import NaN
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

print("Eliminar registros")
eliminar_registros = serie_empleados.dropna()
print(eliminar_registros)

print("Reemplazar valores faltantes por 'Desconocido'")
reemplazar_registros = serie_empleados.fillna('desconocido')
print(reemplazar_registros)

diccionario_temperaturas = {
    2010: 73,
    2011: NaN,
    2012: 75.3,
    2013: 72.4,
    2014: 72.5,
    2015: 74.4,
    2016: NaN,
    2017: NaN,
    2018: 73.5,
    2019: 72.7,
    2020: NaN,
    2021: 73.5,
}
serie_temperaturas= pd.Series(diccionario_temperaturas)

print("Reemplazar valores faltantes por la media")
reemplazar_temperaturas = serie_temperaturas.fillna(serie_temperaturas.mean())
print(reemplazar_temperaturas)
