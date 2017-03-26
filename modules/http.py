from config import app
from subprocess import Popen, PIPE

import os

@app.task
def run(ip, project):
	create_folder(project)
	nmap_scripts(ip, project)

def create_folder(project):
	os.makedirs("{0}http/".format(project))

def nmap_scripts(ip, project):
	http_scripts = []
