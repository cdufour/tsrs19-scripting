# cleaner.ps1
$users = @("Chris", "Stiven", "Julien", "Thierry") # tableau de chaînes de caractères
foreach($user in $users) {
    # suppression récursive (supprime les enfants également) 
    # du dossier utilisateur sans demande de confirmation
    Remove-Item -Path "./$user" -Confirm:$false -Force -Recurse
    Write-Output("Dossier $user supprimé")
}
