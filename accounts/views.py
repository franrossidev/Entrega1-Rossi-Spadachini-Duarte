import django
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from .forms import MyUserCreationForm, MyUserEditForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request, user)
                
                return render(request, 'index.html', {})
            else:
                return render(request, 'accounts/login.html', {'form': form})  
        else:
            return render(request, 'accounts/login.html', {'form': form})

    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {})
        else:
            return render(request, 'accounts/register.html', {'form': form})
        
    form = MyUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def perfil(request):
    return render(request,'accounts/perfil.html')

@login_required
def editar_perfil(request):
    
    user = request.user
    
    if request.method == 'POST':
        form = MyUserEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.first_name = data.get('first_name') if data.get('first_name') else user.first_name
            user.last_name = data.get('last_name') if data.get('last_name') else user.last_name
            user.email = data.get('email') if data.get('last_name') else user.email
            
            if data.get('password1') and data.get('password1') == data.get('password2'):
                user.set_password(data.get('password1'))
            user.save()
            
            return redirect('perfil')
        else:
            return render(request, 'accounts/editar_perfil.html', {'form': form})
        
    form = MyUserEditForm(
        initial={
            'email':user.email,
            'first_name':user.first_name,
            'last_name':user.last_name
        }
        )
    
    return render(request,'accounts/editar_perfil.html', {'form': form})