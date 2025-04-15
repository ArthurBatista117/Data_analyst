import pandas as pd

df = pd.read_csv('../data/archive/clientes.csv')

df = df.dropna()

print(df)