from .models import Cars, Photos
from .serializers import CarsSerializer, PhotosSerializer
from rest_framework import viewsets
from .permissions import CustomPermission
from rest_framework import filters
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()[:30]
    serializer_class = CarsSerializer
    permission_classes = (CustomPermission,)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['brand', 'model']


class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    permission_classes = (CustomPermission,)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['car_id']


class CheckAuth(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        if request.user.is_authenticated:
            data = {
                # "params": request.headers.get(),
                "auth": "ok",
                "username": request.user.username
            }
        else:
            data = {
                "params": request.headers.get('Authorization'),
                "auth": "invalid",
                "user": request.user.username
            }
        return JsonResponse(data, status=200)
