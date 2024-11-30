from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Item

def login(request):
    if request.method == 'POST':
        return redirect('list_items')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        User.objects.create(username=username, email=email)
        return redirect('login')
    return render(request, 'register.html')

def list_items(request):
    items = Item.objects.all()
    return render(request, 'list_items.html', {'items': items})

def detail_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'detail_item.html', {'item': item})

def add_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Item.objects.create(name=name, description=description, price=price)
        return redirect('list_items')
    return render(request, 'add_item.html')

def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.price = request.POST['price']
        item.save()
        return redirect('list_items')
    return render(request, 'update_item.html', {'item': item})
