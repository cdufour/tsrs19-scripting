# tva.py
'''
Créer un script demandant à l'utilisateur 
1/ de saisir un montant HT
2/ un taux TVA (exemple: 20%)

Le script affichera le montant TTC correspondant

exemple
HT: 100
TVA: 20
=> 120
'''
ht = float(input('Montant HT: '))
tva = float(input('Taux TVA (%): '))
montant_tva = ht * (tva/100)
montant_ttc = ht + montant_tva
print('Montant TTC: ' + str(round(montant_ttc, 2)) + ' €')