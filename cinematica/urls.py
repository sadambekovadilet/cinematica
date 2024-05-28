from rest_framework.routers import DefaultRouter

from . import views


cinematic_routes = DefaultRouter()

cinematic_routes.register(r"top_list", views.MovieList)