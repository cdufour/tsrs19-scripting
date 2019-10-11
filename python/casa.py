# casa.py
'''
Ecrire et tester une fonction qui retournera la surface d'une pièce
dont on connaît la largeur et la longueur (ces deux infos
seront en fournis en entrée de la fonction)
'''

def surface(largeur, longueur):
    return largeur * longueur

largeur = float(input('Largeur de la pièce (en mètre): '))
longueur = float(input('Longueur de la pièce (en mètre): '))
superficie = surface(largeur, longueur)
print("Superficie de la pièce:", superficie, "m2")