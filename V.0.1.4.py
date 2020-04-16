#acueil du programme
import datetime
import subprocess
import os
import os.path
from random import randrange
from math import ceil
import time
i=0 #compteur
process70 = subprocess.Popen(["touch", "/var/log/logScript.log"])
mon_fichierlog = open("/var/log/logScript.log","a") #on cré le fichier logScript qui contiendra les logs
mon_fichierlog.write('Ouverture du programme  ') #on ecrit la premiere ligne dans le fichier de logs




mon_fichierlog.write('\n') #log

print("Voulez vous rentre en mode duplication ? 1 oui 0 non ") #mode duplication
duplication_enable = input()
duplication_enable = int(duplication_enable)

if duplication_enable == 1:
	print("mode duplication activé")
	if os.path.isfile('duplication.txt'):
		print("fichier trouvé")
		liste = open("duplication.txt", "r").read()


	else:
		print("fichier non trouvé")
		print("mode duplication non activé")
		duplication_enable = 'n'




elif duplication_enable == 0:
	print("mode duplication pas activé")
else:
	print("répondez par 1 ou 0")







#On fait une boucle afin de rester dans le programme même après être arrivé à la fin
while i == 0:

	print("Acueil : faites votre choix") #On affiche l'acueil
	print("1 = DHCP  2 = Netplan  3 = Serveur de fichier 4 = Nouveau dossier partagé 5 = Table de routage 0 = quitter")

#        mon_fichierlog.write("Saisit de l'utilisateur\n") #log

	choix_acueil = input()
	try: #on fait un test pour être sûr que la valeur rentré soit correct
		choix_acueil = int(choix_acueil)
	except ValueError:
		print("Vous n'avez pas saisit un bon numéro")
#                mon_fichierlog.write("Vous n'avez pas saisit un bon numéro\n")
	if choix_acueil < 0:
		print("ce nombre est négatif")
#                mon_fichierlog.write("Nombre saisit négatif\n")
	if choix_acueil > 5:
		print("ce chiffre est supérieur à 5")
#                mon_fichierlog.write("Numéro saisit supérieur à 5\n")


## Si l'on choisit l'option 1
#######################################affectation de l'interface DHCP à configurer#############################################################


	if choix_acueil == 1 and duplication_enable ==0:

		print("choix 1") #on affiche que l'on à choisis le premier choix

		import subprocess #on import le subprocess pour acceder à l'invite de commande

		process4 = subprocess.Popen(["rm", "/etc/default/isc-dhcp-server"])

		process20 = subprocess.Popen(["apt", "-", "update"])
		time.sleep(2) #on attend que les paquets se mettent à jours
		process1 = subprocess.Popen(["apt", "-", "install", "isc-dhcp-server"]) #premier process est d'installer le serveur DHCP
		time.sleep(20) # on attend que le logciel soit intallé
		mon_fichierlog.write("Configuration du DHCP\n")


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

		mon_fichierlog.write("Création du fichier de configuration du DHCP\n")


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
		mon_fichierlog.write("Copie du fichier de Configuration et Redémarrage du serveur DHCP\n")
		process5 = subprocess.Popen(["mv", "dhcpd.conf", "/etc/dhcp/dhcpd.conf"]) #on bouge le fichier pour le mettre dans le repertoire adequat
		process6 = subprocess.Popen(["systemctl", "restart", "isc-dhcp-server"]) #on redemarre dhcp pour qu'il prenne les paramètres

		print("Serveur DHCP installé")
		print("Voulez-vous faire le routage tout de suite ? 1 = oui 0 = non")

		jumpto_rout = input() #on récupere la donnée
		jumpto_rout = int(jumpto_rout) #on convertie la valeur en chaine de caracteres

		if jumpto_rout == 1:
			choix_acueil = 5

#                mon_fichierlog.write("Serveur DHCP installé\n")

