import pandas as pd

df_datos_personal = pd.DataFrame({
    "id": [15379, 15419, 15420, 46556, 46555],
    "nombre": ["Hernan", "Carlos", "Elena", "Teresa", "Sonia"],
    "apellido": ["Maldonado", "Zambrano", "Domínguez", "Benítez", "Blanco"],
    "edad": [35, 30, 32, 41, 29],
    "email": ["hmaldonado@kinetecoinc.com","czambrano@kinetecoinc.com","edominguez@kinetecoinc.com","tbenitez@kinetecoinc.com","sblanco@kinetecoinc.com"],
})

df_datos_puesto = pd.DataFrame({
    "id": [15379, 15419, 46555, 46556],
    "puestos": ["Ingeniero I", "Vicetresidente RRHH", "Manufacturación y distribución","Geólogo IV"],
    "lugar": ["Texas", "California", "California", "Maryland"]
})

union_dataframes = pd.merge(df_datos_personal, df_datos_puesto, on='id', how='left')
print("Colaboradores sin un puesto asociado:")
print(union_dataframes)