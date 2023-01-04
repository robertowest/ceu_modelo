#!/bin/bash
git add .

git reset -- config/__init__.py
git reset -- config/settings.py

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
