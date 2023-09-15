FROM python
ARG key_id
ARG secret

ENV AWS_ACCESS_KEY_ID=$key_id
ENV AWS_SECRET_ACCESS_KEY=$secret

RUN pip install --no-cache-dir boto3

COPY movies.csv .
COPY series.csv .
COPY etl.py .

RUN python etl.py
