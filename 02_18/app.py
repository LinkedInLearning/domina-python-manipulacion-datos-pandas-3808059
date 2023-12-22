import pandas as pd

df_empleados = pd.DataFrame({
  "nombre" : ["Hernan", "Carlos", "Elena", "Teresa"],
  "apellido": ["Maldonado", "Zambrano", "Domínguez", "Benítez"],
  "edad" : [35, 30, 32, 41],
  "email": ["hmaldonado@kinetecoinc.com","czambrano@kinetecoinc.com","edominguez@kinetecoinc.com","tbenitez@test.com"]
})

print("Dataframe original:")
print(df_empleados)

print("Nombres en mayúscula:")
df_empleados['nombre'] = df_empleados['nombre'].str.upper()
print(df_empleados['nombre'])

print("Correos electrónicos que tienen la palabra ez")
print(df_empleados[df_empleados['email'].str.contains('ez', case=False)])

print("Todos los correos electrónicos finalizan con kinetecoinc.com")
print(df_empleados[~df_empleados['email'].str.endswith('kinetecoinc.com')])