import pyspark
import pandas as pd
from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import lit
from pyspark.sql.functions import *
from subprocess import call

#  initialise spark session
spark = (
    SparkSession.builder
                .appName("Stack Overflow Data Wrangling")
                .config("spark.jars", "postgresql-42.2.8.jar") 
                .getOrCreate()
)


#  read spark data
questions = spark.read.csv(
    "questions.csv",
    header=True, inferSchema=True, multiLine=True, escape = '"'
    )

questions.printSchema()

#   renaming same column names
questions = questions.withColumnRenamed('id', 'questions_id') 
questions = questions.withColumnRenamed('user_id', 'question_user_id')
questions = questions.withColumnRenamed('created_at', 'questions_created_at')
questions.show(5)

#  read spark data
answers = spark.read.csv(
      "answers.csv",
    header=True, inferSchema=True,multiLine=True, escape = '"'
    )

#   renaming same column names
answers = answers.withColumnRenamed('id', 'answer_id') 
answers = answers.withColumnRenamed('user_id', 'answer_user_id')
answers.show(5)

#  read spark data
users = spark.read.csv(
    "users.csv",
    header=True, inferSchema=True,multiLine=True, escape = '"'
    )

users = users.withColumnRenamed('id', 'user_id')

#  Select users from only one country of your choosing.
users.registerTempTable('users')
userCountry = spark.sql("SELECT * FROM users WHERE location = 'India'").show(5)

indiaTb = users.filter(users.location.contains('India'))

#  renaming column
indiaTb = indiaTb.withColumn('location', lower(col('location')))

indiaTb = indiaTb.withColumn('location', regexp_replace('location', r"[,]\s*\w*\s*[,]", ','))
indiaTb.show(10)

#  Extract the country and city into new columns
indialoc = indiaTb.withColumn('location', split(indiaTb.location, ',')) \
  .select('user_id', 'display_name', 'views', 'reputation', 'updated_at', 'location', 'created_at', element_at(col('location'),-2).alias('city'), element_at(col('location'), -1).alias('country'))

#  display data
indialoc.show(5)

#  Join this with the questions and only pick questions with at least 20 view_counts.
quesIndia = indialoc.join(questions, indialoc.user_id == questions.question_user_id)
quesIndia.show(5)


quesIndia.filter(quesIndia.view_count >= 20).show(5)

#   renaming same column names
answers = answers.withColumnRenamed('body', 'answers_body') 
answers = answers.withColumnRenamed('score', 'answers_score') 
answers = answers.withColumnRenamed('comment_count', 'answers_comment_count') 
answers = answers.withColumnRenamed('created_at', 'answers_created_at')

#  Join the answers to the results of (3)
ansRes = quesIndia.join(answers, answers.question_id == quesIndia.questions_id, how='left')
ansRes.show(5)

#  casting to transform a strinf to an integer type
from pyspark.sql.types import IntegerType
ansRes = ansRes.withColumn("views", ansRes["views"].cast(IntegerType()))

#  Use this to return the minimum updated_at time.
min_ansRes = ansRes.select([min('updated_at')])
min_ansRes.show()

#  Use spark to write the results into this table with the snippet below
ansRes.write.format("jdbc").options(
    url='jdbc:postgresql://localhost/postgres',
    driver='org.postgresql.Driver',
    user='postgres',
    password='postgres1234',
    dbtable='stackoverflow_filtered.results'
).save(mode='append')


#  the difference between views and materialized views
The difference between a view and a materialised view is that a view serves as a virtual 
table with the query passed where as the materialised view serves as a physical store table for the query passed.