import pandas as pd

t = pd.read_csv('../data/archive/transacoes.csv')

t['dtCriacao'] = pd.to_datetime(t['dtCriacao'], errors='coerce')
t['datas'] = t['dtCriacao'].dt.date
t = t.sort_values(['idCliente', 'dtCriacao'])

first_day = t.drop_duplicates(keep='first', subset=['idCliente', 'datas'])
print(first_day)
