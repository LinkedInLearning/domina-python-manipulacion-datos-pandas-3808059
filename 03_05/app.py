import pandas as pd
import matplotlib.pyplot as plt

df_ventas = pd.DataFrame({
    'fecha': pd.to_datetime(['2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01', '2023-07-01']),
    'ventas': [1004,1500,1250,1235,13445]
})