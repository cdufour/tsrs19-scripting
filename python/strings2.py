# strings2.py

files = ["toto.targa", "test.py", "zz.bismillah", "machin.tiff", "truc.txt", "apache.log"]

# Objectif: afficher les extensions des fichiers listés

# étape1: boucle sur la liste
for f in files:
    # déterminer l'extension, recherche du point "."
    point_index = f.find(".")
    print(f[point_index + 1:])
    