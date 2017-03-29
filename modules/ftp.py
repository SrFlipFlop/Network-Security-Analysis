from config import app
from subprocess import Popen, PIPE

import os

@app.task
def run(ip, project):
	create_folder(project)
	nmap_scripts(ip, project)

def create_folder(project):
	os.makedirs("{0}ftp/".format(project))

def nmap_scripts(ip, project):
	ssh_scripts = [
		"ftp-anon.nse",
		"ftp-bounce.nse",
		"ftp-brute.nse",
		"ftp-libopie.nse",
		"ftp-proftpd-backdoor.nse",
		"ftp-vsftpd-backdoor.nse",
		"ftp-vuln-cve2010-4221.nse",
		"tftp-enum.nse"
	]

	for script in ssh_scripts:
		cmd = "nmap -sT --script={0} -oN {1}ftp/nmap_{2}".format(script, project, script.replace('.nse', ''))
		p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
		c = p.communicate()