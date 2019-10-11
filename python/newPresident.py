#  newPresident.py
'''
Script remplaçant dans un ensemble de fichier le nom d'un Président
par autre
'''
import os

source_dir = "./files"
oldPresident = "Stiven TOTIC"
newPresident = "Macron"

files = os.listdir(source_dir) # récupération de liste des fichiers

# Parcours et ouverture des fichiers de cette liste
for f in files:
    if f[-3:] == "txt": # s'il s'agit d'un fichier texte
        fd = open(source_dir + '/' + f, 'r') # ouverture du fichier

        # le contenu du ficher et lu et copié dans la variable content
        content = fd.read()

        # si le nom de l'ancien président a été trouvé (find a renvoyé autre chose que -1)
        if not content.find(oldPresident) == -1:
            # remplacement des noms
            newContent = content.replace(oldPresident, newPresident)

            fd.close() # fermeture du descripteur de fichier

            # mise à jour du fichier (writable) avec le nouveau contenu
            fd = open(source_dir + '/' + f, 'w')
            fd.write(newContent)
            fd.close()

            print(f, "modifié")