##fin de l'installation du serveur DHCP###############
## configuration pour Netplan


	if choix_acueil == 2 and duplication_enable ==0:

		mon_fichierlog.write("Configuration de Netplan\n")
		print("choix 2") #on affiche que l'on à choisis le deuxieme choix

		import subprocess #on import le subprocess pour acceder à l'invite de commande

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

		mon_fichierlog.write("Création du fichier de configuration\n")
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

		mon_fichierlog.write("Copie du fichier de configuration et redémarrage de Netplan\n")

		mon_fichier.close()


		process9 = subprocess.Popen(["mv", "test.yaml", "/etc/netplan/netplan.yaml"]) #on bouge le fichier pour le mettre dans le repertoire adequat
		process10 = subprocess.Popen(["netplan", "apply"]) #on applique les changements

		print("interface reseau configuré")
		mon_fichierlog.write("Netplan Configuré\n")



###########Configuration Serveur de fichiers#####################


###########"SAMBA"#######################

	if choix_acueil == 3:

		print("choix 3") #on affiche le menu dans lequel on va rentrer

		print ("1 = Samba  2 = NFS")

		choix_serveur_fichier = input()

		try:
			choix_serveur_fichier = int(choix_serveur_fichier)
		except ValueError:
			print("Erreur")
		if choix_serveur_fichier < 0:
			print("valeur négative")
		if choix_serveur_fichier > 2:
			print("valeur fausse")

		if choix_serveur_fichier == 1:
			mon_fichierlog.write("Configuration Samba\n")

			import subprocess #on importe le subprocess pour acceder à l'invite de commande
			process21 = subprocess.Popen(["apt", "-", "update"])
			time.sleep(20)

			process10 = subprocess.Popen(["apt","-","install","samba"])

			time.sleep(15) #on attend que le programme se télécharge

			print("réseau autorisé ? ex:192.168.0.0/16")
			hosts_allow = input()
			hosts_allow = str(hosts_allow)



			mon_fichierlog.write("Création du dossier partagé et du fichier de configuration Samba\n")
			process11 = subprocess.Popen(["mkdir","/home/share"])
			process12 = subprocess.Popen(["chmod","a+rwx","/home/share"])
			process13 = subprocess.Popen(["touch","smb.conf"])
			mon_fichier = open("smb.conf","w") #on ouvre le fichier texte

			mon_fichier.write('[global]\n')
			mon_fichier.write('server role = standalone server\n')
			mon_fichier.write('usershare allow guests = yes\n')
			mon_fichier.write('hosts allow = ')
			mon_fichier.write(hosts_allow)
			mon_fichier.write('\n')
			mon_fichier.write('\n')
			mon_fichier.write("[share]")
			mon_fichier.write('\n')
			mon_fichier.write('comment = share\n')
			mon_fichier.write('path = /home/share\n')
			mon_fichier.write('read only = no\n')
			mon_fichier.write('guest ok = yes')

			mon_fichierlog.write("Copie du fichier de configuration et redémarrage du serveur SAmba\n")

			mon_fichier.close()


			process14 = subprocess.Popen(["mv", "smb.conf", "/etc/samba/smb.conf"]) #on bouge le fichier pour le mettre dans le repertoire adequat
			process15 = subprocess.Popen(["systemctl", "restart", "smbd"]) #on applique les changements

			print("Serveur de fichier installé (Samba)")



