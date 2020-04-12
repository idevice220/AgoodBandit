#acueil du programme

import os
from random import randrange
from math import ceil
import time


print("1 = DHCP  2 = Netplan  3 = Serveur de fichier")

choix_acueil = input()
choix_acueil = int(choix_acueil)



## Si l'on choisit l'option 1
#######################################affectation de l'interface DHCP à configurer#############################################################


if choix_acueil == 1:
        print("choix 1") #on affiche que l'on à choisis le premier choix

        import subprocess #on import le subprocess pour acceder à l'invite de commande

        process4 = subprocess.Popen(["rm", "/etc/default/isc-dhcp-server"])

        process20 = subprocess.Popen(["apt", "-", "update"])
#        time.sleep(30) #on attend que les paquets se mettent à jours
        process1 = subprocess.Popen(["apt", "-", "install", "isc-dhcp-server"]) #premier process est d'installer le serveur DHCP
#        time.sleep(25) # on attend que le logciel soit installé

        print("plusieurs interfaces à activer 1 = oui 0 = non")
        multiple_interface = input()
        multiple_interface = int(multiple_interface)



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


        process2 = subprocess.Popen(["touch", "isc-dhcp-server"]) #on cré un fichier iscp-dhcp-server
        mon_fichier = open("isc-dhcp-server","w") #on ouvre le fichier iscp-dhcp-server




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
        mon_fichier = open("dhcpd.conf","w") #on ouvre le fichier dhcpd.conf

##On remplit le fichier de configuration##
        mon_fichier.write('option domain-name "example.org";\n')
        mon_fichier.write('option domain-name-servers ns1.example.org, ns2.example.org;\n')
        mon_fichier.write('default-lease-time 600;\n')
        mon_fichier.write('max-lease-time 7200;\n')
        mon_fichier.write('ddns-update-style none;\n')
        mon_fichier.write('authoritative;\n')
        mon_fichier.write('subnet ')
        mon_fichier.write(reseau_ip)
        mon_fichier.write(" netmask 255.255.255.0 {\n")
        mon_fichier.write(' range ')
        mon_fichier.write(plage_ip)
        mon_fichier.write(";\n")
        mon_fichier.write(" option domain-name-servers ")
        mon_fichier.write(dns)
        mon_fichier.write(";\n")
        mon_fichier.write(" option subnet-mask 255.255.255.0")
        mon_fichier.write(";\n")
        mon_fichier.write(" option routers ")
        mon_fichier.write(routeur)
        mon_fichier.write(";\n")
        mon_fichier.write(" option broadcast-address ")
        mon_fichier.write(broadcast)
        mon_fichier.write(";\n")
        mon_fichier.write(" default-lease-time 600;\n")
        mon_fichier.write(" max-lease-time 7200;\n")
        mon_fichier.write("}")
        process5 = subprocess.Popen(["mv", "dhcpd.conf", "/etc/dhcp/dhcpd.conf"]) #on bouge le fichier pour le mettre dans le repertoire adequat
        process6 = subprocess.Popen(["systemctl", "restart", "isc-dhcp-server"]) #on redemarre dhcp pour qu'il prenne les paramètres

        print("Serveur DHCP installé")

##fin de l'installation du serveur DHCP###############
## configuration pour Netplan


if choix_acueil == 2:
        print("choix 2") #on affiche que l'on à choisis le deuxieme choix

        import subprocess #on import le subprocess pour acceder à l'invite de commande

        print("nom de l'interface") #on demande le nom de l'interface à configurer
        interface = input() #on récupere la donnée
        interface = str(interface) #on convertie la valeur en chaine de caracteres

        print("dhcp yes or no ?")
        dhcp_enable = input()
        dhcp_enable = str(dhcp_enable)

        print("submask")
        submask = input()
        submask = str(submask)

        print("addresse ip du serveur")
        addresse_ip = input()
        addresse_ip = str(addresse_ip)

        print("gateway")
        gateway = input()
        gateway = str(gateway)

        print("DNS")
        dns = input()
        dns = str(dns)


        process8 = subprocess.Popen(["touch", "test.yaml"]) #on cré un fichier .yaml
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


        process9 = subprocess.Popen(["mv", "test.yaml", "/etc/netplan/netplan.yaml"]) #on bouge le fichier pour le mettre dans le repertoire adequat
        process10 = subprocess.Popen(["netplan", "apply"]) #on applique les changements

        print("interface reseau configuré")

###########Configuration Serveur de fichiers#####################


###########"SAMBA"#######################

if choix_acueil == 3:

        print("choix 3") #on affiche le menu dans lequel on va rentrer

        print ("1 = Samba  2 = NFS")

        choix_serveur_fichier = input()
        choix_serveur_fichier = int(choix_serveur_fichier)

        if choix_serveur_fichier == 1:

               import subprocess #on importe le subprocess pour acceder à l'invite de commande
               process21 = subprocess.Popen(["apt", "-", "update"])
#               time.sleep(30)

               process10 = subprocess.Popen(["apt","-","install","samba"])

               time.sleep(15) #on attend que le programme se télécharge

               print("réseau autorisé ? ex:192.168.0.0/16")
               hosts_allow = input()
               hosts_allow = str(hosts_allow)

               print("nom d'utilisateur")
               user = input()
               user = str(user)

#        print("nom du partage")
#        partage = input()
#        partage = str(partage)

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

               process18 = subprocess.Popen(["mv", "exports", "/etc/exports"]) #

               process92 = subprocess.Popen(["/etc/init.d/nfs-kernel-server", "restart"]) #On redemarre NFS


               print("Serveur de fichier installé (NFS)")
