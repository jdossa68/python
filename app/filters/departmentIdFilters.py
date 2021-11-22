'''Módulo de filtros departamentos'''

from app.models import departmentId

import django_filters


class departmentIdFilter(django_filters.rest_framework.FilterSet):
    '''filtros para departamentos'''

    class Meta:
        '''clase meta de filtros para departamentos'''

        model = departmentId
        fields = {
            'id': ['exact'],
            'department': ['icontains', 'exact'],
        }
        ordering_fields = ('department')