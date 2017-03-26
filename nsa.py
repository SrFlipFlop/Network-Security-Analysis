#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from argparse import ArgumentParser
from ipaddress import ip_network, IPv4Address

from config import app
from modules.analyze import run

import os
import shutil
import datetime

def log(msg, level=0):
	if level == 0:
		print "[+] {0}".format(msg)
	elif level == 1:
		print "[!] {0}".format(msg)
	elif level == 2:
		print "[-] {0}".format(msg)
	elif level == 3:
		print "[?] {0}".format(msg)
		return raw_input("[?] Do you want to continue? [Y/n] ")

def parse_targets(targets):
	ips = []
	if ',' in targets:
		hosts, mask = targets.split('/')
		ips = map(lambda x: "{0}/{1}".format(x, mask), hosts.split(','))

	elif '-' in targets:
		base, x = targets.split('-')
		num, mask = x.split('/')
		low = base.split('.')[-1]
		for i in range(int(low), int(num) + 1):
			x1, x2, x3, x4 = base.split('.')
			ips.append("{0}.{1}.{2}.{3}/{4}".format(x1, x2, x3, i, mask))

	else:
		hosts = list(ip_network(u'{}'.format(targets), strict=False).hosts())
		base, mask = targets.split('/')
		if IPv4Address(base) in hosts:
			ips = [targets]
		else:
			ips = map(lambda x: "{0}/{1}".format(x, mask), hosts)	
	return ips

def exist_target(target, project):
	if os.path.isdir(project):
		ip = target.replace('/', '-')
		for root, dirs, files in os.walk(project):
			if ip in dirs:
				return True
	return False

def create_asset(target, project):
	if os.path.isdir(project):
		x = str(list(ip_network(u'{}'.format(target), strict=False).hosts())[0])
		network = "{0}.{1}-{2}".format('.'.join(x.split('.')[:-1]), 0, target.split('/')[-1])
		ip = target.replace('/', '-')		
		os.makedirs("{0}{1}/{2}".format(project, network, ip))
		return "{0}{1}/{2}/".format(project, network, ip)
	else:
		log("Project folder does not exist", 2)
		raise SystemExit

def update_asset(target, project):
	if os.path.isdir(project):
		x = str(list(ip_network(u'{}'.format(target), strict=False).hosts())[0])
		network = "{0}.{1}-{2}".format('.'.join(x.split('.')[:-1]), 0, target.split('/')[-1])
		ip = target.replace('/', '-')
		new_dir = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
		shutil.copytree("{0}{1}/{2}".format(project, network, ip), "{0}{1}/{2}/{3}".format(project, network, ip, new_dir))
		return "{0}{1}/{2}/".format(project, network, ip)

def main():
	parser = ArgumentParser()
	parser.add_argument('-t','--target', help='target: 10.0.0.1/24 | 10.0.0.1,10.0.0.2/24 | 10.0.0.1-5/24 | 10.0.0.0/24', required=True)
	parser.add_argument('-p','--project', help='project used to store all scans and information', required=True)
	parser.add_argument('-pj', '--print-json', action='store_true')
	parser.add_argument('-pn', '--print-normal', action='store_true')

	args = parser.parse_args()

	r = log("Using project directory {0}".format(args.project), 3) 
	if r not in ['Yes', 'Y', 'y', '']:
		raise SystemExit

	targets = parse_targets(args.target)
	for target in targets:
		if not exist_target(target, args.project):
			path = create_asset(target, args.project)
			print path
		else:
			path = update_asset(target, args.project)
			print path
			
		if args.print_normal:
			pass
		elif args.print_json:
			pass
		else:
			run.delay(target, path)


if __name__ == "__main__":
	main()