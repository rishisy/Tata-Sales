from django import views
from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello -- Go to ( /view )  to see the sales views -- Go to ( /crud ) to perform crud operations on tha data "
    )
	

from .models import Storage
from .forms import MyForm
 
def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'crud.html', {'form': form})



from django.views.generic.list import ListView

def Salesview(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Storage.objects.all()
         
    return render(request, "view.html", context)

