#!/usr/bin/python3
# coding: utf8

import sys, getopt
import fileinput
import apt
from socket import *
import yaml
import os.path
import configparser # Permet de parser le fichier de paramètres


###########	remplace des éléments	###########
def replaceAll(file,searchExp,replaceExp):
	for line in fileinput.input(file, inplace=1):
		if searchExp in line:
			line = line.replace(searchExp,replaceExp)
		sys.stdout.write(line)


###########	DHCP	###########
def dhcp_conf(server_name,subnet_mask,domain,option_dns,sous_res,interfaces):
	cache = apt.Cache()
	pkg = cache['isc-dhcp-server'] # Access the Package object for python-apt
	pkg.mark_install()
	cache.commit()	

	fichier = open("/etc/dhcp/dhcpd.conf","w")
	fichier.write("##### Option générale par défaut #####\n")
	fichier.write("\n### RÉSEAU #####\n")
	fichier.write("\nserver-name \""+server_name+"\";") #nom du serveur dns
	fichier.write("\nauthoritative;")
	fichier.write("\noption subnet-mask "+subnet_mask+";")
	fichier.write("\noption domain-name \""+ domain +"\";")
	fichier.write("\noption domain-name-servers "+ option_dns +";")
	fichier.write("\nddns-update-style none;")
	fichier.write("\ndefault-lease-time 3600;")
	fichier.write("\nmax-lease-time 7200;")
	fichier.write("\nlog-facility local7;\n")
###########	sous reseaux	###########
	fichier.write("\n##### RÉSEAUX #####\n")
	fichier.write("\n## Déclaration sous réseaux")

	##interfaces= ''
	config = configparser.RawConfigParser() # On créé un nouvel objet "config"
	config.read('reseau.ini')

	i=0
	for i in range(0,sous_res):

		reseau = str("reseau"+str(i))
		subnet = config.get(reseau,'subnet')
		netmask = config.get(reseau,'netmask')
		broadcast = config.get(reseau,'broadcast')
		ntp = config.get(reseau,'ntp')
		routers = config.get(reseau,'routers')
		pool = config.get(reseau,'pool')

		fichier.write("\nsubnet "+subnet+" netmask "+netmask+" {")
		fichier.write("\n  option domain-name \""+domain+"\";")
		fichier.write("\n  option broadcast-address "+broadcast+";")
		fichier.write("\n  option ntp-servers "+ntp+";")
		fichier.write("\n  option routers "+routers+";")
		fichier.write("\n  range "+pool+";")
		fichier.write("\n}\n")
	fichier.close()

	replaceAll("/etc/default/isc-dhcp-server","INTERFACESv4=\"\"","INTERFACESv4=\""+interfaces+"\"")
	os.system("service isc-dhcp-server restart")

###########	main	###########
def main(argv):

   domain = ''
   server_name = ''
   subnet_mask = ''
   option_dns = ''
   sous_res = ''
   interfaces = ''

   try:
      opts, args = getopt.getopt(argv,"hd:n:m:o:r:f:",["domain=","name=","mask=","optdns=","reseau=","interfaces="])
   except getopt.GetoptError:
      print ('dhcp.py -d <domain>  -n <server name> -m <subnet mask> -o <option dns> -r <nb sous res> --interfaces="interface1 interface2 or_more"')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('dhcp.py -d <domain>  -n <server name> -m <subnet mask> -o <option dns> -r <nb sous res> --interfaces="interface1 interface2 or_more"')
         sys.exit()
      elif opt in ("-d", "--domain"):
         domain = arg
      elif opt in ("-n", "--name"):
         server_name = arg
      elif opt in ("-m", "--mask"):
         subnet_mask = arg
      elif opt in ("-o", "--optdns"):
         option_dns = arg
      elif opt in ("-r", "--reseau"):
         sous_res = int(arg)
      elif opt in ("-f", "--interfaces"):
         interfaces = arg
           
   dhcp_conf(server_name,subnet_mask,domain,option_dns,sous_res,interfaces)


if __name__ == "__main__":
   main(sys.argv[1:])






