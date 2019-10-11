# zip.py
from zipfile import ZipFile

# ouverture du fichier du zip en mode écriture
zip = ZipFile('./files/test.zip', 'w')

# ajout de deux fichiers dans l'archive
zip.write('./files/aigle.gif')
zip.write('./files/jaguar.png')

# fermeture du fichier zip
zip.close()
