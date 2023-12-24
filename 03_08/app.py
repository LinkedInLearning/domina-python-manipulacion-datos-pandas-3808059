import pandas as pd

df_ventas = pd.DataFrame({
    "producto": ["Computadora", "Camiseta", "Alfombras", "Tableta", "Vestido", "Computadora"],
    "categoria": ["Electrónicos", "Ropa", "Hogar", "Electrónicos", "Ropa", "Electrónicos"],
    "ventas": [10000, 12000, 15000, 18000, 2000, 3000],
})

df_tabla_dinamica = df_ventas.pivot_table(
    values="ventas", index="categoria", columns="producto", aggfunc="sum"
)

print(df_tabla_dinamica)
