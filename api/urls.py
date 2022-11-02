from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

routers=DefaultRouter()

routers.register('singer', views.SingerViewSet, basename='singer')
routers.register('song', views.SongViewSet, basename='song')


urlpatterns = [

    path('', include(routers.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
