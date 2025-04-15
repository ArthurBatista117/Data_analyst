import pandas as pd

def get_last_id(el):
    last = el.split('-')
    return last[-1]

def main():
    clientes = pd.read_csv('../data/archive/clientes.csv')
    last = []

    for id in clientes['idCliente']:
        last.append(get_last_id(id))

    clientes['novoID'] = last
    print(clientes)


if __name__ == '__main__':
    main()