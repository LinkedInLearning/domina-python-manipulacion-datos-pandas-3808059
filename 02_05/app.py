import pandas as pd

archivo = 'datos.json'
df = pd.read_json(archivo)
print(df)
