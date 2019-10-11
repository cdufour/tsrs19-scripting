# calculs.py

note1 = 15
note2 = 12
print(note1 + note2)

group = "TSRS 19"
print(group + "note2") # concaténation: réunir de chaînes de caractères

# 3 valeurs saisies directement converties en int
n1 = int(input('Saisir note 1: '))
n2 = int(input('Saisir note 2: '))
n3 = int(input('Saisir note 3: '))

moyenne = (n1 + n2 + n3) / 3
print('Moyenne des 3 notes: ' + str(moyenne)) # str() convertit en chaine la valeur reçue en entrée