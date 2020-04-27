import time

mon_fichierlog = open("/var/log/logScript.log","a")

mon_fichierlog.write("configuration de la table de routage \n")

import subprocess


print("Nom de l'interface à router ?")
int_rout = input()
int_rout = str(int_rout)


process81 = subprocess.call(["sysctl", "-w","net.ipv4.ip_forward=1"])


print("Application de la table de routage")

process78 = subprocess.call(['iptables',  '-t', 'nat', '-A', 'POSTROUTING', '-o', int_rout, '-j', 'MASQUERADE'])
process79 = subprocess.call(["ufw", "reload"])
time.sleep(1)
process80 = subprocess.call(["ufw", "enable"])


print("Table de routage modifié")
mon_fichierlog.write("Table de routage modifié \n")
