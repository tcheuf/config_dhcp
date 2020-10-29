#config_dhcp
Ce script permet d'automatiser l'installation d'un serveur dhcp  avec python.
Pour le lancer:sudo ./dhcp_dns.py -d <domain> -n <server name> -m <subnet mask> -o <option dns> -r <nb sous res> --interfaces=<"interface1 interface2 ..."> 
Les fichiers dhcp.py et reseau.ini doivent être dans le même repertoire.
Le fichier reseau.ini doit contenir les differents sous réseaux déclarer comme suit:

[reseau0]
subnet: 192.168.10.0
netmask: 255.255.255.0
broadcast: 192.168.10.255
ntp:  192.168.10.1
routers: 192.168.10.1
pool: 192.168.10.2 192.168.10.254

[reseau1]
subnet: 192.168.20.0
netmask: 255.255.255.0
broadcast: 192.168.20.255
ntp: 192.168.10.1
routers:  192.168.20.1
pool:  192.168.20.2 192.168.20.254


