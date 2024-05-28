from rest_framework import serializers

from cinematica.models import Movie


class MovieSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'avatar', 'movie_file', 'main_artists', 'artists')