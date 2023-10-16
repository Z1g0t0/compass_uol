import sys
import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.sql import functions as f

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

raw = spark.read.json(f"s3://data-lake-do-eduardo/Raw/TMDB/JSON/Movies/{year}/{month}/{day}/tmdb.json")
#raw.printSchema()

trusted = raw.select(f.col("title").alias("Titulo"), f.col("original_title").alias("Original"),
                     f.col("release_date").alias("Data_Lancamento"), f.col("vote_count").alias("Quantidade_Votos"), 
                     f.col("vote_average").alias("Media_Votos"), f.col("popularity").alias("Score_TMDB"), 
                     f.col("genre_ids").alias("Generos"), f.col("overview").alias("Sinopse"))

# Generos como array
#trusted = trusted.withColumn("Generos", f.regexp_replace(f.regexp_replace("Generos","\\[", ""), "\\]", ""))
#trusted = trusted.withColumn("Generos", f.split(f.col("Generos"), ","))

# Filtra por codigo dos generos acao/aventura (12/28)
gen_ids = [12, 28]
trusted = trusted.filter(f.arrays_overlap(f.col("Generos"), f.array([f.lit(i) for i in gen_ids])))

#Limpeza
trusted = trusted.na.drop(subset=["Data_Lancamento"])
trusted = trusted.withColumn("Data_Lancamento", f.to_date("Data_Lancamento"))
trusted = trusted.filter(f.col("Data_Lancamento") < f.lit(f"{year}-{month}-{day}"))
trusted = trusted.filter(f.col("Quantidade_Votos") > 10 )
trusted = trusted.withColumn("Sinopse", f.when(f.col("Sinopse") == "", "Não encontrado").otherwise(f.col("Sinopse")))

#Limitar o tamanho da coluna Resumo/Sinopse
#maxLen = 555
#trusted = trusted.withColumn("Sinopse", f.substring(f.col("Sinopse"), 0, maxLen))

trusted.write.parquet(f"s3://data-lake-do-eduardo/Trusted/{year}/{month}/{day}/", mode='overwrite')

job.commit()
