from config import app
from subprocess import Popen, PIPE

import os

@app.task
def run(ip, project):
	print "[!] Start smb module"
	create_folder(project)
	nmap_scripts(ip, project)
	print "[!] End smb module"

def create_folder(project):
	os.makedirs("{0}smb/".format(project))

def nmap_scripts(ip, project):
	ssh_scripts = [
		"smb-brute.nse",
		"smb-enum-domains.nse",
		"smb-enum-groups.nse",
		"smb-enum-processes.nse",
		"smb-enum-sessions.nse",
		"smb-enum-shares.nse",
		"smb-enum-users.nse",
		"smb-flood.nse",
		"smb-ls.nse",
		"smb-mbenum.nse",
		"smb-os-discovery.nse",
		"smb-print-text.nse",
		"smb-psexec.nse",
		"smb-security-mode.nse",
		"smb-server-stats.nse",
		"smb-system-info.nse",
		"smbv2-enabled.nse",
		"smb-vuln-conficker.nse",
		"smb-vuln-cve2009-3103.nse",
		"smb-vuln-ms06-025.nse",
		"smb-vuln-ms07-029.nse",
		"smb-vuln-ms08-067.nse",
		"smb-vuln-ms10-054.nse",
		"smb-vuln-ms10-061.nse",
		"smb-vuln-regsvc-dos.nse"
	]

	for script in ssh_scripts:
		cmd = "nmap -sT --script={0} -oN {1}smb/nmap_{2}".format(script, project, script.replace('.nse', ''))
		p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
		c = p.communicate()

