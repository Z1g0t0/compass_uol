import sys
import datetime
from pyspark.sql.functions import col,when

from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

current_time = datetime.datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day

df = spark.read.parquet(f"s3://data-lake-do-eduardo/Trusted/{year}/{month}/{day}/*.parquet", index=False)
df = df.withColumn("Sinopse", when(col("Sinopse") == "", "Não encontrado").otherwise(col("Sinopse"))) 

df.write.parquet(f"s3://data-lake-do-eduardo/Refined/{year}/{month}/{day}/", mode='overwrite')

job.commit()
