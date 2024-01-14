from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('car', views.CarsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("checkauth", views.CheckAuth.as_view(), name='checkauth'),
]
