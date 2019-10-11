# dictionary.py

dico = {}
print(type(dico))

player1 = { 'lastname':'Bonucci', 'firstname':'Leonardo', 'team':'Milan AC' }
player2 = { 'lastname':'Verrati', 'firstname':'Marco', 'team':'PSG' }

# accès à une clé en lecture
print(player1['firstname'])

# accès à une clé en écriture (modification)
player2['lastname'] = 'Verratti'

# ajout d'une clé/valeur
player2['smoker'] = True
player2['num'] = 6

# affichage de toutes les valeurs situées dans le dictionnaire player2
for v in player2.values():
    print(v)

# affichage de toutes les clés situées dans le dictionnaire player2
for k in player2.keys():
    print(k)

# items renvoie un tuple de 2 éléments: la clé et la valeur associée
for k, v in player2.items(): 
    print(k, '===========>', v)

# test sur une valeur (savoir une valeur existe)
if 'Juventus' in player1.values():
    print(player1['lastname'], 'joue pour Juventus')
else:
    print(player1['lastname'], 'ne joue pas pour Juventus')