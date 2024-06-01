from datetime import datetime

from rest_framework import serializers

from cinematica.models import Movie, Author, View



class AuthorSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'middle_name')


class MovieSerializerList(serializers.ModelSerializer):
    authors = AuthorSerializerDetail(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'avatar', 'movie_file', 'main_artists', 'artists', 'authors')


class SomeSerializer(serializers.Serializer):
    name = serializers.CharField()
    date_of_birth = serializers.DateField()
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        interval = datetime.now().date() - obj.date_of_birth
        return interval.days // 365


class MovieViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ('id', 'movie', 'user', 'total_view_time')