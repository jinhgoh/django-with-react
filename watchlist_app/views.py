from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
# from django.http import JsonResponse
from rest_framework import generics
# Create your views here.

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values())
#         }
#     return JsonResponse(data)