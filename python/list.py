# list.py
players = ["Dybala", "Matuidi", "Pjanic", "Buffon"]
print(type(players)) # => list

# modification d'un élément
players[1] = "Charo"

# lecture d'un élément par rapport à son indice (ordre dans la liste)
print(players[1])

# ajout d'un élément
players.append("Ronaldo")

# suppression d'un élément
del players[3]

# bouche sur la liste pour afficher le nom du joueur itéré
for player in players:
    print(player)