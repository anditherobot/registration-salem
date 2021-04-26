"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import CreateView
from .models import *
from datetime import datetime, timedelta
from datetime import date
from django.urls import reverse_lazy

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
           
        }
    )



class RegistrantCreate(CreateView):
    model = RegistrantInfo

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrantCreate, self).get_context_data(*args, **kwargs)
        
        context['nextweek'] = date.today()
        context['title'] = "Request Page"
        return context

    success_url = reverse_lazy('success')
    fields = '__all__'

def success(request):
    return render(request, template_name='app/success.html')

