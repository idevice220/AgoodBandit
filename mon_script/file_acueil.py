

print("Voulez vous rentre en mode duplication ? 1 oui 0 non ") #mode duplication
#print("hello world")
duplication_enable = input()
duplication_enable = int(duplication_enable)


#acueil du programme
if duplication_enable == 0:

	print("Acueil : faites votre choix") #On affiche l'acueil
	print("1 = DHCP  2 = Netplan  3 = Serveur de fichier 4 = Nouveau dossier partagé 5 = Table de routage 0 = quitter")

	choix_acueil = input()
	choix_acueil = int(choix_acueil)

if duplication_enable ==1:

	print("Acueil : faites votre choix")
	print("1 = DHCP 2 = NETPLAN 3 = Serveur de fichier")

	choix_acueil = input()
	choix_acueil = int(choix_acueil)
#        mon_fichierlog.write("Saisit de l'utilisateur\n") #log
