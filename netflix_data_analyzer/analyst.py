import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

def convert_cel(x):
    return x.split(', ')


def main():
    df = pd.read_csv('data/netflix_titles.csv')

    # What types of content are most common (Movie vs TV Show)?
    most_common = df.groupby(by='type')['title'].count()
    plt.style.use('bmh')

    #graphs
    plt.title('What types of content are most common (Movie vs TV Show)?')
    plt.bar(most_common.index, most_common.values, color=['#5CDCE0', '#855CE0'], width=0.25)
    plt.ylabel('Number of Titles')
    plt.xlabel('Type')
    plt.show()
    print(most_common.head())

    # How many titles were added each year?
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    df['year_added'] = df['date_added'].dt.year

    title_year = df.groupby('year_added')['title'].count()

    # graphs
    plt.title('How many titles were added each year?')
    plt.bar(title_year.index, title_year.values, color='#5262D9', width=0.25)
    plt.xlabel('Years')
    plt.ylabel('Movies')
    plt.show()
    mean_title = title_year.mean()
    print(f'Will add one mean of {mean_title:.2f} titles for year')

    # Who are the most frequent directors or actors?
    directors = df.groupby(by='director')['title'].count().head(5)
    print(directors.sort_values(ascending=False))

    #graphs
    plt.title('Who are the most frequent directors or actors?')
    plt.bar(directors.index, directors.values, width=0.25, color='#DB1B1B')
    plt.ylabel('Titles')
    plt.xlabel('Directors')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    cast = df['cast'].dropna()
    actors_cast = []
    actors_cast.extend(cast.apply(convert_cel))
    actors = []
    for _ in actors_cast:
        actors.extend(_)
    actor_counts = Counter(actors)

    actors_series = pd.Series(actor_counts).sort_values(ascending=False).head()
    print(actors_series)

    #graphs
    plt.title('Who are the most frequent directors or actors?')
    plt.bar(actors_series.index, actors_series.values, width=0.25, color='#6DDB30')
    plt.ylabel('Movies')
    plt.xlabel('Actors')
    plt.xticks(rotation=45, ha='right')
    plt.show()

    # Which country produces the most content on Netflix?
    top_country = df['country'].dropna().str.split(', ').explode()
    top_country_counts = top_country.value_counts().head()
    print(top_country_counts.sort_values(ascending=False))

    #graphs
    plt.title('Which country produces the most content on Netflix?')
    plt.bar(top_country_counts.index, top_country_counts.values, width=0.25, color='#DBCE30')
    plt.ylabel('Titles')
    plt.xlabel('Country')
    plt.xticks(rotation=45, ha='right')
    plt.show()




if __name__ == '__main__':
    main()