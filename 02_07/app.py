import pandas as pd

df_clientes = pd.DataFrame({
  "nombre" : ["Luis", "Ana", "Sebastián", "Sofía", "Mateo", "Camila", "Valentín", "Isabella"],
  "cuidad" : ["Buenos Aires", "Lima", "Ciudad de México", "Santiago", "Alajuela", "Nueva York", "Toronto", "Río de Janeiro"], 
  "profesion": ["Médico", "Ingeniera civil", "Abogado", "Profesora", "Contador", "Enfermera", "Estudiante", "Periodista"]
})

archivo = 'clientes.csv'

df_clientes.to_csv(archivo, index=False)
print("Archivo exportado")