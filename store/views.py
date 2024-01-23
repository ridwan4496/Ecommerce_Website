from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm
from django import forms


def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html')

def login_user(request):
    if request.method == 'POST':
        temp_username   = request.POST['username']
        temp_password   = request.POST['password']
        random_user = authenticate(request, username=temp_username, password=temp_password)
        if random_user is not None:
            login(request, random_user)
            messages.success(request, ("Succesfully Logged Into Your Account."))
            return redirect('home')
        else:
            messages.success(request, ("Error! Please Enter Correct Username/Password And Try Again."))
            return redirect('login')
    else:
        return render(request, 'store/login.html', )

def logout_user(request):
    logout(request)
    messages.success(request, ("Logged Out From Your Account."))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # # Login user
            # new_user = authenticate(username=username, password=password)
            # login(request, new_user)
            messages.success(request, ("You Have Registered Succesfully. Welcome to PandaMart!"))
            return redirect('login')
        else:
            messages.success(request, ("Error! Please Follow The Instructions And Try Again."))
            return redirect('register')
    else:
        return render(request, 'store/register.html', context)
    
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request,"Proflie Has Been Updated Succesfully.")
            return redirect('home')
        return render(request, 'store/update_user.html',{'user_form': user_form})
    else:
        messages.success(request,"You Must Login First to Access This Page.")
        return redirect('home')        

def product(request, pk):
    item = Product.objects.get(id=pk)
    context = {
        'item': item
    }
    return render(request, 'store/product.html', context)

def category(request, cat):
    # Replace Hyphens with Spaces
    cat = cat.replace('-', ' ')
    # Grab the Category from URL
    try:
        temp_category = Category.objects.get(category_name=cat)
        items = Product.objects.filter(category_name=temp_category)
        context = {
            'items': items,
            'category': temp_category,
        }
        return render(request, 'store/category.html', context)
    
    except:
        messages.success(request, ("This category does not exist."))
        return redirect('home')
