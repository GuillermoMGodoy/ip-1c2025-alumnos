# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados: uno de las imágenes de la API y otro de favoritos, ambos en formato Card, y los dibuja en el template 'home.html'.
def home(request):
    images = services.getAllImages()
    favourite_list = []

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })

# función utilizada en el buscador.
def search(request):
    name = request.POST.get('query', '')

    # si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
    if (name != ''):
        images = services.filterByCharacter(name) # Llamamos a la función del services.py que filtra los Pokémon por nombre.
        favourite_list = []

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# función utilizada para filtrar por el tipo del Pokemon
# Una vez modificado el services.py que es la base para que esta funcion pueda cumplir su funcion se modifica la funcion en views.py que es
# la encargada de mostrarlo en pantalla y funcione correctamente.
def filter_by_type(request):
    pokemon_type = request.POST.get('type', '')

    if pokemon_type != '': # Verifica que se haya enviado un tipo (que no esté vacío)
        images = services.filterByType(pokemon_type) # Llamamos a la función del services.py que filtra los Pokémon por tipo
        favourite_list = []
    #Esta parte ya estaba en el codigo pero si mal no entiendo por lo leeido en django es la encargada de renderizar el template de home.html
        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    pass

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    logout(request)
    return redirect('home')
