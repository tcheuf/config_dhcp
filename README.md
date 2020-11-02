#**config_dhcp**

Ce script permet d'automatiser l'installation d'un serveur dhcp  avec python.

Pour le lancer:

<code> sudo ./dhcp.py -d <domain> -n <server name> -m <subnet mask> -o <option dns> -r <nb sous res> --interfaces=<"interface1 interface2 ..."> </code>
  
Les fichiers dhcp.py et reseau.ini doivent être dans le même repertoire.
Le fichier reseau.ini doit contenir les differents sous réseaux déclarés comme suit:
  
  <img src="https://user-images.githubusercontent.com/72216948/97880528-91ab9700-1d21-11eb-88eb-d4ac8a55f988.png" width="100%"></img> 

##**options: ** 

-h : aide  
-d : rentrer votre nom de domaine dns (ex : mondomaine.fr)  
-n : rentrer votre nom de serveur dhcp (ex : routeur)  
-m : rentrer votre masque pour le serveur (ex : 255.255.255.0)  
-o : rentrer les options dns (ex : 8.8.8.8,1.1.1.1)  
-r : rentrer le nombre de sous réseau que vous avez configuré dans le fichier reseau.ini si vous mettez pas le bon, vos sous réseau ne 
seront pas configurés.  
--interfaces : rentrer vos interfaces d'écoute du serveur dhcp (ex : "enp0s8 enp0s9")  
