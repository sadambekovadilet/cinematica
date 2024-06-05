from django.http.request import HttpRequest
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as drf_filters

from datetime import date

from cinematica.models import Movie, View
from cinematica.serializers import (
    MovieSerializerList, SomeSerializer,
    MovieViewSerializer, MovieDetailSerializerList,
)

class TestClass:
    def __init__(self, name: str, date_of_birth: date) -> None:
        self.name = name
        self.date_of_birth = date_of_birth



class TestView(APIView):
    def get(self, request: HttpRequest):
        print(request)
        c1 = TestClass('Name', date(2000, 10, 19))
        serializer = SomeSerializer(c1)
        return Response(status=200, data=serializer.data)


class MovieViews(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    pagination_class = LimitOffsetPagination
    queryset = Movie.objects.all()
    serializer_class = MovieSerializerList
    filter_backends = (drf_filters.DjangoFilterBackend,)
    filterset_fields = ('janr_id', 'authors')
    
    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializer_class
        elif self.action == 'retrieve':
            return MovieDetailSerializerList

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset
        elif self.action == 'retrieve':
            return Movie.objects.annotate(views_count=Count('views'), reviews_count=Count('reviews'))


class MovieViewCreate(GenericViewSet, CreateModelMixin):
    serializer_class = MovieViewSerializer
    queryset = View.objects.all()
