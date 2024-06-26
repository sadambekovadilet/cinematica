from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('serializer/', views.TestView.as_view()),
]

cinematic_routes = DefaultRouter()

cinematic_routes.register(r"movie", views.MovieViews)
cinematic_routes.register(r"create_view", views.MovieViewCreate)