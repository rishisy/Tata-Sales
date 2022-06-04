
from django import forms
from .models import Storage
 
class MyForm(forms.ModelForm):
  class Meta:
    model = Storage
    fields = ["name","totalsales", "targetsales","type","parents"]
    labels = {'name':"name",'totalsales': "totalsales", "targetsales": "targetsales",   }