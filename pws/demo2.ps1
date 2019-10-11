# demo2.ps1

function createUserFolder() {
    # création du dossier utilisateur
    New-Item -Path "./$username" -ItemType Directory

    # création des fichiers dans le dossier utilisateur
    New-Item -Path "./$username/credentials.txt" -ItemType File
    New-Item -Path "./$username/user_profile.txt" -ItemType File
    New-Item -Path "./$username/user_activity.log" -ItemType File

    # écriture dans le fichier credentials.txt
    $credentials = "username:$username`npassword:$password"
    Set-Content -Path "./$username/credentials.txt" -Value $credentials
}

$username = Read-Host -Prompt "Nom d'utilisateur"
$password = Read-Host -Prompt "Mot de passe"

# interdire un mdp de longueur inférieure à 4 ou supérieure à 8
if ($password.Length -lt 4 -or $password.Length -gt 8) {
    Write-Output("Le mot de passe doit contenir entre 4 et 8 caractères")
} else {
    # Pas de parenthèses après le nom de la fonction (lors de son appel)
    # si celle-ci ne prend aucun paramètre en entrée
    createUserFolder
}