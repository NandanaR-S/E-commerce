from pyexpat.errors import messages
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CartItemForm, ContactForm
from userapp.models import UserModel




def login(request):
    data='valid'
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        userdata=UserModel.objects.filter(Username=username, Password=password, Status='active')
        if userdata:
            request.session['user']=username
            return redirect('/home/')
        else:
            data='invalid'
    return render(request,'login.html',{'message':data})




def signup(request):
    if request.method=='POST':
        Username=request.POST.get('name')
        Password=request.POST.get('password')
        Email=request.POST.get('email')
        Phone_Number=request.POST.get('phone_number')


        user_obj=UserModel()
        user_obj.Username=Username
        user_obj.Password=Password
        user_obj.Email=Email
        user_obj.Phone_Number=Phone_Number
        user_obj.save()
        return HttpResponse ('<h1>Account Created Successfully</h1><a href="/">Login</a>')
    else:
        redirect('/home')

    return render(request, 'signup.html')


def homepage(request):

    if 'user' in request.session:
        username=request.session['user']
        user_data=UserModel.objects.get(Username=username)
        return render(request,'home.html',{'data':user_data})
    else:
        return render(request,'home.html')

def cart_view(request):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            update_cart(request, quantity)
            return redirect('/')
    else:
        form = CartItemForm()

    # Render the cart page with the form
    return render(request, 'cart.html', {'form': form})

def update_cart(request, quantity):
    # Logic to update the cart
    pass


def contact(request):
    return render(request, 'contact.html')




def wishlist(request):
    # Sample data for the wishlist
    products = [
        {'name': 'Product 1', 'price': 29.99, 'image': 'path/to/product1.jpg'},
        {'name': 'Product 2', 'price': 39.99, 'image': 'path/to/product2.jpg'},
        {'name': 'Product 3', 'price': 49.99, 'image': 'path/to/product3.jpg'},
    ]
    return render(request, 'wishlist.html', {'products': products})

from django.shortcuts import render

def men(request):
    return render(request, 'men.html')

