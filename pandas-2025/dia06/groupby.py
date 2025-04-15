import pandas as pd

transacoes = pd.read_csv('../data/archive/transacoes.csv')

cliente_tot_transacoes = transacoes.groupby(by='idCliente')['idTransacao'].count()
clienteVips = cliente_tot_transacoes > 100
print(cliente_tot_transacoes[clienteVips])
