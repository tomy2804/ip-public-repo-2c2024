# capa de vista/presentación
##comment
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from app.layers.services.services import getAllImages, getAllFavourites

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    page=request.GET.get('page', 1)
    name=request.GET.get('name', None)
    images= getAllImages(page, name)
    favourite_list=getAllFavourites(request) if request.user.is_authenticated else []

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list, 'page': int(page), 'name': name })

def search(request):
    search_msg = request.POST.get('query', '')

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
    # y luego renderiza el template (similar a home).
    if search_msg:
        images = getAllImages(name=search_msg)
        favourite_list = getAllFavourites(request) if request.user.is_authenticated else []
        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list, 'page': 1, 'name': search_msg })
    else:
        return redirect('home')

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = getAllFavourites(request)
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
     # Implementación de guardar favoritos
    pass

@login_required
def deleteFavourite(request):
      # Implementación de eliminar favoritos
    pass

@login_required
def exit(request):
    pass