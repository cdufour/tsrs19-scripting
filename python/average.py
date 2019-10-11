# average.py

notes = [14, 3, 16, 10, 2]

'''
Créer un script/fonction qui calcule et affiche la moyenne des notes
'''

def somme(notes):
    somme_notes = 0
    for note in notes:
        somme_notes += note
    return somme_notes

print("La moyenne est de", somme(notes) / len(notes))