# filesystem.py
students = ["Julien", "Stiven", "Yannis", "Arnaud"]

# f = open('files/students.txt', 'a') # mode d'ouverture "append", on ajoute

# for student in students:
#     f.write(student + '\n')

# f.close() # fermeture de descripteur de fichier

for student in students:
    f = open('files/' + student + '.txt', 'w')
    f.write('blabla')
    f.close()