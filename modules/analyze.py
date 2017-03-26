from config import app
from subprocess import Popen, PIPE

@app.task
def run(ip, project):
	launch_nmap(ip, project)
	modules = load_modules()
	services = analyze_nmap(ip, project)	
	schedule_scans(modules, services)
	remove_nmap_output()

def launch_nmap(ip, project):
	cmd = "nmap -sT -A -O2 -p- -oA {0}{1}/nmap_out {2}".format(project, ip.replace('/','-'), ip.split('/')[0])
	p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
	c = p.communicate()

def analyze_nmap(ip, project):
	services = []
	try:
		xml = tree.parse("{0}{1}/nmap_out.xml".format(project, ip.replace('/','-')))
		root = xml.getroot()
		host = root.find('host')
		ports = host.find('ports')
		for port in ports.findall('port'):
			service = port.find('service')
			if service is not None:
				services.append(service.attrib['name'])
		return services
	except Exception as e:
		print "ERROR PARSING NMAP", e
	return services

def load_modules():
	modules = []
	return modules

def schedule_scans(modules, services):
	#launch a module for founded service
	pass

def remove_nmap_output():
	#remove .xml and .gnmap out
	pass