# https://blog.netwrix.fr/2018/12/05/gestion-des-fichiers-avec-powershell/#Supprimer%20des%20fichiers%20et%20des%20dossiers

Get-Item -Path "./"
New-Item -Path "./truc" -ItemType Directory

$max = 3
for($i=0; $i -lt $max; $i++) {
    $n = $i + 1
    New-Item -Path "./truc$n.txt" -ItemType File
}

Start-Process notepad