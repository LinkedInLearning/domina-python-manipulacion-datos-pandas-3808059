import pandas as pd

df_ventas_semestre = pd.DataFrame({
    'mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Marzo', 'Abril'],
    'ventas': [10000, 12000, 15000, 18000, 20000, 22000, 15000, 18000]
})
print(df_ventas_semestre)