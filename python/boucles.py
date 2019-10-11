# boucles.py

# loops = 5
# while loops > 0:
#     print('Ciao!')
#     loops = loops - 1

loops = 0
while loops < 3:
    loops = loops + 1 # incrémentation d'une unité
    print('Ciao! (passage n° ' + str(loops) + ')')

# boucle initialisant une variable n avec la valeur 10
# condition de bouclage: tant que n inférieur à 20
for n in range(10, 20):
    print('Forza Juve ! ', n)