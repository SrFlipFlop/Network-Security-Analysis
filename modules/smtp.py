from config import app
from subprocess import Popen, PIPE

import os

@app.task
def run(ip, project):
	print "[!] Start smtp module"
	create_folder(project)
	nmap_scripts(ip, project)
	print "[!] End smtp module"

def create_folder(project):
	try:
		os.makedirs("{0}smtp/".format(project))
	except:
		pass

def nmap_scripts(ip, project):
	ssh_scripts = [
		"smtp-brute.nse",
		"smtp-commands.nse",
		"smtp-enum-users.nse",
		"smtp-ntlm-info.nse",
		"smtp-open-relay.nse",
		"smtp-strangeport.nse",
		"smtp-vuln-cve2010-4344.nse",
		"smtp-vuln-cve2011-1720.nse",
		"smtp-vuln-cve2011-1764.nse"
	]

	for script in ssh_scripts:
		cmd = "nmap -sT --script={0} -oN {1}smtp/nmap_{2} {3}".format(script, project, script.replace('.nse', ''), ip)
		p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
		c = p.communicate()
