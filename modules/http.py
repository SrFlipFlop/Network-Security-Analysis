from config import app
from subprocess import Popen, PIPE

import os

@app.task
def run(ip, project):
	create_folder(project)
	nmap_scripts(ip, project)
	nikto(ip, project)

def create_folder(project):
	os.makedirs("{0}http/".format(project))

def nmap_scripts(ip, project):
	http_scripts = [
		"http-apache-negotiation.nse",
		"http-apache-server-status.nse",
		"http-aspnet-debug.nse",
		"http-auth-finder.nse",
		"http-auth.nse",
		"http-backup-finder.nse",
		"http-brute.nse",
		"http-cakephp-version.nse",
		"http-cisco-anyconnect.nse",
		"http-coldfusion-subzero.nse",
		"http-comments-displayer.nse",
		"http-config-backup.nse",
		"http-cross-domain-policy.nse",
		"http-csrf.nse",
		"http-default-accounts.nse",
		"http-devframework.nse",
		"http-dlink-backdoor.nse",
		"http-dombased-xss.nse",
		"http-drupal-enum.nse",
		"http-drupal-enum-users.nse",
		"http-enum.nse",
		"http-fileupload-exploiter.nse",
		"http-form-brute.nse",
		"http-form-fuzzer.nse",
		"http-generator.nse",
		"http-headers.nse",
		"http-iis-short-name-brute.nse",
		"http-iis-webdav-vuln.nse",
		"http-internal-ip-disclosure.nse",
		"http-joomla-brute.nse",
		"http-majordomo2-dir-traversal.nse",
		"http-methods.nse",
		"http-method-tamper.nse",
		"http-passwd.nse",
		"http-phpmyadmin-dir-traversal.nse",
		"http-phpself-xss.nse",
		"http-php-version.nse",
		"http-put.nse",
		"http-rfi-spider.nse",
		"http-robots.txt.nse",
		"http-shellshock.nse",
		"http-sitemap-generator.nse",
		"http-slowloris-check.nse",
		"http-slowloris.nse",
		"http-sql-injection.nse",
		"http-stored-xss.nse",
		"http-traceroute.nse",
		"http-userdir-enum.nse",
		"http-vuln-cve2006-3392.nse",
		"http-vuln-cve2009-3960.nse",
		"http-vuln-cve2010-0738.nse",
		"http-vuln-cve2010-2861.nse",
		"http-vuln-cve2011-3192.nse",
		"http-vuln-cve2011-3368.nse",
		"http-vuln-cve2012-1823.nse",
		"http-vuln-cve2013-0156.nse",
		"http-vuln-cve2013-6786.nse",
		"http-vuln-cve2013-7091.nse",
		"http-vuln-cve2014-2126.nse",
		"http-vuln-cve2014-2127.nse",
		"http-vuln-cve2014-2128.nse",
		"http-vuln-cve2014-2129.nse",
		"http-vuln-cve2014-3704.nse",
		"http-vuln-cve2014-8877.nse",
		"http-vuln-cve2015-1427.nse",
		"http-vuln-cve2015-1635.nse",
		"http-vuln-misfortune-cookie.nse",
		"http-waf-detect.nse",
		"http-waf-fingerprint.nse",
		"http-webdav-scan.nse",
		"http-wordpress-brute.nse",
		"http-wordpress-enum.nse",
		"http-wordpress-users.nse",
		"http-xssed.nse",
	]
	for script in ssh_scripts:
		cmd = "nmap -sT --script {0} -oN {1}http/nmap_{2} {3}".format(script, project, script.replace('.nse', ''), ip)
		p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
		c = p.communicate()

def nikto(ip, project):
	cmd = "nikto -h http://{0} | tee {1}/http/nikto_out.txt".format(ip, project)
	p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
	c = p.communicate()

def sqlmap(ip, project):
	cmd = "sqlmap -u http://{0} --forms --batch --crawl=10 --level=5 --risk=3 | tee {1}/http/sqlmap_out.txt".format(ip, project)
	p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
	c = p.communicate()
    
def dirb(ip, project):
    cmd = "dirb http://{0}/ | tee {1}/http/dirb_out.txt".format(ip, project)
    p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE)
    c = p.communicate()
