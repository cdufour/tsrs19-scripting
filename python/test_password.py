# test_password.py

# déclaration et initialisation des variables
correctPass = "abc123"
userPass = ''
numAttempts = 0 # nombre de tentatives
loginSuccess = True

while not userPass == correctPass:
    numAttempts += 1 # incrémentation
    if numAttempts > 3: # 3 tentatives effectuées
        loginSuccess = False
        numAttempts -= 1
        break # sortie de boucle immédiate
    userPass = input("Votre mot de passe: ")

if loginSuccess == True:
    print('*** LOGIN REUSSI après', numAttempts, 'tentatives ***')
else:
    print('*** LOGIN ECHEC après', numAttempts, 'tentatives ***')