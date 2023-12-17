import pandas as pd
import matplotlib.pyplot as plt

diccionario_temperaturas = {
    2010: 73,
    2011: 73.2,
    2012: 75.3,
    2013: 72.4,
    2014: 72.5,
    2015: 74.4,
    2016: 74.9,
    2017: 74.6,
    2018: 73.5,
    2019: 72.7,
    2020: 74.6,
    2021: 73.5,
}

serie_temperaturas= pd.Series(diccionario_temperaturas)

serie_temperaturas.plot(
    title='Temperaturas del 2010 al 2021',
    marker='o',
    color='green',
    xlabel='Años',
    ylabel='Temperaturas'
)

plt.show()
