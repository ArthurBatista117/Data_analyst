import pandas as pd

df = pd.read_csv('../data/archive/clientes.csv')

filtro =  df['dtCriacao'].isna()
filtro2 = df['dtCriacao'].notna()

print(filtro)

print(filtro2)