from rest_framework import serializers
from watchlist_app.models import Movie, ImageTest, Titanic

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = "__all__"
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTest
        fields = "__all__"
        
class TitanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titanic
        fields = "__all__"