from django.shortcuts import redirect, render
from .forms import LoginForm
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

def inici(request):
    return render(request,'inici.html')