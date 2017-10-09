from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

#from lists.views import home_page


def home_page(request):
    return render(request, 'home.html')