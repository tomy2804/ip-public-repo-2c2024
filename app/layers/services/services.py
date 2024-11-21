# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user
import requests
from ..utilities.translator import fromRequestIntoCard


DEFAULT_PAGE = '1'
DEFAULT_REST_API_URL = 'https://rickandmortyapi.com/api/character?page='
DEFAULT_NAME_QUERY_PARAM = '&name='

def getAllImages(page=1, name=None):
    api_url = f'{DEFAULT_REST_API_URL}{page}'
    if name:
        api_url += f'{DEFAULT_NAME_QUERY_PARAM}{name}'
        
    response = requests.get(api_url)
    
    if response.status_code == 200:
        try:
            json_collection = response.json()
            results = json_collection.get('results', [])
        except ValueError:
            print("Error decoding JSON")
            results = []
    else:
        print(f"Error fetching API: {response.status_code}")
        results = []

    images = [fromRequestIntoCard(raw_data) for raw_data in results]

    print(f"Page {page}, Name {name}: {images}")  # Verifica los datos obtenidos
    return images





# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.S

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.