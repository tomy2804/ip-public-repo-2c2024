from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout
from app.layers.services.services import getAllImages, getAllFavourites


def index_page(request):
    return render(request, 'index.html')

def home(request):
    page = request.GET.get('page', 1)
    name = request.GET.get('name', None)
    images = getAllImages(page, name)
    favourite_list = getAllFavourites(request) if request.user.is_authenticated else []

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list, 'page': int(page), 'name': name })

def search(request):
    search_msg = request.POST.get('query', '')

    if search_msg:
        images = getAllImages(name=search_msg)
        favourite_list = getAllFavourites(request) if request.user.is_authenticated else []
        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list, 'page': 1, 'name': search_msg })
    else:
        return redirect('home')

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