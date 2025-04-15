import pandas as pd
from faker import Faker

def create_data():
    fake = Faker()
    name = []
    age = []
    city = []
    salary = []
    for _ in range(5):
        name.append(fake.name())
        age.append(fake.random_int(min=8, max=90))
        city.append(fake.city())
        salary.append(fake.random_int(min=1200, max=100000))

    data = {'Name': name, 'Age': age, 'City': city, 'Salary': salary}

    return data


def main():
    df = pd.DataFrame(create_data())
    print(df)
    print('='*30)
    print(df[df['Age'] > 25])
    print('=' * 30)
    print(df.sort_values('Age', ascending=False))
    print('=' * 30)
    df['Salary'] = df['Salary'] * 1.10
    print(df)


if __name__ == '__main__':
    main()