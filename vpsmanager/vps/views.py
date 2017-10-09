from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
#from lists.forms import ExistingListItemForm, ItemForm
#from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')