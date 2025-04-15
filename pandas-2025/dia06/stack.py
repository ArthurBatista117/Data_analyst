import pandas as pd

def main():
    df = pd.read_csv('homicidios_completo.csv')
    df = df.set_index(['nome', 'período'])
    df = df.stack()
    df = df.reset_index()
    df = df.rename(columns={'level_2': 'Metrica', 0: 'Valor'})
    print(df)


if __name__ == '__main__':
    main()