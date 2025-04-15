import pandas as pd
import matplotlib.pyplot as plt

# Global DataFrame
df = pd.read_csv('../data/Export.csv')

def compare_country(c1, c2, item):
    countries = df['Area'].unique()
    items = df['Item'].unique()

    if c1 not in countries or c2 not in countries:
        raise ValueError('Invalid Country')
    elif item not in items:
        raise ValueError('Invalid Item')

    subset = df[(df['Item'] == item) & (df['Area'].isin([c1, c2]))]

    pivot = subset.pivot_table(index='Year', columns='Area', values=['Production', 'Consumption'])

    pivot['Production'].plot(title=f'Produção de {item} - {c1} x {c2}', figsize=(10, 6))
    plt.ylabel('Produção')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    pivot['Consumption'].plot(title=f'Consumo de {item} - {c1} x {c2}', figsize=(10, 6))
    plt.ylabel('Consumo')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    df_2020 = df[df['Year'] == 2020]

    top10 = df_2020.groupby('Item')['Production'].sum().sort_values(ascending=False).head(10)
    top10.plot(kind='bar', figsize=(10, 6), title='Top 10 Produtos mais Produzidos em 2020')
    plt.ylabel('Produção total')
    plt.xlabel('Produto')
    plt.grid()
    plt.tight_layout()
    plt.show()

    top5_consumption = df_2020.groupby('Area')['Consumption'].sum().sort_values(ascending=False).head(5)
    print("Top 5 países com maior consumo em 2020:")
    print(top5_consumption)

    df['Efficiency'] = df['Production'] / (df['Consumption'] + 1)

    print("Itens disponíveis:\n", df['Item'].unique())
    compare_country('India', 'Indonesia', 'Vanilla, raw')

if __name__ == '__main__':
    main()
