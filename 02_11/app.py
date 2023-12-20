import pandas as pd

df_ventas_semestre = pd.DataFrame({
    'productos': ['computadora', 'teléfono', 'computadora', 'teléfono', 'computadora', 'teléfono', 'computadora', 'teléfono' ],
    'mes': ['Enero', 'Enero', 'Febrero', 'Febrero', 'Marzo', 'Marzo', 'Abril', 'Abril'],
    'ventas': [10000, 12000, 15000, 18000, 20000, 22000, 15000, 18000]
})

print("Dataframe original:")
print(df_ventas_semestre)

df_reestructurado = df_ventas_semestre.pivot(index='mes', columns='productos', values='ventas')

print("Dataframe reestructurado:")
print(df_reestructurado)