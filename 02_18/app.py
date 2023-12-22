import pandas as pd

df_empleados = pd.DataFrame({
  "nombre" : ["Hernan", "Carlos", "Elena", "Teresa"],
  "apellido": ["Maldonado", "Zambrano", "Domínguez", "Benítez"],
  "edad" : [35, 30, 32, 41],
  "email": ["hmaldonado@kinetecoinc.com","czambrano@kinetecoinc.com","edominguez@kinetecoinc.com","tbenitez@test.com"]
})

print("Dataframe original:")
print(df_empleados)