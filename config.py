from celery import Celery

import os

def load_modules():
    modules = []
    for root, dirs, files in os.walk('./modules'):
        modules += map(lambda y: "modules.{0}".format(y.replace('.py', "")), filter(lambda x: '__' not in x and 'pyc' not in x, files))
    return modules

app = Celery('nsa', broker='redis://localhost:6379/0', include=load_modules())