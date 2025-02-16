from django.db import connection
from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Usuari

def login_sense_sessio(request):
    error = None 
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            contrasenya = form.cleaned_data["contrasenya"]
            
            try:
                usuari = Usuari.objects.get(email=email, contrasenya=contrasenya)
                return redirect("inici")
            except Usuari.DoesNotExist:
                error = "Credencials incorrectes."

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form, "error": error})





def login_amb_sessio(request):
    if request.user.is_authenticated:  
        return redirect("inici") 

    error = None

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            contrasenya = form.cleaned_data["contrasenya"]

            usuari = authenticate(request, username=email, password=contrasenya)  

            if usuari is not None:
                login(request, usuari)  
                return redirect("inici")  
            else:
                error = "Credenciales incorrectas."

    else:
        form = LoginForm()

    return render(request, "autenticacio/login.html", {"form": form, "error": error})





def inici(request):

    db_name = connection.settings_dict['NAME']

    return render(request, "inici.html", {
        "usuari": request.user,  
        "db_name": db_name,     
    })


def logout(request):
    request.session.flush() 
    return redirect("login")  