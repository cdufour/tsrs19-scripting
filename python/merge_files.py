# merge_files.py

'''
Objectif: fusionner en un seul fichier "apache.log"
l'ensemble des fichier logs apache
On demande à l'utilisateur ce qu'il souhaite faire des fichiers de log
1: rien ; 2: archivage (zip) ; 3: suppression
'''

import os
from zipfile import ZipFile

source_dir = './files/logs'
logs = ''
files = os.listdir(source_dir)
choice = int(input('Que faire des fichiers .log ? 1: rien, 2: archivage, 3: suppression '))

# choix de l'archivage: ouvertur d'un fichier zip
# en attente de contenu (de fichiers)
if choice == 2:
    zip = ZipFile('./files/logs/apache.log.zip', 'w')

# itération sur les fichiers de log
for f in files:
    fd = open(source_dir + '/' + f, 'r')
    logs += '\n' + fd.read()
    fd.close()

    # prise en compte du choix de l'utilisateur
    if choice == 3:
        os.remove(source_dir + '/' + f) # suppression du fichier
    elif choice == 2:
        zip.write(source_dir + '/' + f) # archivage du fichier

# on ferme le fichier zip dans le cas où l'archivage a été choisi
if choice == 2:
    zip.close()

# enregistrement sur disque de la variable logs
fd = open(source_dir + '/apache.log', 'w')
fd.write(logs)
fd.close()
