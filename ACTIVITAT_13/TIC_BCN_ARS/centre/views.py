from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def teachers(request):

    professor1 = {"id": 1, "name": "Roger", "surname": "Sobrino", "age": "39", "curs":"DAM2B, DAW2A"}
    professor2 = {"id": 2, "name": "Oriol", "surname": "Roca", "age": "25", "curs":"DAW2B, DAW2A, DAW1A"}
    professor3 = {"id": 3, "name": "Juanma", "surname": "Biel", "age": "24", "curs":"DAM2B, DAW2A"}
    

    return render(request, 'teachers.html', {"professor1": professor1,"professor2": professor2,"professor3": professor3})
