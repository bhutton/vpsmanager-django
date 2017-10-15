# from django.http import HttpResponse
# from django.shortcuts import redirect, render
# from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from vps.models import Instance

def home_page(request):
    items = Instance.objects.all()
    return render(request, 'home.html', {'items': items})

def create_vps(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_name']
        Instance.objects.create(name=new_item_text)
        return redirect('/')
    else:
        new_item_text = ''

    return render(request, 'createvps.html', {
        'new_item_text': new_item_text,
    })


def create_user(request):
    return render(request, 'createuser.html')