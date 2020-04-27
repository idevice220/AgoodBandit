import time

mon_fichierlog = open("/var/log/logScript.log","a")

mon_fichierlog.write("Installation d'un serveur de fichier \n")

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

	mon_fichierlog.write("configuration de SAMBA \n")


	import subprocess #on importe le subprocess pour acceder à l'invite de commande

	process10 = subprocess.Popen(["apt","-","install","samba"])
	time.sleep(10)


	print("réseau autorisé ? ex:192.168.0.0/16")
	hosts_allow = input()
	hosts_allow = str(hosts_allow)



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


	mon_fichier.close()

	mon_fichierlog.write("Application des parametres \n")

	process14 = subprocess.Popen(["mv", "smb.conf", "/etc/samba/smb.conf"]) #on bouge le fichier pour le mettre dans le repertoire adequat
	process15 = subprocess.Popen(["systemctl", "restart", "smbd"]) #on applique les changements

	mon_fichierlog.write("Serveur SAMBA installé \n")

	print("Serveur de fichier installé (Samba)")



##############"NFS"#################################


if choix_serveur_fichier == 2:

	mon_fichierlog.write("Configuration NFS \n")

	import subprocess #on import le subprocess pour acceder à l'invite de commande

	process90 = subprocess.Popen(["apt", "-", "install", "nfs-common"]) #process est d'installer les outils NFS
	time.sleep(2)

	process91 = subprocess.Popen(["apt", "-", "install", "nfs-server"]) #process est d'installer le serveur NFS
	time.sleep(2)


	print("addresse réseau du dossier partagé")
	addresse_dossier_partage = input()

	addresse_dossier_partage = str(addresse_dossier_partage)
	print("masque de sous réseau (ex: 24 = /24)")
	masquedesousreseau = input()
	masquedesousreseau = str(masquedesousreseau)

	process16 = subprocess.Popen(["mkdir", "/home/ftp"])

	process17 = subprocess.Popen(["touch", "exports"]) #

	mon_fichier = open("exports","w")

	mon_fichier.write('/home/ftp ')
	mon_fichier.write(addresse_dossier_partage)
	mon_fichier.write('/')
	mon_fichier.write(masquedesousreseau)
	mon_fichier.write("(ro,sync,root_squash,no_subtree_check,fsid=0)")

	mon_fichier.close()


	mon_fichierlog.write("Application des parametres \n")

	process18 = subprocess.Popen(["mv", "exports", "/etc/exports"]) #

	process92 = subprocess.Popen(["/etc/init.d/nfs-kernel-server", "restart"]) #On redemarre NFS


	mon_fichierlog.write("Serveur NFS installé \n")

	print("Serveur de fichier installé (NFS)")

	time.sleep(2)
