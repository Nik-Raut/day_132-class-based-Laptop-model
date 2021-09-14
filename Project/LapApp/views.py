from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Laptop
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required





#------------------homeview -------- normal way
def homeview(request):
    template_name='LapApp/base.html'
    context={}
    return render(request,template_name,context)



#------------------Built-in class-based generic views

class LaptopListview(ListView):
    model = Laptop


class LaptopCreateView(CreateView):
    model = Laptop
    fields = '__all__'
    success_url = '/LapApp/list/'


class LaptopUpdateView(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/LapApp/list/'


class LaptopDeleteView(DeleteView):
    model = Laptop
    success_url = '/LapApp/list/'




