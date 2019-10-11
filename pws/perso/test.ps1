[string]$nom = "DUFOUR"
$prenom = "Chris"

$nom + ' ' + $prenom

$test = $true

if ($test) {
    #echo 'Vrai'
    Write-Output("Vrai")
}

$notes = @(14,3,16,10)
$notes[1]

function somme($notes) {
    $cumul_notes = 0
    foreach($note in $notes) {
        $cumul_notes += $note
    }
    return $cumul_notes
}

foreach($note in $notes) {
    Write-Output($note)
}

$moy = somme($notes)
$moy / 4
