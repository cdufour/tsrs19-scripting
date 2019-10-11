# max.py

notes = [14, 3, 16, 10]

'''
Créer un script/fonction qui trouve et affiche la note la plus élevée
'''

note_max = notes[1] # par défaut on considère la première valeur du tableau comme note max

for note in notes:
    if note > note_max:
        note_max = note

print("La note la plus élévée est", note_max)
