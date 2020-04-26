import os.path
import datetime
import time
import subprocess

print("choix 1") #on affiche que l'on à choisis le premier choix

mon_fichierlog = open("/var/log/logScript.log","a")
mon_fichierlog.write("configuration Serveur DHCP \n")



process4 = subprocess.Popen(["rm", "/etc/default/isc-dhcp-server"])
process20 = subprocess.Popen(["apt", "-", "update"])
time.sleep(2)
process1 = subprocess.Popen(["apt", "-", "install", "isc-dhcp-server"]) #premier process est d'installer le serveur DHCP
time.sleep(2)

print("plusieurs interfaces à activer 1 = oui 0 = non")
multiple_interface = input()
try: #test
	multiple_interface = int(multiple_interface)
except ValueError:
	print("Erreur")

if multiple_interface > 2:
	print("mauvaise valeur saisie")




if multiple_interface == 0:
	print("nom de l'interface") #on demande le nom de l'interface à configurer
	interface = input() #on récupere la donnée
	interface = str(interface) #on convertie la valeur en chaine de caracteres
if multiple_interface == 1:
	print("nom de la premiere interface") #on demande le nom de l'interface à configurer
	interface = input() #on récupere la donnée
	interface = str(interface) #on convertie la valeur en chaine de caracteres
	print("nom de la deuxieme interface")
	interface2 = input()
	interface2 = str(interface2)


process2 = subprocess.Popen(["touch", "isc-dhcp-server"]) #on cré un fichier isc-dhcp-server
mon_fichier = open("isc-dhcp-server","w") #on ouvre le fichier iscp-dhcp-server




mon_fichier.write('INTERFACESv4="')

if multiple_interface == 0:
	mon_fichier.write(interface) #on rajoute au fichier le contenu de la variable interface
	mon_fichier.write('\"')
	mon_fichier.close()

if multiple_interface == 1:
	mon_fichier.write(interface)
	mon_fichier.write(" ")
	mon_fichier.write(interface2)
	mon_fichier.write('\"')
	mon_fichier.close() #on ferme le fichier


process3 = subprocess.Popen(["mv", "isc-dhcp-server", "/etc/default/isc-dhcp-server"]) #on bouge le fichier pour le mettre dans le repertoire adequat

##On récupère les données nécessaires à remplir le fichier de configuration##

print("plage ip")
plage_ip = input()
plage_ip = str(plage_ip)
print("réseau ?")
reseau_ip = input()
reseau_ip = str(reseau_ip)
print("DNS ?")
dns = input()
dns = str(dns)
print("routeur ?")
routeur = input()
routeur = str(routeur)
print("broadcast")
broadcast = input()
broadcast = str(broadcast)
process4 = subprocess.Popen(["touch", "dhcpd.conf"]) #on cré le fichier de configuration
mon_fichier2 = open("dhcpd.conf","w") #on ouvre le fichier dhcpd.conf

##On remplit le fichier de configuration##
mon_fichier2.write('option domain-name "example.org";\n')
mon_fichier2.write('option domain-name-servers ns1.example.org, ns2.example.org;\n')
mon_fichier2.write('default-lease-time 600;\n')
mon_fichier2.write('max-lease-time 7200;\n')
mon_fichier2.write('ddns-update-style none;\n')
mon_fichier2.write('authoritative;\n')
mon_fichier2.write('subnet ')
mon_fichier2.write(reseau_ip)
mon_fichier2.write(" netmask 255.255.255.0 {\n")
mon_fichier2.write(' range ')
mon_fichier2.write(plage_ip)
mon_fichier2.write(";\n")
mon_fichier2.write(" option domain-name-servers ")
mon_fichier2.write(dns)
mon_fichier2.write(";\n")
mon_fichier2.write(" option subnet-mask 255.255.255.0")
mon_fichier2.write(";\n")
mon_fichier2.write(" option routers ")
mon_fichier2.write(routeur)
mon_fichier2.write(";\n")
mon_fichier2.write(" option broadcast-address ")
mon_fichier2.write(broadcast)
mon_fichier2.write(";\n")
mon_fichier2.write(" default-lease-time 600;\n")
mon_fichier2.write(" max-lease-time 7200;\n")
mon_fichier2.write("}")
mon_fichier2.close()
process5 = subprocess.Popen(["mv", "dhcpd.conf", "/etc/dhcp/dhcpd.conf"]) #on bouge le fichier pour le mettre dans le repertoire adequat
process6 = subprocess.Popen(["systemctl", "restart", "isc-dhcp-server"]) #on redemarre dhcp pour qu'il prenne les paramètres

mon_fichierlog.write('serveur dhcp configuré \n')
