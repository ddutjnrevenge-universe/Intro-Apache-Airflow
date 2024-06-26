from airflow.decorators import task, dag
from airflow.providers.docker.operators.docker import DockerOperator

from datetime import datetime

@dag(start_date=datetime(2024,1,1),schedule_interval='@daily',catchup=False)

def docker_dag():

        @task()
        def t1():
            pass

        t2 = DockerOperator(
              task_id='t2',
              api_version='auto',
              container_name='task_t2',
              image='stock:latest',
              command='python stock_data.py',
              docker_url='unix://var/run/docker.sock',
              network_mode='bridge',
              mount_tmp_dir=False, 
              xcom_all=True,
              retrieve_output=True,
              retrieve_output_path='/tmp/script.out',
              auto_remove=True
        )

        t1() >> t2

dag = docker_dag()

    
            