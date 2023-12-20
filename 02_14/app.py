import pandas as pd

df_ventas_anuales = pd.DataFrame(
    {
        "mes": [
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre",
        ],
        "ventas": [
            50000,
            55000,
            60000,
            75000,
            100000,
            200000,
            80000,
            60000,
            55000,
            70000,
            95000,
            1550000,
        ],
    }
)
print("Dataframe original:")
print(df_ventas_anuales)

Q1 = df_ventas_anuales["ventas"].quantile(0.25)
Q3 = df_ventas_anuales["ventas"].quantile(0.75)
IQR = Q3 - Q1

umbral = 1.5
limite_inferior = Q1 - umbral * IQR
limite_superior = Q3 + umbral * IQR
df_valores_atipicos = df_ventas_anuales[
    (df_ventas_anuales["ventas"] < limite_inferior)
    | (df_ventas_anuales["ventas"] > limite_superior)
]

print("Valores atípicos:")
print(df_valores_atipicos)
