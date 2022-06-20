from django.shortcuts import render
from requests import get

# Create your views here.
BASE_URL = "https://imdb-api.com/"
MOVIE_URL = "pt-br/API/SearchMovie/"

apiKey = "k_ks2nkhaq/"
movie = input('Digite o nome do filme: ')


def get_movie():
    response = get(BASE_URL+MOVIE_URL+apiKey+movie).json()
    return response


print(get_movie())
