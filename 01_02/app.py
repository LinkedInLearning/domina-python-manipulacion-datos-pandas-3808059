import pandas as pd

lista_email = ["hmaldonado@kinetecoinc.com","czambrano@kinetecoinc.com","edomínguez@kinetecoinc.com","tbenítez@kinetecoinc.com"]
etiquetas_id = [15379, 15419, 15420, 46556]
serie_email = pd.Series(lista_email, index =etiquetas_id)

print(serie_email)

#print(serie_email[1])
print(serie_email[15379])