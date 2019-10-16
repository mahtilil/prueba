#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from polls.models import Pregunta, Opcion

from django.template import loader

def agregar_preguntas(request):
	template = loader.get_template('polls/agregar_preguntas.html')
	context = {}
	return HttpResponse(template.render(context, request))

def validar_formulario(request):
	c1 = request.POST.get('txtPregunta')
	c2 = request.POST.get('txtFecha')
	c3 = request.POST.get('txtHora')

	if c1.strip() == "" or c2.strip() == "" or c3.strip() == "":
		return HttpResponse("Debe llenar todos los campos")
	else:
		return HttpResponse("Ty")

def index(request):
	preguntas = Pregunta.objects.order_by('-fecha')[:5]
	template = loader.get_template('polls/index.html')
	context = { 'listado': preguntas,}
	return HttpResponse(template.render(context, request))

def detalle(request, id_pregunta):
	pregunta = Pregunta.objects.get(id=id_pregunta)
	template = loader.get_template('polls/detalle.html')
	context = { 'pregunta': pregunta,}
	return HttpResponse(template.render(context, request))

def resultados(request, total):
	latest_question_list = Pregunta.objects.order_by('fecha')[:total]
	output = ', '.join([q.descripcion for q in latest_question_list])
	return HttpResponse(output)