import boto3
import datetime
import os
import io
import json
import requests
import pandas as pd

#from IPython.display import display
from botocore.exceptions import ClientError

def save_s3(df):
    
    current_time = datetime.datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day
    
    json_buffer = io.StringIO()
    df.to_json(json_buffer, orient='records')
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('data-lake-do-eduardo')
    
    destination = f'Raw/TMDB/JSON/Movies/{year}/{month}/{day}/tmdb.json'

    return bucket.put_object(Key=destination, Body=json_buffer.getvalue())
    
def lambda_handler(event, context):
    
    # TODO implement
    api_key = "bddd4e410aadb3c90b27d93b5a057e13"
    pages = 500

    res = pd.DataFrame()

    for i in range(1, pages):
    
        #breakpoint()
    
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&include_adult=true&include_video=true&language=pt-BR&page={i}&sort_by=popularity.desc"
    
        response = requests.get(url)
        data = response.json()
    
        filmes = []
    
        for movie in data['results']:
            try:
                df = {
                    'Titulo': movie['title'],
                    #'Data de lançamento': movie['release_date'],
                    'Sinopse': movie['overview'],
                    'Qtd_votos': movie['vote_count'],
                    'Media': movie['vote_average']
                }
            except KeyError:
                continue
            
            filmes.append(df)
    
        res = pd.concat([res, pd.DataFrame(filmes)], ignore_index=True)
        res.set_index('Titulo')
    
    res.drop_duplicates()
    if save_s3(res):
    
        return {
            'statusCode': 200,
            'body': json.dumps('Dados ingeridos com sucesso')
        }
        
    else:
        return {
            'body': json.dumps('Erro')
        }
    
