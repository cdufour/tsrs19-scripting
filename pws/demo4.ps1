# demo4.ps1
function createUserFolder() {
    param($username) # cette fonction prend 1 paramètre en entrée

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

# tableaux associatifs contenant deux clés (name et password)
$u1 = @{ name = "Chris" ; password = "abc123" }
$u2 = @{ name = "Stiven" ; password = "jkl556" }
$u3 = @{ name = "Julien" ; password = "7_Lm88" }
$u4 = @{ name = "Thierry" ; password = "ccc123" }

$users = @($u1, $u2, $u3, $u4) # tableau de tableaux associatifs

foreach($user in $users) {
    createUserFolder($user.name)
    Write-Output("Folder $user.name created with success")

    # à compléter: ajouter le mot de passe utilisateur au fichier credentials...
}
