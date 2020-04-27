mon_fichierlog = open ("/var/log/logScript.log")


#mon_fichierlog.write("Création d'un nouveau dossier partagé\n")

import subprocess #on import le subprocess pour acceder à l'invite de commande
print("Nom du dossier ?")
nom_dossier = input()
nom_dossier = str(nom_dossier)

print("quel est la localisation de votre dossier, rajouter le nom du dossier à la fin")
path = input()
path = str(path)

process75 = subprocess.call(['mkdir', path ])


process76 = subprocess.call(['chmod', 'a+rwx', path])


mon_fichier = open("/etc/samba/smb.conf","a") #on ouvre le fichier texte

mon_fichier.write("\n\n[")
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


mon_fichier.close()

process77 = subprocess.Popen(["systemctl", "restart", "smbd"])

#mon_fichierlog.write("Nouveau dossié créé \n")
