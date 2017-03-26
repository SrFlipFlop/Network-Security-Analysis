from config import app
from subprocess import Popen, PIPE
from importlib import import_module
from modules import *

import xml.etree.ElementTree as tree
import os

@app.task
def run(ip, project):
	launch_nmap(ip, project)
	modules = load_modules()
	services = analyze_nmap(ip, project)
	schedule_scans(modules, services, ip, project)

def launch_nmap(ip, project):
	cmd = "nmap -sT -A -O2 -p- -oA {0}nmap_out {1}".format(project, ip.split('/')[0])
	p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
	c = p.communicate()

def analyze_nmap(ip, project):
	services = []	
	xml = tree.parse("{0}nmap_out.xml".format(project))
	root = xml.getroot()
	host = root.find('host')
	ports = host.find('ports')
	for port in ports.findall('port'):
		service = port.find('service')
		if service is not None:
			services.append(service.attrib['name'])
	return services

def load_modules():
	modules = []
	for root, dirs, files in os.walk('./modules'):
		modules += filter(lambda x: '__' not in x and 'pyc' not in x, files)
	return modules

def schedule_scans(modules, services, ip, project):
	log("Services founded: {0}".format(services), 0)
	log("Modules loaded: {0}".format(modules), 0)
	for service in services:
		if service in services:
			module = import_module("modules.{0}".format(service))
			module.run.delay(ip, project)

def log(msg, level=0):
	if level == 0:
		print "[+] {0}".format(msg)
	elif level == 1:
		print "[!] {0}".format(msg)
	elif level == 2:
		print "[-] {0}".format(msg)
