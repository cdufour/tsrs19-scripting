# demo.py

str1 = "48"
str2 = "55"
print(str1 + str2) # => 4855

'''
la fonction int() convertit en entier 
(quand c'est possible) la valeur qui lui est fournie en entrée
'''
print(int(str1) + int(str2)) # => 103

int(48.32) # valide => 48
int("blabla") # invalide, valeur non convertible en entier