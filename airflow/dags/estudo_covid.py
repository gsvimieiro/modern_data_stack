from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
import json

with DAG(dag_id='estudo_covid',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily',
         start_date=days_ago(1)
         ) as dag:

    airbyte_economy_sf_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_economy-sf',
        airbyte_conn_id='airbyte_connection',
        connection_id='74d2b99a-98cd-4182-a2e9-972adbfc778a',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

#    airbyte_demographics_sf_sync = AirbyteTriggerSyncOperator(
#        task_id='airbyte_demographics-sf',
#        airbyte_conn_id='airbyte_connection',
#        connection_id=????,
#        asynchronous=False,
#        timeout=3600,
#        wait_seconds=3
#    )

    airbyte_economy_s3_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_economy-s3',
        airbyte_conn_id='airbyte_connection',
        connection_id='d39aaba2-c421-40dc-bf78-b38d3f5611dd',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

    airbyte_economy_sf_sync >> airbyte_economy_s3_sync