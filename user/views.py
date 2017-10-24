from django.shortcuts import redirect, render
from user.models import Instance

CHECKBOX_MAPPING = {'on': True,
                    'off': False, }

def create_user(request):
    return render(request, 'createuser.html')