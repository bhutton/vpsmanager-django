from django.shortcuts import redirect, render

from user.models import User

def create_user(request):
    if request.method == 'POST':
        new_username = request.POST['username']
        new_password = request.POST['password']
        User.objects.create(username=new_username, password=new_password)
        return redirect('/')

    return render(request, 'createuser.html')


def modify_user(request, id):
    if request.method == 'POST':
        new_username = request.POST['username']
        new_password = request.POST['password']

        saved_items = User.objects.get(pk=id)
        existing_items = saved_items

        existing_items.username = new_username
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