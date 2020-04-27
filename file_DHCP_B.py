mon_fichierlog = open("/var/log/logScript.log","a")

mon_fichierlog.write("Configuration d'un serveur dHCP en mode duplication \n")


import os.path
import time

print("choix 1") #on affiche que l'on à choisis le premier choix

if os.path.isfile('dhcp.txt'):
	print("fichier trouvé")

	import subprocess #on import le subprocess pour acceder à l'invite de commande
#			process4 = subprocess.Popen(["rm", "/etc/default/isc-dhcp-server"])

	process20 = subprocess.Popen(["apt", "-", "update"])
	time.sleep(5) #on attend que les paquets se mettent à jours
	process1 = subprocess.Popen(["apt", "-", "install", "isc-dhcp-server"])
	time.sleep(20) # on attend que le logciel soit intallé


	mon_fichierlog.write("lecture du fichier \n")


	with open('dhcp.txt','r') as fich:
		for i in range(1):
			multiple_interface = fich.readline()
			multiple_interface = int(multiple_interface)
#			print(multiple_interface)



	if multiple_interface == 0:
		with open('dhcp.txt','r') as fich:
			for i in range(2):
				interface = fich.readline()
				interface = str(interface)
#				print(interface)
			process41 = subprocess.Popen(["touch", "isc-dhcp-server"])
			f = open("isc-dhcp-server","w")
			f.write('INTERFACESv4"')
			f.write(interface )
			f.write('"')
			f.close()


	if multiple_interface == 1:
		with open('dhcp.txt','r') as fich:
			for i in range(2):
				interface = fich.readline()
				interface = str(interface)
#						print(interface)
		with open('dhcp.txt', 'r') as fich:
			for i in range(3):
				interface2 = fich.readline()
				interface2 = str(interface2)
#						print(interface2)
			process40 = subprocess.Popen(["touch", "isc-dhcp-server"])
			f = open("isc-dhcp-server","w")
			f.write('INTERFACESv4="')
			f.write(interface)
			f.write(", ")
			f.write(interface2)
			f.write('"')
			f.close()
	process43 = subprocess.Popen(["mv", "isc-dhcp-server", "/etc/default/isc-dhcp-server"])


	with open('dhcp.txt','r') as fich:
		for i in range(4):
			plage_ip = fich.readline()
			plage_ip = str(plage_ip)
#					print(plage_ip)

	with open('dhcp.txt','r') as fich:
		for i in range(5):
			reseau_ip = fich.readline()
			reseau_ip = str(reseau_ip)
#					print(reseau_ip)


	with open('dhcp.txt','r') as fich:
		for i in range(6):
			dns = fich.readline()
			dns = str(dns)
#					print(dns)


	with open('dhcp.txt','r') as fich:
		for i in range(7):

			routeur = fich.readline()
			routeur = str(routeur)
#					print(routeur)


	with open('dhcp.txt','r') as fich:
		for i in range(8):
			broadcast = fich.readline()
			broadcast = str(broadcast)
#					print(broadcast)

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
	print("serveur dhcp installé")

	mon_fichierlog.write("Serveur DHCP installé \n")

else:
	print("fichier non trouvé")

	mon_fichierlog.write("le fichier de configuration 'dhcp.txt' pas trouvé dans le dossier du programme \n")



