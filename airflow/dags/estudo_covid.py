from airflow import DAG
import airflow.utils.dates
#from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id = "estudo_covid",
    schedule_interval='@daily',
    start_date=airflow.utils.dates.days_ago(14),
)

task_echo_message = BashOperator(
    task_id="echo_message",
    bash_command="echo teste",
    dag=dag
)

task_echo_message