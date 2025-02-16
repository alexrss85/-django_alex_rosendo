from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

professors = [
    {"id": 1, "nom": "Roger", "cognom1": "Sobrino", "cognom2": "Martínez", "email": "roger@ticbcn.com", "curs": "DAM2B, DAW2A", "tutor": "Si", "moduls": "Entorn Servidor"},
    {"id": 2, "nom": "Oriol", "cognom1": "Roca", "cognom2": "Fernández", "email": "oriol@ticbcn.com", "curs": "DAW2B, DAW2A, DAW1A", "tutor": "No", "moduls": "Entorn Client"},
    {"id": 3, "nom": "Juanma", "cognom1": "Biel", "cognom2": "Nicasi", "email": "juanma@ticbcn.com", "curs": "DAM2B, DAW2A", "tutor": "No", "moduls": "Desplegament"},
]

alumnes = [
    {"id": 1, "nom": "Anna", "cognom1": "Gonzalez", "cognom2": "Martínez", "email": "anna@ticbcn.com", "curs": "DAW2A", "moduls": "Programació"},
    {"id": 2, "nom": "Marc", "cognom1": "Pastor", "cognom2": "Fernández", "email": "marc@ticbcn.com", "curs": "DAW2A", "moduls": "Bases de Dades"},
    {"id": 3, "nom": "Paula", "cognom1": "Pérez", "cognom2": "Nicasi", "email": "paula@ticbcn.com", "curs": "DAW2A", "moduls": "Sistemes"},
    {"id": 4, "nom": "David", "cognom1": "López", "cognom2": "Sánchez", "email": "david@ticbcn.com", "curs": "DAW2A", "moduls": "Programació"},
    {"id": 5, "nom": "Laura", "cognom1": "Molina", "cognom2": "Vázquez", "email": "laura@ticbcn.com", "curs": "DAW2B", "moduls": "Bases de Dades"},
    {"id": 6, "nom": "Javier", "cognom1": "García", "cognom2": "Ruiz", "email": "javier@ticbcn.com", "curs": "DAW2B", "moduls": "Sistemes"},
    {"id": 7, "nom": "Carla", "cognom1": "Martín", "cognom2": "Fernández", "email": "carla@ticbcn.com", "curs": "DAW2B", "moduls": "Programació"},
    {"id": 8, "nom": "Sergio", "cognom1": "Rodríguez", "cognom2": "Alonso", "email": "sergio@ticbcn.com", "curs": "DAW2B", "moduls": "Bases de Dades"},
    {"id": 9, "nom": "Sandra", "cognom1": "López", "cognom2": "Pérez", "email": "sandra@ticbcn.com", "curs": "DAW2A", "moduls": "Programació"},
    {"id": 10, "nom": "Antonio", "cognom1": "Ramírez", "cognom2": "Serrano", "email": "antonio@ticbcn.com", "curs": "DAW2A", "moduls": "Sistemes"},
    {"id": 11, "nom": "María", "cognom1": "Fernández", "cognom2": "García", "email": "maria@ticbcn.com", "curs": "DAW2A", "moduls": "Bases de Dades"},
    {"id": 12, "nom": "Luis", "cognom1": "Sánchez", "cognom2": "Vega", "email": "luis@ticbcn.com", "curs": "DAW2B", "moduls": "Sistemes"},
    {"id": 13, "nom": "Bea", "cognom1": "Ruiz", "cognom2": "Pérez", "email": "bea@ticbcn.com", "curs": "DAW2A", "moduls": "Programació"},
]


def profes(request):

    return render(request, 'teachers.html', {"professors": professors})

def students(request):
    
    return render(request, 'students.html', {"alumnes": alumnes})


def teacher_detail(request, pk):
    teacher_obj = None
    for teacher in professors:
        if teacher["id"] == pk:
            teacher_obj = teacher
    return render(request, 'teacher_detail.html', {"teacher": teacher_obj})


def student_detail(request, pk):
    student_obj = None
    for student in alumnes:
        if student["id"] == pk:
            student_obj = student
    return render(request, 'student_detail.html', {"student": student_obj})

