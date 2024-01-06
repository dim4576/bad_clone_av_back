from .models import Cars
from .serializers import CarsSerializer
from rest_framework import viewsets
from .permissions import CustomPermission
from rest_framework import filters
from django.http import JsonResponse

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (CustomPermission,)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['brand', 'model']

def checkAuth(request):
    if request.user.is_authenticated:
        data = {
            #"params": request.headers.get(),
            "auth": "ok",
            "username": request.user.username
        }
    else:
        data = {
            "params": request.headers.get('Authorization'),
            "auth": "invalid"
        }
    return JsonResponse(data, status=200)
