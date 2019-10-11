# fonctions.py

'''
Python offre des fonctions natives pour réaliser certaines tâches.
Exemples
- print("valeur") pour afficher du texte dans le terminal
- int(valeur) pour convertir la valeur fournie entrée en entier

Le développeur peut créer ses propres fonctions ("personnalisées")
pour réaliser une tâche en fonction d'un certain besoin

Une fonction peut recevoir un ou plusieurs arguments
Les arguments sont des données fournies à la fonction
lors de l'appel
Exemple: square(5), je fournis le chiffre 5 à la fonction square
'''

def main():
    # corps de la fonction: toutes les instructions qu'elle contient
    print('Je suis la fonction principale (main)')
    square(6)
    cube(3)

def square(num):
    print("Je suis la fonction square")
    print(num * num)

# créer une fonction qui affiche le cube du nombre fourni en entrée
def cube(num):
    print("Je suis la fonction cube")
    print(num * num * num)

main()
