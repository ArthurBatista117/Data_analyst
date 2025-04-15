import pandas as pd

def main():
    df1 = pd.DataFrame({
        'name': ['Arthur', 'Batista', 'Mah', 'Nah'],
        'age': [18, 17, 28, 19],
        'id': [1, 2, 3, 4],
    })
    df2 = pd.DataFrame({
        'id_cliente': [1, 2, 3, 4, 5, 4, 2],
        'value': [190, 123, 67, 125, 234, 333, 7776],
    })

    print(df1)
    print('='*30)
    print(df2)
    print('='*30)
    ids = df1.merge(df2, left_on=['id'], right_on='id_cliente', how='inner')
    print(ids)
    print('='*30)
    soma = ids.groupby(by='id').sum()
    print(soma)


if __name__ == '__main__':
    main()