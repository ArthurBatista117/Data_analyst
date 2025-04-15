import pandas as pd

age = [
    12, 32, 33, 43, 19, 23,
    22, 18, 34, 37, 28, 25
]

indexs = [
        'Arthur', 'Batista', 'Byanka', 'Myckelly', 'Guilherme', 'Henrique',
        'Evandro', 'Flavia', 'Alex',    'Álvaro',   'Pedro',    'Fernando'
]

age_series = pd.Series(age)

age_names = pd.Series(indexs)

df = pd.DataFrame()
df['age'] = age_series
df['names'] = age_names
print(df)