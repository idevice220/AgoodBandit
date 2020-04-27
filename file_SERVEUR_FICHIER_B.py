import subprocess
import os.path
import time


mon_fichierlog = open("/var/log/logScript.log","a")

mon_fichierlog.write("Configuration d'un serveur de fichier avec le mode duplication \n")


print("configuration Serveur de fichier")
if os.path.isfile('serveur_fichier.txt'):
	print("fichier trouvé")

	mon_fichierlog.write('Fichier de configuration serveur de fichier trouvé \n')

	with open('serveur_fichier.txt','r') as fich:
		for i in range(1):
			choix_serveur_fichier = fich.readline()
			choix_serveur_fichier = str(choix_serveur_fichier)
			choix_serveur_fichier = int(choix_serveur_fichier)

		if choix_serveur_fichier == 1:
			print("SAMBA INSTALLATION")

			mon_fichierlog.write('SAMBA... \n')
			process56 = subprocess.Popen(["apt", "-", "update"])
			time.sleep(5)

			process57 = subprocess.Popen(["apt","-", "install", "samba"])

			time.sleep(10)

			with open('serveur_fichier.txt','r') as fich:
				for i in range(2):
					hosts_allow = fich.readline()
					hosts_allow = str(hosts_allow)

			process56 = subprocess.Popen(["mkdir","/home/share"])
			process59 = subprocess.Popen(["chmod","a+rwx","/home/share"])
			process58 = subprocess.Popen(["touch","smb.conf"])


			mon_fichier = open("smb.conf","w")
			mon_fichier.write('[global]\n')
			mon_fichier.write('server role = standalone server\n')
			mon_fichier.write('usershare allow guests = yes\n')
			mon_fichier.write('hosts allow = ')
			mon_fichier.write(hosts_allow)
			mon_fichier.write('\n')
			mon_fichier.write("[share]")
			mon_fichier.write('\n')
			mon_fichier.write('comment = share\n')
			mon_fichier.write('path = /home/share\n')
			mon_fichier.write('read only = no\n')
			mon_fichier.write('guest ok = yes')

			mon_fichier.close()

			mon_fichierlog.write('Application des paramètres \n')

			process60 = subprocess.Popen(["mv", "smb.conf", "/etc/samba/smb.conf"])
			process61 = subprocess.Popen(["systemctl", "restart", "smbd"])

			print("serveur samba installé")

			mon_fichierlog.write('SAMBA confiuguré \n')


		if choix_serveur_fichier == 2:
			print("serveur NFS installation")

			mon_fichierlog.write('NFS... \n')

			process62 = subprocess.Popen("apt", "-", "install", "nfs-common")
			time.sleep(10)
			process63 = subprocess.Popen("apt", "-", "install", "nfs-server")
			time.sleep(10)

			with open('serveur_fichier.txt','r') as fich:
				for i in range(2):
					addresse_dossier_partage = fich.readline()
					addresse_dossier_partage = str(addresse_dossier_partage)

			with open('serveur_fichier.txt','r') as fich:
				for i in range(3):
					masquedesousreseau = fich.readline()
					masquedesousreseau = str(masquedesousreseau)

			process64 = subprocess.Popen(["mkdir", "/home/ftp"])

			process65 = subprocess.Popen(["touch", "exports"])

			mon_fichier = open("exports","w")

			mon_fichier.write("/home/ftp ")
			mon_fichier.write(addresse_dossier_partage[:12])
			mon_fichier.write('/')
			mon_fichier.write(masquedesousreseau[:2])
			mon_fichier.write(" (ro,sync,root_squash,no_subtree_check,fsid=0)")
			mon_fichier.close()

			mon_fichierlog.write('Application des paramètres NFS \n')


			process66 = subprocess.Popen(["mv", "exports", "/etc/exports"])

			process67 = subprocess.Popen(["/etc/init.d/nfs-kernel-server", "restart"])

			print("serveur de fichier installé")

			mon_fichierlog.write('Serveur de fichier configuré \n')



else:
	print('fichier non trouvé')

	mon_fichierlog.write('Fichier de configuration "serveur-fichier.txt" non trouvé dans le dossier du programme \n')


