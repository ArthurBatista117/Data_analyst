import pandas as pd
from faker import Faker

def create_dataframe():
    dataframe = {'nome': [], 'idade': [], 'telefone': [], 'salário': []}
    fake = Faker('pt_BR')
    for _ in range(50):
        dataframe['nome'].append(fake.name())
        dataframe['idade'].append(fake.random_int(min=15, max=65))
        dataframe['telefone'].append(fake.phone_number())
        dataframe['salário'].append(fake.random_int(min=1500, max=100000))

    df = pd.DataFrame(dataframe)
    df['salário'] = df['salário'].astype(float)

    return df


def main():
    df = create_dataframe()
    print(df)


if __name__ == '__main__':
    main()