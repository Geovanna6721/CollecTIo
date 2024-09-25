from django import forms

class Alunos(forms.Form):
    nome = forms.CharField(max_length=100, null= False)
    email = forms.EmailField(max_length=50, null= False)
    cpf = forms.CharField(max_length=11, null= False)
    data_nascimento = forms.DateField(input_formats='xx/xx/xxxx', null= False)
    matricula = forms.CharField (max_length=12, null= False)