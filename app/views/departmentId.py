from rest_framework.filters import OrderingFilter
from rest_framework import routers, viewsets,serializers
from rest_framework.filters import OrderingFilter

from app.models import departmentId
from django_filters.rest_framework import DjangoFilterBackend

from ..filters import departmentIdFilter
from ..serializer import departmentIdSerializer


class departmentIdView(viewsets.ModelViewSet):
  '''Archivo de vistas de departamentos'''

  permission_code = 'departmentId'
  queryset = departmentId.objects.all()
  serializer_class = departmentIdSerializer
  filter_class = departmentIdFilter
  filter_backends = (DjangoFilterBackend, OrderingFilter)