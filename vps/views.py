from django.shortcuts import redirect, render
from vps.models import Instance, Disk, Network, InstanceControl
from vps.forms import ExistingListItemForm

CHECKBOX_MAPPING = {'on': True,
                    None: False, }


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
        try:
            new_item_create_disk = CHECKBOX_MAPPING.get(request.POST['item_create_disk'])
        except:
            new_item_create_disk = False

        try:
            new_item_create_path = CHECKBOX_MAPPING.get(request.POST['item_create_path'])
        except:
            new_item_create_path = False

        item = Instance.objects.create(
            name=new_item_name,
            description=new_item_description,
            image=new_item_image,
            memory=new_item_memory,
            disk=new_item_disk,
            create_disk=new_item_create_disk,
            create_path=new_item_create_path
        )

        Disk.objects.create(name='', instance=item, size=int(new_item_disk))
        Network.objects.create(name='', bridge=new_item_bridge, instance=item)

        return redirect('/')
    else:
        new_item_text = ''

    return render(request, 'createvps.html', {
        'new_item_text': new_item_text,
    })


def modify_vps(request,id):
    if request.method == 'POST':
        new_item_name = request.POST['item_name']
        new_item_description = request.POST['item_description']
        new_item_image = request.POST['item_image']
        new_item_memory = request.POST['item_memory']
        new_item_disk = request.POST['item_disk']
        new_item_bridge = request.POST['item_bridge']

        try:
            new_item_create_disk = CHECKBOX_MAPPING.get(request.POST['item_create_disk'])
        except:
            new_item_create_disk = False

        try:
            new_item_create_path = CHECKBOX_MAPPING.get(request.POST['item_create_path'])
        except:
            new_item_create_path = False

        saved_items = Instance.objects.get(pk=id)
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

        return redirect('/')
    else:
        saved_items = Instance.objects.all().filter(pk=id)

    return render(request, 'modifyvps.html', {
        'items': saved_items,
    })


def delete_vps(request, id):
    if request.method == "GET":
        saved_items = Instance.objects.get(pk=id)
        saved_items.delete()
    return redirect('/')


def view_vps(request, list_id):
    instance = Instance.objects.all().filter(pk=list_id)
    disks = Disk.objects.all().filter(instance_id=instance[0].id)
    device = Network.objects.all().filter(instance_id=instance[0].id)

    return render(request, 'viewvps.html', {
        'row': instance,
        'disks': disks,
        'device': device,
    })


def start_vps(request, id):
    vps = InstanceControl()
    status = vps.start(id)

    saved_items = Instance.objects.get(pk=id)
    existing_items = saved_items
    existing_items.status = status
    saved_items.save()

    instance = Instance.objects.all().filter(pk=id)
    disks = Disk.objects.all().filter(instance_id=instance[0].id)
    device = Network.objects.all().filter(instance_id=instance[0].id)

    return render(request, 'viewvps.html', {
        'row': instance,
        'disks': disks,
        'device': device,
    })


def stop_vps(request, id):
    vps = InstanceControl()
    status = vps.stop(id)

    saved_items = Instance.objects.get(pk=id)
    existing_items = saved_items
    existing_items.status = status
    saved_items.save()

    instance = Instance.objects.all().filter(pk=id)
    disks = Disk.objects.all().filter(instance_id=instance[0].id)
    device = Network.objects.all().filter(instance_id=instance[0].id)

    return render(request, 'viewvps.html', {
        'row': instance,
        'disks': disks,
        'device': device,
    })

def status_vps(request, id):
    vps = InstanceControl()
    status = vps.status(id)

    saved_items = Instance.objects.get(pk=id)
    existing_items = saved_items
    existing_items.status = status
    saved_items.save()

    instance = Instance.objects.all().filter(pk=id)
    disks = Disk.objects.all().filter(instance_id=instance[0].id)
    device = Network.objects.all().filter(instance_id=instance[0].id)


    return render(request, 'viewvps.html', {
        'row': instance,
        'disks': disks,
        'device': device,
    })


def snapshot_vps(request, id):
    instance = Instance.objects.all().filter(pk=id)
    disks = Disk.objects.all().filter(instance_id=instance[0].id)
    device = Network.objects.all().filter(instance_id=instance[0].id)

    return render(request, 'viewvps.html', {
        'row': instance,
        'disks': disks,
        'device': device,
    })


def create_user(request):
    return render(request, 'createuser.html')