from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('car', views.CarsViewSet)
router.register('photos', views.PhotosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("checkauth", views.CheckAuth.as_view(), name='checkauth'),
]
