from django.db import models


class Materiais(models.Model):
    CHOICES = [
        ('CIR', 'Cirugico'),
        ('DESC', 'descartavel'),
    ]
    
    name = models.CharField(max_length=100, default="", blank=True)
    data = models.DateField(blank=True)
    type_material = models.CharField(max_length=10, choices=CHOICES,blank=True)
    stage = models.CharField(max_length=100, blank=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name
