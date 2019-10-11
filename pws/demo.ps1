# demo.ps1

<#
Script demandant de saisir :
- un nom d'utilisateur
- un mot de passe
Le script génèrera un dossier portant ce nom
ainsi que les 3 fichiers suivants:
- credentials.txt
    username: username
    password: password
- user_profile.txt
- user_activity.log
#>

$username = Read-Host -Prompt "Nom d'utilisateur"
$password = Read-Host -Prompt "Mot de passe"

# création du dossier utilisateur
New-Item -Path "./$username" -ItemType Directory

# création des fichiers dans le dossier utilisateur
New-Item -Path "./$username/credentials.txt" -ItemType File
New-Item -Path "./$username/user_profile.txt" -ItemType File
New-Item -Path "./$username/user_activity.log" -ItemType File

# écriture dans le fichier credentials.txt
$credentials = "username:$username`npassword:$password"
Set-Content -Path "./$username/credentials.txt" -Value $credentials
