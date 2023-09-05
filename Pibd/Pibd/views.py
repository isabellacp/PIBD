from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return render(request, 'hello.html')

def insert(request):
    return render(request, 'alter_info_professor_ministrante.html')    

def cadastro_ies(request):
    return render(request, 'cadastro_ies.html')

def registro_coordenador_administrativo(request):
    return render(request, 'registro_coordenador_administrativo.html')

def data_coord_admin(request):
    return render(request, 'data_coord_admin.html')

def comp_curriculares(request):
    return render(request, 'comp_curriculares.html')

def lista_oferta_coletiva(request):
    return render(request, 'lista_oferta_coletiva.html')