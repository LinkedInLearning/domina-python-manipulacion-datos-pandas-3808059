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

