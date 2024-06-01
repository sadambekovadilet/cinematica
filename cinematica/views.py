from django.http.request import HttpRequest

from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as drf_filters

from datetime import date

from cinematica.models import Movie, View
from cinematica.serializers import (
    MovieSerializerList, SomeSerializer,
    MovieViewSerializer,
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


class MovieList(GenericViewSet, ListModelMixin):
    pagination_class = LimitOffsetPagination
    queryset = Movie.objects.all()
    serializer_class = MovieSerializerList
    filter_backends = (drf_filters.DjangoFilterBackend,)
    filterset_fields = ('janr_id', 'authors')

    def list(self, request: HttpRequest, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class MovieViewCreate(GenericViewSet, CreateModelMixin):
    serializer_class = MovieViewSerializer
    queryset = View.objects.all()
    