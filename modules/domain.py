from config import app
from subprocess import Popen, PIPE

import os

@app.task
def run(ip, project):
	print "[!] Start domain module"
	create_folder(project)
	nmap_scripts(ip, project)
	print "[!] End domain module"

def create_folder(project):
	os.makedirs("{0}dns/".format(project))

def nmap_scripts(ip, project):
	ssh_scripts = [
		"dns-blacklist.nse",
		"dns-brute.nse",
		"dns-cache-snoop.nse",
		"dns-check-zone.nse",
		"dns-client-subnet-scan.nse",
		"dns-fuzz.nse",
		"dns-nsec3-enum.nse",
		"dns-nsec-enum.nse",
		"dns-nsid.nse",
		"dns-random-srcport.nse",
		"dns-random-txid.nse",
		"dns-recursion.nse",
		"dns-service-discovery.nse",
		"dns-srv-enum.nse",
		"dns-zone-transfer.nse",
	]

	for script in ssh_scripts:
		cmd = "nmap -sT --script={0} -oN {1}dns/nmap_{2} {3}".format(script, project, script.replace('.nse', ''), ip)
		p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
		c = p.communicate()
