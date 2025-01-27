from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def teachers(request):

    professor1 = {"nom": "Roger", "cognom1": "Sobrino","cognom2": "Martínez", "email": "roger@ticbcn.com", "curs":"DAM2B, DAW2A","tutor":"Si", "moduls": "Entorn Servidor"}
    professor2 = {"nom": "Oriol", "cognom1": "Roca","cognom2": "Fernández", "email": "oriol@ticbcn.com", "curs":"DAW2B, DAW2A, DAW1A","tutor":"No", "moduls": "Entorn Client"}
    professor3 = {"nom": "Juanma", "cognom1": "Biel","cognom2": "Nicasi", "email": "juanma@ticbcn.com", "curs":"DAM2B, DAW2A","tutor":"No", "moduls": "Desplegament"}
    
    return render(request, 'teachers.html', {"professor1": professor1,"professor2": professor2,"professor3": professor3})

def students(request):
    student1 = {"nom": "Anna", "cognom1": "Gonzalez", "cognom2": "Martínez", "email": "anna@ticbcn.com", "curs": "DAW2A", "moduls": "Programació"}
    student2 = {"nom": "Marc", "cognom1": "Pastor", "cognom2": "Fernández", "email": "marc@ticbcn.com", "curs": "DAW2A", "moduls": "Bases de Dades"}
    student3 = {"nom": "Paula", "cognom1": "Pérez", "cognom2": "Nicasi", "email": "paula@ticbcn.com", "curs": "DAW2A", "moduls": "Sistemes"}

    return render(request, 'students.html', {"student1": student1, "student2": student2, "student3": student3})