import pandas as pd

def main():
    exp = pd.read_csv('../data/Export.csv')

    print(exp.sample(n=7))
    print('='*30)

    only_countries = exp['Area'].unique()
    print(only_countries)

    tot_production = exp['Production'].sum()
    print('='*30)
    print(tot_production)

    print('=' * 30)
    filtro1 = ((exp['Item'].str.contains('raw')) | (exp['Item'].str.contains('Raw'))
               & (exp['Year'] == 2020))
    print(exp[filtro1].sort_values(by=['Item', 'Year']))

    print('='*30)
    exp['Balance'] = exp['Production'] - exp['Consumption']
    print(exp[['Production', 'Consumption', 'Balance']].sample(n=8))

    print('='*30)
    exp_ordered = exp.sort_values(by='Year')
    print(exp_ordered)
    top5_most_products = exp.groupby(by='Item').sum()
    print(top5_most_products[0:5])


if __name__ == '__main__':
    main()