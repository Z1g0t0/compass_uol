import boto3
import datetime
import os
import json
import requests
import pandas as pd

#from IPython.display import display
from botocore.exceptions import ClientError
    
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
def save_s3(df):
    
    current_time = datetime.datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day

    #key_id = os.getenv('AWS_ACCESS_KEY_ID')
    #secret = os.getenv('AWS_SECRET_ACCESS_KEY')
    
    #s3_client = boto3.client('s3',
    #                         aws_access_key_id=key_id,
    #                         aws_secret_access_key=secret)
    
    #response_1 = s3_client.upload_file(r'./movies.csv', 'data-lake-do-eduardo', f'Raw\Local\CSV\Movies\{year}\{month}\{day}\movies.csv')
    #response_2 = s3_client.upload_file(r'./series.csv', 'data-lake-do-eduardo', f'Raw\Local\CSV\series\{year}\{month}\{day}\series.csv')

    #print(f'RESPOSTA 1: {response_1} \n')
    #print(f'RESPOSTA 2: {response_2} \n')
    
    try:                
        res.to_json(f's3://data-lake-do-eduardo/Raw/TMDB/JSON/Movies/{year}/{month}/{day}/out.json')
        return True
        
    except:
        return False

if __name__ == "__main__":
    
    api_key = "bddd4e410aadb3c90b27d93b5a057e13"

    pages = 5

    res = pd.DataFrame()

    for i in range(1, pages+1):
    
        #breakpoint()
    
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&include_adult=true&include_video=true&language=pt-BR&page={i}&sort_by=popularity.desc"
    
        response = requests.get(url)
        data = response.json()
    
        filmes = []
    
        for movie in data['results']:
            df = {'Titulo': movie['title'],
            'Data de lançamento': movie['release_date'],
            'Visão geral': movie['overview'],
            'Votos': movie['vote_count'],
            'Média de votos:': movie['vote_average']}
    
            filmes.append(df)
    
        res = pd.concat([res, pd.DataFrame(filmes)], ignore_index=True)
    
    print(save_s3(res))
    #res.to_json('out.json', orient='split')
    #res.to_csv('out.csv')