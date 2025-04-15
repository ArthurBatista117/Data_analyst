import pandas as pd

def main():
    transacao = pd.read_csv('../data/archive/transacoes.csv')
    transacao_produto = pd.read_csv('../data/archive/transacao_produto.csv')
    produto = pd.read_csv('../data/archive/produtos.csv')

    ids = transacao_produto.merge(produto, on='idProduto', how='left')

    id12 = (ids['idProduto'] == 12)
    steaks = ids[id12]

    clientes_steak = transacao.merge(steaks, on='idTransacao', how='inner')

    much_steak_inordered = clientes_steak.groupby(by='idCliente')['qtdeProduto'].count()
    much_steak = much_steak_inordered.sort_values(ascending=False)

    print(much_steak.head())

    produto = produto[produto['idProduto'] == 12]
    top5 = (
        transacao.merge(transacao_produto, on='idTransacao', how='left')
                         .merge(produto, on='idProduto', how='inner')
                         .groupby(by='idCliente')['qtdeProduto'].count()
                         .sort_values(ascending=False)
            )
    print(top5.head())


if __name__ == '__main__':
    main()