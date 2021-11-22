
'''Archivo de Modelos'''
from django.db import models
from django.contrib.auth.models import User

class departmentId(models.Model):
    '''Modelo departamentos'''
    
    department = models.CharField('Departamento', max_length=50)
    def __str__(self):
        return self.department

class Person(models.Model):
    '''Modelo personas'''
    
    departmentPerson = models.ForeignKey(departmentId, verbose_name='Departamento por persona', on_delete=models.CASCADE)
    name = models.CharField('Nombre', max_length=50)
    lastName = models.CharField('Apellido', max_length=50)
    identification = models.CharField('Identificación', max_length=50)
    email =  models.EmailField('Correo electronico', max_length=50)
    

