import pandas as pd
import os

from anaconda_navigator.utils.url_utils import file_name


def read_file( file_name:str ):
    df = (
        pd.read_csv(f'../data/ipea/{file_name}.csv', sep=';')
                .rename(columns={'valor': file_name})
                .set_index(['nome', 'período'])
                .drop(['cod'], axis=1)
        )
    return df

def main():
    names = os.listdir('../data/ipea/')
    dfs = []
    for i in names:
        file_name = i.split('.')[0]
        dfs.append(read_file(file_name))
    dfs = pd.concat(dfs, axis=1).reset_index().sort_values(['período', 'nome'])
    dfs.to_csv('homicidios_completo.csv')
    print(dfs)


if __name__ == '__main__':
    main()