from config import app
from subprocess import Popen, PIPE

import os

@app.task
def run(ip, project):
	print "[!] Start ftp module"
	create_folder(project)
	nmap_scripts(ip, project)
	print "[!] End ftp module"

def create_folder(project):
	try:
		os.makedirs("{0}ftp/".format(project))
	except:
		pass

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
		cmd = "nmap -sT --script={0} -oN {1}ftp/nmap_{2} {3}".format(script, project, script.replace('.nse', ''), ip)
		p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
		c = p.communicate()