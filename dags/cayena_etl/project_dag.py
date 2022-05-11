# [START documentation]
# set up connectivity from airflow to gcp using [key] in json format
# create new bucket - cayena-bucket [GoogleCloudStorageCreateBucketOperator]
# transfer local file to cayena bucket [LocalFilesystemToGCSOperator]
# list objecs on the cayena bucket [GCSListObjectsOperator]
# create datatset on bigquery [BigQueryCreateEmptyDatasetOperator]
# transfer file in gcs to bigquery [GCSToBigQueryOperator]
# verify count of rows (if not null) [BigQueryCheckOperator]
# [END documentation]

# [START import module]
from airflow import DAG
from datetime import datetime
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.contrib.operators.gcs_operator import GoogleCloudStorageCreateBucketOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.gcs import GCSSynchronizeBucketsOperator, GCSListObjectsOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator, BigQueryCheckOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.operators.dummy import DummyOperator
from cayena_etl.src.domain.main import etl_web_scrapping, delete_data_files
# [END import module]

# [START import variables]
PROJECT_ID = Variable.get("cayena_project_id")
CAYENA_BUCKET = Variable.get("cayena_bucket")
BUCKET_LOCATION = Variable.get("cayena_bucket_location")
BQ_DATASET_NAME = Variable.get("cayena_bq_dataset_name")
# [END import variables]

# [START default args]
default_args = {
    'owner': 'Felipe Gomes',
    'depends_on_past': False
}
# [END default args]

# [START instantiate dag]
with DAG(
    dag_id="gcp-gcs-bigquery-cayena",
    tags=['development', 'cloud storage', 'google bigqueury', 'cayena'],
    default_args=default_args,
    start_date=datetime(year=2022, month=5, day=5),
    schedule_interval='@daily',
    catchup=False,
    description="ETL Process for Cayena Case"
) as dag:
# [END instantiate dag]

# [START set tasks]

    # create start task
    start = DummyOperator(task_id="start")
    
    # create end task
    end = DummyOperator(task_id="end")
    
    # create gcp bucket to cayena - cayena-bucket
    # https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_modules/airflow/providers/google/cloud/operators/gcs.html
    create_gcs_cayena_bucket = GoogleCloudStorageCreateBucketOperator(
        task_id="create_gcs_cayena_bucket",
        bucket_name=CAYENA_BUCKET,
        storage_class='STANDARD',
        location=BUCKET_LOCATION,
        labels={'env': 'dev', 'team': 'airflow'},
        gcp_conn_id="gcp_cayena"
    )
    
    # web scrapping scrit for site - https://books.toscrape.com/catalogue/page-1.html
    # https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/python/index.html#airflow.operators.python.PythonOperator
    run_web_scrapping_script = PythonOperator(
        task_id='run_web_scrapping_script',
        python_callable=etl_web_scrapping,
        provide_context=True,
        op_kwargs={
            "ingestion_date":"{{ ds }}"
        }
    )
    
    # transfer local books csv to cayena bucket - cayena-bucket
    # https://registry.astronomer.io/providers/google/modules/localfilesystemtogcsoperator
    upload_books_csv_to_gcs_cayena_bucket = LocalFilesystemToGCSOperator(
        task_id="upload_books_csv_to_gcs_cayena_bucket",
        src="dags/cayena_etl/data/*",
        dst="books-daily-data/",
        bucket=CAYENA_BUCKET,
        gcp_conn_id="gcp_cayena"
    )
    
    # list files inside of gcs bucket - books-daily-data from cayena bucket
    # https://registry.astronomer.io/providers/google/modules/gcslistobjectsoperator
    list_files_from_cayena_bucket_books_daily_data = GCSListObjectsOperator(
        task_id="list_files_from_cayena_bucket_books_daily_data",
        bucket=CAYENA_BUCKET,
        prefix="books-daily-data/",
        gcp_conn_id="gcp_cayena"
    )
    
    # delete all data in data folder - path: dags/cayena_etl/data
    # https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/python/index.html#airflow.operators.python.PythonOperator
    delete_all_local_data_in_data_folder = PythonOperator(
        task_id='delete_all_local_data_in_data_folder',
        python_callable=delete_data_files
    )
    

# [END set tasks]

# [START task sequence]
start >> create_gcs_cayena_bucket >> run_web_scrapping_script >> upload_books_csv_to_gcs_cayena_bucket >> list_files_from_cayena_bucket_books_daily_data >> delete_all_local_data_in_data_folder >> end
# [END task sequence]
