# demo3.ps1
function createUserFolder() {
    param($username) # cette fonction prend un paramètre en entrée
    # création du dossier utilisateur
    New-Item -Path "./$username" -ItemType Directory

    # création des fichiers dans le dossier utilisateur
    New-Item -Path "./$username/credentials.txt" -ItemType File
    New-Item -Path "./$username/user_profile.txt" -ItemType File
    New-Item -Path "./$username/user_activity.log" -ItemType File

    # écriture dans le fichier credentials.txt
    $credentials = "username:$username`npassword:yyy"
    Set-Content -Path "./$username/credentials.txt" -Value $credentials
}

$users = @("Chris", "Stiven", "Julien", "Thierry") # tableau de chaînes de caractères

foreach($user in $users) {
    createUserFolder($user) # création du dossier utilisateur
}
