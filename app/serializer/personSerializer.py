''' serializador para personas'''

from django.contrib.auth.models import Group
from rest_framework import serializers

from app.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
  '''serializador para personas'''

  class Meta:

    model = Person
    fields = ('url', 'id', 'departmentPerson' , 'name', 'lastName', 'identification', 'email')