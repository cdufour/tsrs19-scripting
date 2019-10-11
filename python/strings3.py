# strings3.py

phones = [
    "+33611 2233 44", 
    "+39611223355", 
    "+3961 1223366", 
    "+33611223377",
    "+3361122 3388",
    "+40611223399",
    "+381 61122 33 22",
    "+4061122 3333",
    "+40611223300",
]

str = "Je sais programmer en Python"
str = "+33-07-88-33-22-50"
# x = str.upper() # => JE SAIS PROGRAMMER EN PYTHON
# x = str.split('-')
# print(x[4], x[5])

x = str.startswith('+33')
print(x)

# Objectif: à partir de la liste des numéros de téléphone
# produire deux fichiers: l'un contenant les numéros fr
# l'autre contenant les numéro it

# créer deux sous-liste
phones_fr = []
phones_it = []
phones_ro = []
phones_sr = []

# parcourir la liste des numéros de tel
for phone in phones:
    if phone.startswith('+33'):
        # insertion du numéro dans la sous-liste avec suppression 
        # des espaces inutiles (espace remplacé par vide)
        phones_fr.append(phone.replace(' ', ''))

    elif phone.startswith('+39'):
        phones_it.append(phone.replace(' ', ''))

    elif phone.startswith('+40'):
        phones_ro.append(phone.replace(' ', ''))

    elif phone.startswith('+381'):
        phones_sr.append(phone.replace(' ', ''))

# ouverture des fichiers
# numéros FR
fd = open('./files/phones_fr.txt', 'w')
for phone in phones_fr:
   fd.write(phone + '\n')
fd.close()

# numéros IT
fd = open('./files/phones_it.txt', 'w')
for phone in phones_it:
   fd.write(phone + '\n')
fd.close()


# Exo: ajouter des numéros roumains et serbes dans la liste des 
# numéros et produire les fichiers correspondants

# numéros RO
fd = open('./files/phones_ro.txt', 'w')
for phone in phones_ro:
   fd.write(phone + '\n')
fd.close()

# numéros SR
fd = open('./files/phones_sr.txt', 'w')
for phone in phones_sr:
   fd.write(phone + '\n')
fd.close()
