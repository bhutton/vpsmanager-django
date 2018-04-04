from django.shortcuts import redirect, render

from user.models import User

CHECKBOX_MAPPING = {'on': True,
                    'off': False, }


def create_user(request):
    if request.method == 'POST':
        new_username = request.POST['username']
        new_password = request.POST['password']
        item = User.objects.create(username=new_username, password=new_password)
        return redirect('/')

    return render(request, 'createuser.html')


def modify_user(request):
    return render(request, 'modifyuser.html')


def view_user(request, username):
    return render(request, 'viewuser.html')

def list_user(request):
    return render(request, 'listuser.html')