from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer, PostSerializer
# from django.http import JsonResponse
from rest_framework import generics, status

from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ImageUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    

# class ExampleView(APIView):
#     """
#     A view that can accept POST requests with JSON content.
#     """
#     parser_classes = (MultiPartParser,)

#     def post(self, request, format=None):
#         # to access files
#         print request.FILES
#         # to access data
#         print request.data
#         return Response({'received data': request.data})    
    
# class FileUploadView(APIView):
#     parser_classes = [FileUploadParser]

#     def put(self, request, filename, format=None):
#         file_obj = request.data['file']
#         # ...
#         # do some stuff with uploaded file
#         # ...
#         return Response(status=204)
    
# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values())
#         }
#     return JsonResponse(data)