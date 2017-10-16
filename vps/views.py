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
        new_item_name = request.POST['item_name']
        new_item_description = request.POST['item_description']
        new_item_image = request.POST['item_image']
        new_item_memory = request.POST['item_memory']
        new_item_disk = request.POST['item_disk']
        new_item_bridge = request.POST['item_bridge']
        new_item_create_disk = request.POST['item_create_disk']
        new_item_create_path = request.POST['item_create_path']
        Instance.objects.create(
            name=new_item_name,
            description=new_item_description,
            image=new_item_image,
            memory=new_item_memory,
            disk=new_item_disk,
            bridge=new_item_bridge,
            create_disk=new_item_create_disk,
            create_path=new_item_create_path
        )
        return redirect('/')
    else:
        new_item_text = ''

    return render(request, 'createvps.html', {
        'new_item_text': new_item_text,
    })


def create_user(request):
    return render(request, 'createuser.html')