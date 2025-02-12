from django.shortcuts import render

# Create your views here.
def login_senseSessio(request):
    return render(request,'login.html')

def inici(request):
    return render(request,'inici.html')