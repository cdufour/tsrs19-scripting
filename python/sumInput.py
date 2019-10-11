# sumInput
'''
Créer un script demandant à l'utilisateur de saisir
un chiffre tant que la somme des chiffres précédemment saisis
est inférieur à 100

exemple:
10
60
10
30 => 10 + 60 + 10 + 30 = 110 > 100 => sortie de boucle
'''
sum = 0 # variable servant à faire le cumul des valeurs saisies

while sum < 100: # on boucle tant que la somme cumulée est inférieure à 100
    num = int(input("Saisir un entier: "))
    sum += num # accumulation (on ajoute la nouvelle valeur à l'ancienne)

print('Somme des valeurs saisies', sum) 


