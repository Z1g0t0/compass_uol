import boto3
import datetime
import os

if __name__ == '__main__':

    current_time = datetime.datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day

    key_id = os.getenv('AWS_ACCESS_KEY_ID')
    secret = os.getenv('AWS_SECRET_ACCESS_KEY')

    s3_client = boto3.client('s3',
                             aws_access_key_id=key_id,
                             aws_secret_access_key=secret)

    response_1 = s3_client.upload_file(r'./movies.csv', 'data-lake-do-eduardo', f'Raw\Local\CSV\Movies\{year}\{month}\{day}\movies.csv')
    response_2 = s3_client.upload_file(r'./series.csv', 'data-lake-do-eduardo', f'Raw\Local\CSV\series\{year}\{month}\{day}\series.csv')

    print(f'RESPOSTA 1: {response_1} \n')
    print(f'RESPOSTA 2: {response_2} \n')