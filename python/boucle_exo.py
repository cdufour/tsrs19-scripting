# boucle_exo.py

'''
Créer un script qui demande à l'utilisateur de saisir:
1/ un message à afficher
2/ le nombre de fois où le message saisi devra être affiché

Si l'utilisateur a saisi un nombre de fois supérieur à 1000,
on affichera un message lui indiquant qu'il ne peut pas dépasser cette limite
Sinon, affichera le message autant que de fois qu'indiqué par l'utilisateur

exemple:
Message: "Adoro i pompini"
Nombre de fois: 3
Adoro i pompini
Adoro i pompini
Adoro i pompini

'''

LIMIT = 30 # constante (nom de la variable en MAJUSCULE)

message = input('Quel message souhaitez-vous afficher ? ')
nb_fois = int(input('Combien de fois ? '))

if nb_fois > LIMIT:
    print('Limite dépassée (' + str(LIMIT) + ' fois max)')
else:
    for n in range(nb_fois):
        print(message)





