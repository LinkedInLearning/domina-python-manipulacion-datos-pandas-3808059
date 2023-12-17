import pandas as pd

df_caja1 = pd.DataFrame({
    'fecha': ['2023-02-01', '2023-02-02', '2023-02-03', '2023-02-04', '2023-02-05'],
    'venta_caja1': [1004,1500,1250,1235,13445]
})

df_caja2 = pd.DataFrame({
    'fecha': ['2023-02-01', '2023-02-02', '2023-02-03', '2023-02-04', '2023-02-05', '2023-02-06'],
    'venta_caja2': [990,1240,1600,1258,1364,1239]
})

df_ventas_totales = pd.merge(df_caja1, df_caja2, on='fecha', how='outer')
df_ventas_totales['Total'] = df_ventas_totales[['venta_caja1', 'venta_caja2']].sum(axis=1)

print(df_ventas_totales)
