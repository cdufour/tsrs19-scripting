# images.py
import os # on importe le module (bibliothèques de fonctions) os

# files = ["a.png", "b.txt", "c.jpg", "d.jpg", "e.gif", "f.exe"]
files = os.listdir('./files')

'''
Créer un script affichant le nombre d'images trouvées dans la liste
de fichiers ci-dessus.
Est considéré comme image un fichier png, jpg ou gif
'''

num_images = 0 # nombre d'images trouvées, initialisé à 0

# la fonction isImage prend un en entrée un nom de fichier
# et renvoie True si ce nom contient une extension de type image
# sinon elle renvoie False
def isImage(filename):
    extension = filename[-3:]
    image_extensions = ["jpg", "png", "gif"]
    return extension in image_extensions

# Parcours de la liste, lorsqu'une image est trouvée
# on incrémente la variable num_images
for f in files:
    if isImage(f):
        num_images += 1

print(num_images, "images trouvées dans le dossier ./files")


