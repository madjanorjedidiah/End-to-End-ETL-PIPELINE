# SCRAPING REAL ESTATES LISTINGS

This is a python script that is building a basic ETL pipeline to read data from a source, transform
this data, then load the output into a prescribed location. The etl pipeline.py file has been documented for a walk through this project.

## Getting Started

Download the project unto your local device. Run the script file in a python integrated development envirnment (IDE) or in your python virtual environment.

### Prerequisites

First and foremost, use the requirements.txt file to install the dependencies needed to run this project. After, run this project in your virtual environment.


### Installing
Start by opening your terminal and going into your python virtual environment to install the dependcies through the requirements.txt file. After, navigate to the etl pipeline.py to run it in the python vitual environment.

OR

You can run it in your python IDE after you have installed the necessary dependencies.


```
until finished you should see data scraped into this table column format.
```
You should have an output free-7-million-company-dataset.zip in your local device. The script also involves filtering out companies with no domain name and then writting them to the formats stated below:

i.Parquet
ii.JSON (compressed using gzip )

Data is then uploaded to S3.

## Running the tests

After you have run these tests, you should see the data formats stated above written to your S3 bucket.

## Deployment
This can be deployed on aws to run automatedly. Apache Airflow can be used to schedule the time interval for the script to run.

## Author

* **Jedidiah Madjanor**
