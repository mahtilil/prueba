from django import forms

class PreguntasForm(forms.Form):
	pregunta = forms.CharField(max_length=50)
	fecha = forms.DateField()
	hora = forms.TimeField()