##############"NFS"#################################


		if choix_serveur_fichier == 2:


			import subprocess #on import le subprocess pour acceder à l'invite de commande
			process90 = subprocess.Popen(["apt", "-", "install", "nfs-common"]) #process est d'installer les outils NFS
			time.sleep(20)
			process91 = subprocess.Popen(["apt", "-", "install", "nfs-server"]) #process est d'installer le serveur NFS
			time.sleep(20)
			mon_fichierlog.write("Récupération des données afin de configurer NFS\n")

			print("addresse réseau du dossier partagé")
			addresse_dossier_partage = input()
			addresse_dossier_partage = str(addresse_dossier_partage)

			print("masque de sous réseau (ex: 24 = /24)")
			masquedesousreseau = input()
			masquedesousreseau = str(masquedesousreseau)

			mon_fichierlog.write("Création du dossier partagé et du fichier de configuration\n")
			process16 = subprocess.Popen(["mkdir", "/home/ftp"])

			process17 = subprocess.Popen(["touch", "exports"]) #

			mon_fichier = open("exports","w")

			mon_fichier.write('/home/ftp ')
			mon_fichier.write(addresse_dossier_partage)
			mon_fichier.write('/')
			mon_fichier.write(masquedesousreseau)
			mon_fichier.write("(ro,sync,root_squash,no_subtree_check,fsid=0)")

			mon_fichier.close()
			process18 = subprocess.Popen(["mv", "exports", "/etc/exports"]) #

			process92 = subprocess.Popen(["/etc/init.d/nfs-kernel-server", "restart"]) #On redemarre NFS


			print("Serveur de fichier installé (NFS)")
			mon_fichierlog.write("Serveur NFS installé\n")


	if choix_acueil == 4:

		import subprocess #on import le subprocess pour acceder à l'invite de commande
		print("Nom du dossier ?")
		nom_dossier = input()
		nom_dossier = str(nom_dossier)

		print("quel est la localisation de votre dossier")
		path = input()
		path = str(path)

		process75 = subprocess.call(['mkdir',  nom_dossier])

		mon_fichierlog.write("Installation nouveau dossier partagé\n")

		process76 = subprocess.call(['chmod', 'a+rwx',nom_dossier])


		mon_fichier = open("/etc/samba/smb.conf","a") #on ouvre le fichier texte

		mon_fichier.write("\n[")
		mon_fichier.write(nom_dossier)
		mon_fichier.write("]\n")
		mon_fichier.write('\n')
		mon_fichier.write('comment = ')
		mon_fichier.write(nom_dossier)
		mon_fichier.write('\n')
		mon_fichier.write('path = ')
		mon_fichier.write(path)
		mon_fichier.write('\n')
		mon_fichier.write('read only = no\n')
		mon_fichier.write('guest ok = yes')

		mon_fichierlog.write("Copie du fichier de configuration et redémarrage du serveur SAmba\n")

		mon_fichier.close()

		process77 = subprocess.Popen(["systemctl", "restart", "smbd"])

		mon_fichierlog.write("Nouveau dossié partagé créé\n")


	if choix_acueil == 5:

		import subprocess #on import le subprocess pour acceder à l'invite de commande


		print("Nom de l'interface à router ?")
		int_rout = input()
		int_rout = str(int_rout)



		print("Application de la table de routage")

		process78 = subprocess.call(['iptables',  '-t', 'nat', '-A', 'POSTROUTING', '-o', int_rout, '-j', 'MASQUERADE'])
		process79 = subprocess.call(["ufw", "reload"])
		print("Table de routage modifié")






	if choix_acueil == 1 and duplication_enable == 1:

		print("choix 1") #on affiche que l'on à choisis le premier choix
		import subprocess #on import le subprocess pour acceder à l'invite de c

#		process4 = subprocess.Popen(["rm", "/etc/default/isc-dhcp-server"])

