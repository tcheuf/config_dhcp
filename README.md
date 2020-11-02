#config_dhcp

Ce script permet d'automatiser l'installation d'un serveur dhcp  avec python.

Pour le lancer:sudo ./dhcp.py -d  <domain>  -n <server name> -m <subnet mask> -o <option dns> -r <nb sous res> --interfaces=<"interface1 interface2 ..."> 
  
Les fichiers dhcp.py et reseau.ini doivent être dans le même repertoire.
Le fichier reseau.ini doit contenir les differents sous réseaux déclarés comme suit:
  
  <img src="https://user-images.githubusercontent.com/72216948/97880528-91ab9700-1d21-11eb-88eb-d4ac8a55f988.png" width="100%"></img> 
