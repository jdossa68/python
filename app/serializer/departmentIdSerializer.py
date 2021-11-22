''' serializador para departamentos'''

from django.contrib.auth.models import Group
from rest_framework import serializers

from app.models import departmentId


class departmentIdSerializer(serializers.HyperlinkedModelSerializer):
  '''serializador para departamentos'''

  class Meta:

    model = departmentId
    fields = ('url', 'id', 'department')