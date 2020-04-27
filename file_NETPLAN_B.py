mon_fichierlog = open("/var/log/logScript.log","a")
mon_fichierlog.write('Configuration NETPLAN avec mode duplication activé \n')

print("choix 2")

import os.path
if os.path.isfile('netplan.txt'):
	print("fichier trouvé")
	import subprocess

	mon_fichierlog.write('Fichié de configuration trouvé \n')

	process52 = subprocess.Popen(["rm", "/etc/netplan/netplan.yaml"])

#               process53 = subprocess.Popen(["apt", "-", "update"])
#               process54 = subprocess.Popen(["apt", "-", "intall", ""])

	with open('netplan.txt','r') as fich:
		for i in range(1):
			interface = fich.readline()
			interface = str(interface)
#                               print(interface[:5])
	with open('netplan.txt','r') as fich:
		for i in range(2):
			dhcp_enable = fich.readline()
			dhcp_enable = str(dhcp_enable)
#                               print(dhcp_enable)
	with open('netplan.txt','r') as fich:
		for i in range(3):
			submask = fich.readline()
			submask = str(submask)
#                               print(submask)
		with open('netplan.txt','r') as fich:
			for i in range(4):
				addresse_ip = fich.readline()
				addresse_ip = str(addresse_ip)
#                               print(addresse_ip)
		with open('netplan.txt','r') as fich:
			for i in range(5):
				gateway = fich.readline()
				gateway = str(gateway)
#                               print(gateway)
		with open('netplan.txt','r') as fich:
			for i in range(6):
				dns = fich.readline()
				dns = str(dns)
#                               print(dns)
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
#               mon_fichier.write("\n")
	mon_fichier.write("      nameservers:")
	mon_fichier.write("\n")
	mon_fichier.write("        addresses: [")
	mon_fichier.write(dns[:16])
	mon_fichier.write("]")
	mon_fichier.close()

	mon_fichierlog.write('Application des parametres NETPLAN \n')

	process54 = subprocess.Popen(["mv", "netplan.yaml", "/etc/netplan/netplan.yaml"])

	process55 = subprocess.Popen(["netplan", "apply"])

	print("interface configurée")

	mon_fichierlog.write('NETPLAN configuré \n')









else:
	print("fichier non trouvé")
	mon_fichierlog.write('Pas de fichiers de configuration "dhcp.txt" dans le dossier du programme\n')

