import random

from pyspark.sql import SparkSession, \
                        functions as f, \
                        types as t
from pyspark import SparkContext, SQLContext

def escolaridade():

    grad = [ "Fundamental", "Medio", "Superior" ]
    num = random.randrange(0, 3)
    
    return grad[num]

def pais():

    paises = [  "Chile", "Argentina", "Uruguai", 
                "Paraguai", "Brasil", "Bolivia", 
                "Peru", "Equador", "Colombia", 
                "Venezuela", "Guiana", "Guiana Francesa",
                "Suriname" ]

    num = random.randrange(0, 13)
    
    return paises[num]

def nascimento():
    
    return random.randrange(1945, 2010)

if __name__ == "__main__":

    spark = SparkSession.builder.master("local[*]") \
            .appName("Exercicio Intro").getOrCreate()

    df_nomes = spark.read.csv("nomes_aleatorios.txt")
    df_nomes = df_nomes.withColumnRenamed("_c0", "Nome")
    df_nomes.printSchema() 
    
    school = f.udf(escolaridade, t.StringType())
    df_nomes = df_nomes.withColumn("Escolaridade", school())

    df_nomes.printSchema() 
    df_nomes.show(11)

    country = f.udf(pais, t.StringType())
    df_nomes = df_nomes.withColumn("Pais", country() )

    birth = f.udf(nascimento, t.IntegerType())
    df_nomes = df_nomes.withColumn("AnoNascimento", birth())

    df_nomes.write.mode("overwrite")    \
            .option("header", True)     \
            .csv('test.csv')
    df_nomes = spark.read.csv("test.csv", header=True)
    #df.printSchema()
    #df.show()

    df_nomes.select("Nome", "AnoNascimento") \
            .where(f.col("AnoNascimento") > 2000)\
            .show()

    df_nomes.createOrReplaceTempView ("pessoas")
    spark.sql(
        """
        select Nome, AnoNascimento
        from pessoas 
        where AnoNascimento > 2000
        """
        ).show()

    print( df_nomes.where(
                (f.col("AnoNascimento") >= 1980) &\
                (f.col("AnoNascimento") <= 1994)) \
                .count() )

    spark.sql(
        """
        select count(*)
        from pessoas 
        where AnoNascimento >= 1980 
        AND AnoNascimento <= 1994
        """
        ).show()

    spark.sql(
        """
        select Pais, 

            case when AnoNascimento >= 1944 
            AND AnoNascimento <= 1964 
            then 'Baby Boomers'

            when AnoNascimento >= 1965 
            AND AnoNascimento <= 1979 
            then 'Geracao X'

            when AnoNascimento >= 1980 
            AND AnoNascimento <= 1994 
            then 'Millenials (Geracao Y)'

            when AnoNascimento >= 1995 
            AND AnoNascimento <= 2015 
            then 'Geracao Z'
             
            end as Geracao, count(*) as Quantidade

        from pessoas
        group by Pais, Geracao
        """
        ).show()

