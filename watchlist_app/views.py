from django.shortcuts import render
from .models import Movie, Titanic
from .serializers import MovieSerializer, PostSerializer, TitanicSerializer
from django.http import JsonResponse
from rest_framework import generics, status

from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from . import fake_model
from . import ml_predict
import json

# from rest_framework.permissions import IsAuthenticated
# Create your views here.


def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
        }
    return JsonResponse(data)


def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active,
        'num2': movie.num1 * 2
    }
    return JsonResponse(data)


class MovieList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
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

        
class TitanicList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Titanic.objects.all()
    serializer_class = TitanicSerializer

    
class TitanicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Titanic.objects.all()
    serializer_class = TitanicSerializer


def titanic_details(request, pk):
    titanic = Titanic.objects.get(pk=pk)
    pclass = titanic.pclass
    sex = titanic.sex
    age = titanic.age
    sibsp = titanic.sibsp
    parch = titanic.parch
    fare = titanic.fare
    embarked = titanic.embarked
    title = titanic.title
    prediction = ml_predict.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    list_prediction = prediction.tolist()
    json_prediction = json.dumps(list_prediction)
    data = {
        'result': titanic.pclass + titanic.sex + titanic.age,
        'prediction': json_prediction
    }
    print("MachinLearning result: ", prediction)
    return JsonResponse(data)
    
        
        
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
    
