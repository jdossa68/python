'''Módulo de filtros personas'''

from app.models import Person

import django_filters


class PersonFilter(django_filters.rest_framework.FilterSet):
    '''     filtros para personas   '''

    class Meta:
        '''  clase meta de filtros para personas  '''

        model = Person
        fields = {
            'id': ['exact'],
            'departmentPerson' : ['exact'],
            'name': ['icontains', 'exact'],
            'lastName': ['icontains', 'exact'],
            'identification': ['icontains', 'exact'],
            'email': ['icontains', 'exact'],
        }
        ordering_fields = ('name', 'lastName', 'identification', 'email')