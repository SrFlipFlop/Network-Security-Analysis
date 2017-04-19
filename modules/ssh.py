from config import app
from subprocess import Popen, PIPE

import os

print app

@app.task
def run(ip, project):
	print "[!] Start ssh module"
	create_folder(project)
	nmap_scripts(ip, project)
	print "[!] End ssh module"

def create_folder(project):
	os.makedirs("{0}ssh/".format(project))

def nmap_scripts(ip, project):
	ssh_scripts = [
		"ssh2-enum-algos.nse",
		"ssh-hostkey.nse",
		"sshv1.nse",
	]

	for script in ssh_scripts:
		cmd = "nmap -sT --script {0} -oN {1}ssh/nmap_{2}".format(script, project, script.replace('.nse', ''))
		p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
		c = p.communicate()
