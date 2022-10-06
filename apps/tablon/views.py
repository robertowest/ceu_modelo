import json, os

from django.shortcuts import render

# Create your views here.
def index(request):
    # leemos el contenido del json y lo convertimos en diccionario
    with open('{}/config.json'.format(os.path.dirname(__file__))) as json_file:
        data = json.load(json_file)
    return render(request, 'tablon/index.html', context={'config' : data})


def tablon(request, slug):
    # unique_slug = get_object_or_404(Tablon, slug=slug)
    unique_slug = 'esto_es_un_slug'
    return render(request, "tablon/tablon.html", {"titulacion": slug})
