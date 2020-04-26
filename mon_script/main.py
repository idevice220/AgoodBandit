#fichier principale du programme
#affectation des variables:
import datetime
import subprocess
import os
import os.path
from random import randrange
from math import ceil
import time
i=0 #compteur
y=0
process70 = subprocess.Popen(["touch", "/var/log/logScript.log"])
mon_fichierlog = open("/var/log/logScript.log","a") #on cré le fichier logScript qui contiendra les logs
mon_fichierlog.write('Ouverture du programme  ') #on ecrit la premiere ligne dans le fichier de logs

mon_fichierlog.write('\n') #log


while y == 0:

	print("Voulez vous rentre en mode duplication ? 1 oui 0 non ") #mode duplication
	duplication_enable = input()
	duplication_enable = int(duplication_enable)

	if duplication_enable == 0:
		print("Acueil : faites votre choix") #On affiche l'acueil
		print("1 = DHCP  2 = Netplan  3 = Serveur de fichier 4 = Nouveau dossier partagé 5 = Table de routage 0 = quitter")
		choix_acueil = input()
		choix_acueil = int(choix_acueil)


	if duplication_enable == 1:
		print("Acueil : faites votre choix")
		print("1 = DHCP 2 = NETPLAN 3 = Serveur de fichier")
		choix_acueil = input()
		choix_acueil = int(choix_acueil)

	if duplication_enable == 0 and choix_acueil == 1:

		import file_DHCP_A



	if duplication_enable == 0 and choix_acueil == 2:


		import file_NETPLAN_A


	if duplication_enable == 0 and choix_acueil == 3:

		import file_SERVEUR_FICHIER_A


	if duplication_enable == 0 and choix_acueil == 4:

		import file_NOUVEAU_DOSSIER_SAMBA


	if duplication_enable == 0 and choix_acueil == 5:

		import file_ROUTAGE

#####partie duplication enable = 0 terminé#############
############################################################################


	if duplication_enable == 1 and choix_acueil == 1:

		import file_DHCP_B


	if duplication_enable == 1 and choix_acueil == 2:

		import file_NETPLAN_B


	if duplication_enable == 1 and choix_acueil == 3:

		import file_SERVEUR_FICHIER_B











	if choix_acueil == 0:

		import file_quit
