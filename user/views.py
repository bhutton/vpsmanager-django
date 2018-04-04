from django.shortcuts import redirect, render

CHECKBOX_MAPPING = {'on': True,
                    'off': False, }


def create_user(request):
    return render(request, 'createuser.html')


def modify_user(request):
    return render(request, 'modifyuser.html')