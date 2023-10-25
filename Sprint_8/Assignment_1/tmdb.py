import requests
import pandas as pd

from IPython.display import display

api_key = "bddd4e410aadb3c90b27d93b5a057e13"

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()

filmes = []

for movie in data['results']:
    df = {
        'Titulo': movie['title'],
        'Data_Lancamento': movie['release_date'],
        'Sinopse': movie['overview'],
        'Quantidade_Votos': movie['vote_count'],
        'Media': movie['vote_average']}

    filmes.append(df)

df = pd.DataFrame(filmes)
display(df)

#df.to_csv('out.csv')