# conditions.ps1

$feuVert = $true

if($feuVert) {
    echo("J'avance")
} else {
    echo("Je m'arrête")
}

$feu = "orange"
if ($feu -eq "vert") {
    echo("J'avance")
} elseif ($feu -eq "orange") {
    echo("Je ralentis")
} else {
    echo("Je stoppe")
}