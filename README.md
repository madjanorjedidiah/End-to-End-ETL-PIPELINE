# End to End ETL PIPELINE

This is a python script for building a basic end to end etl pipeline to read data from a source, transform
this data, then load the output into a prescribed location. The end to end etl pipeline.py file has been documented to aid you walk through this project.

## Getting Started

Download the project unto your local device. Run the script file in a python integrated development envirnment (IDE) or in your python virtual environment.

### Prerequisites

First and foremost, use the requirements.txt file to install the dependencies needed to run this project. After, run this project in your virtual environment. 


### Installing
Start by opening your terminal and going into your python virtual environment to install the dependcies through the requirements.txt file. After, navigate to the etl pipeline.py to run it in the python vitual environment. Also, install a postgres database.

OR

You can run it in your python IDE after you have installed the necessary dependencies.

## Transformations 
TASKS:
1. Select users from only one country of your choosing.
2. Extract the country and city into new columns.
3. Join this with the questions and only pick questions with at least 20 views.
4. Join the answers to the results of (3).

## DATA LOADING:
SQL DATA DEFINITION LANGUAGE(DDL)
1. Created a new schema called  stackoverflow_filtered.
2. Created one table called results.
3. Used spark to write the results into this table with the snippet below.
4. Created a btree  index on the reputation column within the results table.
5. Created a hash index on the display_name column within the results table.
6. From the results table, I created a view with the column names display_name, city,
questions_id  where the  accepted_answer_id is not null.  
7. Created a materialized view similar to (6). They should have different names.
8. In my Jupyter notebook, I stated the difference between views and materialized views.
```
until finished you should see these tasks completed.
```
I used pyspark and sql queries in answering and completing the tasks above. The .sql queries have in them queries that have been made to project certain question a user is likely to ask and the likely responses to get from such questions.


## Running the tests

After you have run these tests, you should have data extracted from a source, transformed and loaded into a postgres database. I used dbeaver to manage the postgresql queries. 

## Deployment
This can be deployed anywhere for end to end etl pipelines to run automatedly. Apache Airflow can be used to schedule the time interval for the script to run. You will just need to do a little tweaking to these scripts to get it working for your personlised project. 

## Author

* **Jedidiah Madjanor**
