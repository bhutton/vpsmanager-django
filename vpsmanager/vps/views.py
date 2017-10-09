from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
#from lists.forms import ExistingListItemForm, ItemForm
#from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def create_vps(request):
    return render(request, 'createvps.html')

def create_user(request):
    return render(request, 'createuser.html')