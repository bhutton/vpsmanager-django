from django.shortcuts import redirect, render

from user.models import User

def create_user(request):
    if request.method == 'POST':
        new_name = request.POST['name']
        new_email = request.POST['email']
        new_password = request.POST['password']
        User.objects.create(name=new_name, email=new_email, password=new_password)
        return redirect('/user/')

    return render(request, 'createuser.html')


def modify_user(request, id):
    if request.method == 'POST':
        new_name = request.POST['name']
        new_email = request.POST['email']
        new_password = request.POST['password']

        saved_items = User.objects.get(pk=id)
        existing_items = saved_items

        existing_items.name = new_name
        existing_items.email = new_email
        existing_items.password = new_password
        existing_items.save()
        return redirect('/user')

    item = User.objects.get(pk=id)
    return render(request, 'modifyuser.html', {'item': item})


def view_user(request, username):
    return render(request, 'viewuser.html')


def list_user(request):
    items = User.objects.all()
    return render(request, 'listuser.html', {'items': items})


def delete_user(request, id):
    if int(id) > 0:
        saved_items = User.objects.get(pk=id)
        saved_items.delete()

    items = User.objects.all()
    return render(request, 'listuser.html', {'items': items, 'deleted': 'yes'})