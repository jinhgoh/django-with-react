"""watchmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import MovieList, MovieDetail, ImageUpload, movie_list, movie_details, TitanicList, TitanicDetail, titanic_details #, FileUploadView, ExampleView
from .models import Movie, Titanic
from .serializers import MovieSerializer, PostSerializer, TitanicSerializer

#URL/watchlist/
urlpatterns = [
    path('list/', MovieList.as_view(queryset=Movie.objects.all(), serializer_class=MovieSerializer)),
    path('<int:pk>', MovieDetail.as_view(queryset=Movie.objects.all(), serializer_class=MovieSerializer)),
    path('create/', ImageUpload.as_view()),
    path('listfunction/', movie_list),
    path('detailfunction/<int:pk>', movie_details),
    path('titanic/list/', TitanicList.as_view(queryset=Titanic.objects.all(), serializer_class=TitanicSerializer)),
    path('titanic/<int:pk>', TitanicDetail.as_view(queryset=Titanic.objects.all(), serializer_class=TitanicSerializer)),
    path('titanicfunction/<int:pk>', titanic_details),
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)