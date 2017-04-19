from config import app
from subprocess import Popen, PIPE

import os

@app.task
def run(ip, project):
	print "[!] Start snmp module"
	create_folder(project)
	nmap_scripts(ip, project)
	print "[!] End snmp module"

def create_folder(project):
	os.makedirs("{0}snmp/".format(project))

def nmap_scripts(ip, project):
	ssh_scripts = [
		"snmp-brute.nse",
		"snmp-hh3c-logins.nse",
		"snmp-info.nse",
		"snmp-interfaces.nse",
		"snmp-netstat.nse",
		"snmp-processes.nse",
		"snmp-sysdescr.nse",
		"snmp-win32-services.nse",
		"snmp-win32-shares.nse",
		"snmp-win32-software.nse",
		"snmp-win32-users.nse"
	]

	for script in ssh_scripts:
		cmd = "nmap -sT --script={0} -oN {1}snmp/nmap_{2}".format(script, project, script.replace('.nse', ''))
		p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
		c = p.communicate()