import requests
from rest_framework.filters import OrderingFilter
from rest_framework import routers, viewsets,serializers
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Person
from django_filters.rest_framework import DjangoFilterBackend

from ..filters import PersonFilter
from ..serializer import PersonSerializer


class PersonView(viewsets.ModelViewSet):
  '''Archivo de vistas de personas'''

  permission_code = 'Person'
  queryset = Person.objects.all()
  serializer_class = PersonSerializer
  filter_class = PersonFilter
  filter_backends = (DjangoFilterBackend, OrderingFilter)

@api_view(['POST'])
def consultDepartmentView(request):
    dataConsult = []
    query = Person.objects.select_related('departmentPerson').filter(identification = request.data.get('document'))
    if query:
      for i in query:
        dataConsult.append({
          'name': i.name,
          'department': i.departmentPerson.department,
          'lastName': i.lastName,
        })
      return Response(dataConsult, status=200)
    else:
      return Response('Error', status=400)
    