#                       process20 = subprocess.Popen(["apt", "-", "update"])
#                       time.sleep(2) #on attend que les paquets se mettent à jours
#                       process1 = subprocess.Popen(["apt", "-", "install", "isc-dhcp-server"])
#                       time.sleep(20) # on attend que le logciel soit intallé

		with open('duplication.txt','r') as fich:
			for i in range(1):
				multiple_interface = fich.readline()
				multiple_interface = int(multiple_interface)




		if multiple_interface == 0:
			with open('duplication.txt','r') as fich:
				for i in range(2):
					interface = fich.readline()
					interface = str(interface)
					print(interface)
				process41 = subprocess.Popen(["touch", "isc-dhcp-server"])
				f = open("isc-dhcp-server","w")
				f.write('INTERFACESv4"')
				f.write(interface )
				f.write('"')
				f.close()


		if multiple_interface == 1:
			with open('duplication.txt','r') as fich:
				for i in range(2):
					interface = fich.readline()
					interface = str(interface)
					print(interface)
			with open('duplication.txt', 'r') as fich:
				for i in range(3):
					interface2 = fich.readline()
					interface2 = str(interface2)
					print(interface2)
				process40 = subprocess.Popen(["touch", "isc-dhcp-server"])
				f = open("isc-dhcp-server","w")
				f.write('INTERFACESv4="')
				f.write(interface)
				f.write(", ")
				f.write(interface2)
				f.write('"')
				f.close()
		process43 = subprocess.Popen(["mv", "isc-dhcp-server", "/etc/default/isc-dhcp-server"])



		with open('duplication.txt','r') as fich:
			for i in range(4):
				plage_ip = fich.readline()
				plage_ip = str(plage_ip)
				print(plage_ip)

		with open('duplication.txt','r') as fich:
			for i in range(5):
				reseau_ip = fich.readline()
				reseau_ip = str(reseau_ip)
				print(reseau_ip)


		with open('duplication.txt','r') as fich:
			for i in range(6):
				dns = fich.readline()
				dns = str(dns)
				print(dns)


		with open('duplication.txt','r') as fich:
			for i in range(7):

				routeur = fich.readline()
				routeur = str(routeur)
				print(routeur)


		with open('duplication.txt','r') as fich:
			for i in range(8):
				broadcast = fich.readline()
				broadcast = str(broadcast)
				print(broadcast)

		process44 = subprocess.Popen(["touch", "dhcpd.conf"])


		mon_fichier2 = open("dhcpd.conf","w") #on ouvre le fichier dhcpd.conf

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






		process41 = subprocess.Popen(["mv", "dhcpd.conf", "/etc/dhcp/dhcpd.conf"]) #on bouge le fichier po
		process42 = subprocess.Popen(["systemctl", "restart", "isc-dhcp-server"])








	if choix_acueil == 2 and duplication_enable == 1:

		print("choix 2")

		import os.path
		if os.path.isfile('netplan.txt'):
			print("fichier trouvé")









		else:
			print("fichier non trouvé")
			choix_acueil == 2 and duplication_enable == 0






		import subprocess

		process52 = subprocess.Popen(["rm", "/etc/netplan/netplan.yaml"])

#		process53 = subprocess.Popen(["apt", "-", "update"])
#		process54 = subprocess.Popen(["apt", "-", "intall", ""])

		with open('netplan.txt','r') as fich:
			for i in range(1):
				interface = fich.readline()
				interface = str(interface)
				print(interface[:5])
		with open('netplan.txt','r') as fich:
			for i in range(2):
				dhcp_enable = fich.readline()
				dhcp_enable = str(dhcp_enable)
				print(dhcp_enable)
		with open('netplan.txt','r') as fich:
			for i in range(3):
				submask = fich.readline()
				submask = str(submask)
				print(submask)
		with open('netplan.txt','r') as fich:
			for i in range(4):
				addresse_ip = fich.readline()
				addresse_ip = str(addresse_ip)
				print(addresse_ip)
		with open('netplan.txt','r') as fich:
			for i in range(5):
				gateway = fich.readline()
				gateway = str(gateway)
				print(gateway)
		with open('netplan.txt','r') as fich:
			for i in range(6):
				dns = fich.readline()
				dns = str(dns)
				print(dns)


		process53 = subprocess.Popen(["touch", "netplan.yaml"])
		mon_fichier = open("netplan.yaml","w")

		mon_fichier.write('network:\n')
		mon_fichier.write('  version: 2\n')
		mon_fichier.write('  renderer: NetworkManager\n')
		mon_fichier.write('  ethernets:\n')
		mon_fichier.write('    ' )
		mon_fichier.write(interface[:5])
		mon_fichier.write(":\n")
		mon_fichier.write("      dhcp4: ")
		mon_fichier.write(dhcp_enable[:2])
		mon_fichier.write("\n")
		mon_fichier.write("      addresses: [")
		mon_fichier.write(addresse_ip[:12])
		mon_fichier.write("/")
		mon_fichier.write(submask[:2])
		mon_fichier.write("]\n")
		mon_fichier.write("      gateway4: ")
		mon_fichier.write(gateway)
#		mon_fichier.write("\n")
		mon_fichier.write("      nameservers:")
		mon_fichier.write("\n")
		mon_fichier.write("        addresses: [")
		mon_fichier.write(dns[:16])
		mon_fichier.write("]")
		mon_fichier.close()


		process54 = subprocess.Popen(["mv", "netplan.yaml", "/etc/netplan/netplan.yaml"])

		process55 = subprocess.Popen(["netplan", "apply"])

		print("interface configurée")


	if choix_acueil == 0:

		mon_fichierlog.write("Bye\n")
		mon_fichierlog.close()
		quit()
