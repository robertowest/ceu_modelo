#!/bin/bash
git add .
git commit -m "modificado por Roberto"
git branch -M main
echo "¿Quiere subir los cambios?"
select sn in "Sí" "No"; do
    case $sn in
        Sí ) git push -u origin main; break;;
        No ) exit;;
    esac
done



# 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

