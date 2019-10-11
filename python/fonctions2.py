# fonctions2.py
'''
Une fonction peut également retourner une valeur grâce au mot-clé return
Dans l'exemple ci-dessous square() n'affiche plus le carré de 
la valeur saisie, elle le RETOURNE
Ce retour peut ensuite être:
- utilisé en entrée d'une autre fonction
- affecté à une variable
'''

def square(num):
    # print(num * num)
    return num * num

print(square(4))

sq = square(int(input('Saisir un nombre: ')))
print(sq)

