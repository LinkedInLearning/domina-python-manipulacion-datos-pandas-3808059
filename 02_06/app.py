import pandas as pd

archivo = 'datos.xlsx'
df = pd.read_excel(archivo, sheet_name='datos')
print(df)
