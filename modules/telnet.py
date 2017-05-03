from config import app
from subprocess import Popen, PIPE

import os

@app.task
def run(ip, project):
	print "[!] Start telnet module"
	create_folder(project)
	nmap_scripts(ip, project)
	print "[!] End telnet module"

def create_folder(project):
	try:
		os.makedirs("{0}telnet/".format(project))
	except:
		pass

def nmap_scripts(ip, project):
	telnet_scripts = [
		"telnet-brute.nse",
		"telnet-encryption.nse",
		"telnet-ntlm-info.nse"
	]

	for script in telnet_scripts:
		cmd = "nmap -sT --script {0} -oN {1}telnet/nmap_{2} {3}".format(script, project, script.replace('.nse', ''), ip)
		p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
		c = p.communicate()