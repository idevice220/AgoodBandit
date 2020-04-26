## configuration pour Netplan

print("choix 2") #on affiche que l'on à choisis le deuxieme choix

import subprocess #on import le subprocess pour acceder à l'invite de commande
import os.path

mon_fichierlog = open("/var/log/logScript.log","a")
mon_fichierlog.write("configuration de L'interface réseau \n")

print("nom de l'interface") #on demande le nom de l'interface à configurer
interface = input() #on récupere la donnée
interface = str(interface) #on convertie la valeur en chaine de caracteres

print("dhcp yes or no ?")
dhcp_enable = input()
try:
	dhcp_enable = str(dhcp_enable)
except ValueError:
	print("Erreur")

print("submask")
submask = input()
submask = int(submask)
if submask < 0: #on fait un test pour être sur que la valeur soit compatible
	print("Valeur négative")

if submask > 32:
	print("valeur trop élevé")

submask = str(submask)


print("addresse ip du serveur ex: 192.168.1.10")
addresse_ip = input()
addresse_ip = str(addresse_ip)

print("gateway ex: 192.168.1.254")
gateway = input()
gateway = str(gateway)

print("DNS ex 8.8.8.8, 8.8.4.4")
dns = input()
dns = str(dns)

process48 = subprocess.Popen(["touch", "test.yaml"]) #on cré un fichier .yaml
mon_fichier = open("test.yaml","w") #on ouvre le fichier iscp-dhcp-server

## creation du fichier avec le différentes variables et le texte ##
mon_fichier.write('network:\n')
mon_fichier.write('  version: 2\n')
mon_fichier.write('  renderer: NetworkManager\n')
mon_fichier.write('  ethernets:\n    ')
mon_fichier.write(    interface)
mon_fichier.write(":\n")
mon_fichier.write("      dhcp4: ")
mon_fichier.write(dhcp_enable)
mon_fichier.write("\n")
mon_fichier.write("      addresses: [")
mon_fichier.write(addresse_ip)
mon_fichier.write("/")
mon_fichier.write(submask)
mon_fichier.write("]\n")
mon_fichier.write("      gateway4: ")
mon_fichier.write(gateway)
mon_fichier.write("\n")
mon_fichier.write("      nameservers:")
mon_fichier.write("\n")
mon_fichier.write("        addresses: [")
mon_fichier.write(dns)
mon_fichier.write("]")


mon_fichier.close()

mon_fichierlog.write("application du fichié de configuration \n")


process9 = subprocess.Popen(["mv", "test.yaml", "/etc/netplan/netplan.yaml"]) #on bouge le fichier pour le mettre dans le repertoire adequat
process10 = subprocess.Popen(["netplan", "apply"]) #on applique les changements


mon_fichierlog.write("Interface réseau confuguré \n")

print("interface reseau configuré")
