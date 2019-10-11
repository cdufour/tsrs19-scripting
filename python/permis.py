# permis.py
'''
Créer un script demandant à l'utilisateur de saisir son âge
Si l'utilisateur a 18 ans ou plus, on affiche 'autorisé'
Si l'utilisateur a 16 ou 17 ans, on affiche 'conduite accompagné possible'
Si l'utilisateur a moins de 16 ans, on affiche 'non autorisé'
'''

age = int(input('Ton âge: '))

if age >= 18:
    print('autorisé')
else:
    if age >= 16:
        print('conduit acc possible')
    else:
        print('non autorisé')
