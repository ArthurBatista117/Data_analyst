import pandas as pd

client = pd.read_csv('../data/archive/clientes.csv')

client['pontos100'] = client['qtdePontos'] + 100

print(client)

print(client.sort_values(by='pontos100', ascending=False).head())
