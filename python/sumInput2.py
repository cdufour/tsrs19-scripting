# sumInput2

sum = 0 # variable servant à faire le cumul des valeurs saisies
inputValues = [] # liste vide

while sum < 100: # on boucle tant que la somme cumulée est inférieure à 100
    num = int(input("Saisir un entier: "))
    inputValues.append(num) # insertion de la valeur saisie dans la liste
    sum += num # accumulation (on ajoute la nouvelle valeur à l'ancienne)

print('Somme des valeurs saisies', sum)
print('Vous avez saisi les valeurs suivantes: ')

# Affichage des valeurs saisies
for val in inputValues:
    print(val)



