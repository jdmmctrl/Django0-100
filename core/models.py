from django.db import models
from datetime import datetime

# Create your models here.

class Employee(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de edición')
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', blank=True, null=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    db_table ='empleados'
    ordering = ['id']