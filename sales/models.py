from pyexpat import model
from tkinter import CASCADE
from unicodedata import category
from django.db import models
import sales


# base class for anything that is used to store goods

class Storage(models.Model):
    name = models.CharField(max_length=100,default="default-name",null=False)
    totalsales = models.IntegerField()
    targetsales= models.IntegerField()
    #This can be later on coverted to it's own class if there are more choices needed
    STORAGE_TYPE = (
        ("Factory", 'factory'),
        ("Warehouse", 'warehouse'),
        ("Godown", 'godown'),
        ("Stock", 'stock')
    )
    type = models.CharField(max_length=25, choices=STORAGE_TYPE)

    parents = models.ManyToManyField('self', null=True, blank=True, related_name='p', symmetrical=False)

    
    def __str__(self):
        return self.name