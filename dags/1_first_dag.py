  
from airflow.decorators import dag, task
from datetime import datetime


@dag(
    dag_id="first_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
)
def first_dag():

    @task
    def first_task():
        print("This is my first task")

    @task
    def second_task():
        print("This is my second task")

    @task
    def third_task():
        print("This is my third task")

    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third
   

first_dag()