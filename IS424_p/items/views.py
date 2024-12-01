from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Item
from django.contrib.auth import authenticate, login
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)  # Use Django's built-in login function
            return redirect('list_items')  # Redirect to the desired page
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validation checks
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Automatically log the user in
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect('list_items')  # Redirect to the homepage or dashboard

    return render(request, 'register.html')

def list_items(request):
    items = Item.objects.all()
    return render(request, 'list_items.html', {'items': items})

def detail_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        if item.quantity > 0:
            item.users.add(request.user)  # Link user to item
            item.quantity -= 1  # Reduce available quantity
            item.save()
            messages.success(request, f"You have successfully added/purchased/rented '{item.name}'.")
        else:
            messages.error(request, f"'{item.name}' is out of stock.")
        return redirect('detail_item', item_id=item_id)

    return render(request, 'detail_item.html', {'item': item})

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        # Save to the database
        item = Item(name=name, description=description, price=price, quantity=quantity)
        item.save()

        return redirect('list_items')  # Redirect to the list page after successful submission

    return render(request, 'add_item.html')

def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        # Get the updated values from the form
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        # Validate and update the item
        if not name or not price or not quantity:
            messages.error(request, "Please fill out all fields!")
        else:
            item.name = name
            item.description = description
            item.price = price
            item.quantity = quantity
            item.save()
            messages.success(request, "Item updated successfully!")
            return redirect('list_items')  # Redirect to item list page after updating

    # Render the template with the item data
    return render(request, 'update_item.html', {'item': item})
