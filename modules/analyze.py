from config import app

@app.task
def run(ip, project):
	launch_nmap(ip, project)
	modules = load_modules(project)
	services = analyze_nmap(project)	
	schedule_scans(modules, services)
	remove_nmap_output()

def launch_nmap(ip, project):
	#nmap -sT -A -O2 -p- -oA project/out IP
	pass

def analyze_nmap(project):
	services = []
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