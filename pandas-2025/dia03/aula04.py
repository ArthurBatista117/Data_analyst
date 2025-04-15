import pandas as pd

df = pd.read_csv('../data/archive/clientes.csv')

replace = {'0000-00-00 00:00:00.000': '2000-03-10 07:00:00.000'}

df['dtCriacao'] = pd.to_datetime(df['dtCriacao'].replace(replace))
print(df['dtCriacao'].dt.year)
print(df['dtCriacao'].dt.month)
print(df['dtCriacao'].dt.day)

