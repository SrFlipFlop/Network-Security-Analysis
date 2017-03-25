from celery import Celery

app = Celery('nsa', broker='redis://localhost:6379/0')