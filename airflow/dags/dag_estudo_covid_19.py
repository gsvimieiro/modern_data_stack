from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.models import Variable
import json

with DAG(dag_id='trigger_airbyte_job',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily',
         start_date=days_ago(1)
         ) as dag:

    airbyte_economy_sf_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_economy-sf',
        airbyte_conn_id='poc-airbyte-airflow',
        connection_id='e49a2b45-1615-4e9f-aaf4-4f8677b9a6d4',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

#    airbyte_demographics_sf_sync = AirbyteTriggerSyncOperator(
#        task_id='airbyte_demographics-sf',
#        airbyte_conn_id='poc-airbyte-airflow',
#        connection_id=????,
#        asynchronous=False,
#        timeout=3600,
#        wait_seconds=3
#    )

    airbyte_economy_s3_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_economy-s3',
        airbyte_conn_id='poc-airbyte-airflow',
        connection_id='5978d61c-0ae0-4454-9b9a-aeedc3b30849',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

    [airbyte_economy_sf_sync] >> airbyte_economy_s3_sync