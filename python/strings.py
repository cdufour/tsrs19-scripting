# strings.py

message = "Pizdele frumoase"
files = ["blabla.png", "fdp.gif", "cazzo.png", "curva.jpg", "troia.log", "pecora.py", "test.png"]

print(len(message)) # affiche la longueur de la chaîne

# boucle sur les carctères de la chaîne
# for c in message:
    # print(c) 

sli = message[0:5] + '...' # => Pizde
sli2 = message[2:5] # => zde
sli3 = message[2:] # => zdele frumoase

# slicing avec indice négatif pour partir de la droite de la chaîne
sli4 = message[0:-3] # => Pizdele frumo
print(sli4)

for f in files:
    # affiche le nom du fichier
    # print(f[0:-4])
    print(f[-3:]) # affiche l'extension du fichier (3 derniers caractères)

test = "fru" in message # => True

num_png = 0

for f in files:
    if ".png" in f:
        num_png += 1

print(num_png, "fichers trouvés au format png")

message_modif = message.replace("e", "i") # replace retourne une copie modifiée de message
print(message_modif) # => Pizdili frumoasi

