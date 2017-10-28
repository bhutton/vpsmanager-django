from django.shortcuts import redirect, render
from vps.models import Instance
from vps.forms import ExistingListItemForm

CHECKBOX_MAPPING = {'on': True,
                    'off': False, }

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
        new_item_create_disk = CHECKBOX_MAPPING.get(request.POST['item_create_disk'])
        new_item_create_path = CHECKBOX_MAPPING.get(request.POST['item_create_path'])

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

def modify_vps(request):
    if request.method == 'POST':
        new_item_id = int(request.POST['item_id'])
        new_item_name = request.POST['item_name']
        new_item_description = request.POST['item_description']
        new_item_image = request.POST['item_image']
        new_item_memory = request.POST['item_memory']
        new_item_disk = request.POST['item_disk']
        new_item_bridge = request.POST['item_bridge']
        new_item_create_disk = CHECKBOX_MAPPING.get(request.POST['item_create_disk'])
        new_item_create_path = CHECKBOX_MAPPING.get(request.POST['item_create_path'])

        saved_items = Instance.objects.get(pk=new_item_id)
        existing_items = saved_items
        existing_items.name = new_item_name
        existing_items.description = new_item_description
        existing_items.image = new_item_image
        existing_items.memory = new_item_memory
        existing_items.disk = new_item_disk
        existing_items.bridge = new_item_bridge
        existing_items.create_disk = new_item_create_disk
        existing_items.create_path = new_item_create_path
        saved_items.save()

        # saved_items.

        return redirect('/')
    else:
        new_item_text = ''

    return render(request, 'createvps.html', {
        'new_item_text': new_item_text,
    })

def view_vps(request, list_id):
    list_ = Instance.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)

    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(list_)

    return render(request, 'list.html', {'list': list_, "form": form})

def create_user(request):
    return render(request, 'createuser.html')