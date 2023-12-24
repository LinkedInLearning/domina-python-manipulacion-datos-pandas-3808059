import pandas as pd

ventas = {
    'ventas': [10000, 12000, 15000, 18000, 20000, 22000, 15000, 18000],
    'cantidad': [10, 40, 20, 10, 6, 10, 9, 8]
}

indice = pd.MultiIndex.from_tuples([
     ('Electrónicos', 'Laptop', 'En línea'),
     ('Electrónicos', 'Tableta', 'En tienda'),
     ('Electrónicos', 'Teléfonos', 'En línea'),
     ('Ropa', 'Camiseta', 'En tienda'),
     ('Ropa', 'Medias', 'En línea'),
     ('Ropa', 'Vestido', 'En línea'),
     ('Hogar', 'Alfombras', 'En tienda'),
     ('Hogar', 'Cortinas', 'En tienda'),
], names=['Categoria', 'Producto', 'Canal_Ventas'])

df_tienda = pd.DataFrame(ventas, index=indice)
print(df_tienda)