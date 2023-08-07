"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest

from .forms import BookingForm, UserRegistrationForm

from .models import Menu, Imagem
# from .forms import ClientForm, ImagemForm

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'app/menu_item.html', {"menu_item": menu_item}) 

def menu(request, pk=None):
    menu_cat = Menu.objects.all().order_by('id')
    menu_data = Menu.objects.all().order_by('id')
    main_data = {"cats": menu_cat, "menu": menu_data}
    return render(request, "app/menu.html", main_data)

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'app/book.html', context)

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = UserRegistrationForm()
    return render(request, 'app/registro.html', {'form': form})

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
