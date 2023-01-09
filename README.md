Creación del modelo para la web principal

Prueba del modelo mediante adminsite


# en casa
source ~/.local/pyenv/ceu/bin/activate


# eliminar migraciones
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete