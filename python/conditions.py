# conditions.py
note = float(input('Saisir la note (sur 20): '))

# if note == 20:
#     print('Parfait !')

if note >= 10:
    print('Admis !')
    if note == 20:
        print('avec mention "Parfait"')
else:
    if note >= 8:
        print('Admis au rattrapage')
    else:
        print('Recalé')
        