from django.http.request import HttpRequest

from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from cinematica.models import Movie
from cinematica.serializers import MovieSerializerList

class Welcome(APIView):

    def get(self, request: HttpRequest):
        return Response(data={'message': 'Hello, world!'})



class MovieList(GenericViewSet, ListModelMixin):
    pagination_class = LimitOffsetPagination
    queryset = Movie.objects.all()
    serializer_class = MovieSerializerList
