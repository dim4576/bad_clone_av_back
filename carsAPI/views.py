from .models import Cars
from .serializers import CarsSerializer
from rest_framework import viewsets
from .permissions import CustomPermission
from rest_framework import filters

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (CustomPermission,)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['brand', 'model']