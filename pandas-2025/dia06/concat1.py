import pandas as pd
from faker import Faker

def main():
    fake = Faker()
    df1 = pd.DataFrame( {'name': [fake.name() for _ in range(5)]})
    df2 = pd.DataFrame({'idade': [fake.random_int(min=10, max=90) for _ in range(3)]})
    df_full = pd.concat([df1, df2], axis=1)
    print(df_full)


if __name__ == '__main__':
    main()
