print("Voulez vous rentre en mode duplication ? 1 oui 0 non ") #mode duplication
duplication_enable = input()
duplication_enable = int(duplication_enable)

if duplication_enable == 1:
	print("mode duplication activé")
#	if os.path.isfile('duplication.txt'):
#		print("fichier trouvé")
#		liste = open("duplication.txt", "r").read()


#	else:
#		print("fichier non trouvé")
#		print("mode duplication non activé")
#		duplication_enable = 0




elif duplication_enable == 0:
	print("mode duplication pas activé")
else:
	print("répondez par 1 ou 0")