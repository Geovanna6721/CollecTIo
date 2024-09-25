from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # Import settings to use AUTH_USER_MODEL

class Arquivos(models.Model):
    capa = models.ImageField(verbose_name='Capa', blank=True, null=True)
    titulo = models.CharField(verbose_name='Título', max_length=100)
    autor = models.CharField(verbose_name='Autor', max_length=50)
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    
    area = [
        ("1", "Saúde"),
        ("2", "Tecnologia"),
        ("3", "Linguagens"),
        ("4", "Ciências Exatas"),
        ("5", "Ciências Humanas"),
    ]   
    area_de_con = models.CharField(verbose_name='Área de Conhecimento', max_length=3, choices=area)
    upload = models.URLField(verbose_name="Upload do Arquivo")

    # ForeignKey to link Arquivos to CustomUser
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='arquivos')

    class Meta:
        verbose_name = 'Arquivo'

class CustomUser(AbstractUser):
    perfil = models.ImageField(verbose_name="Foto", null=True, blank=True)
    matricula = models.CharField(max_length=15, blank=True, null=True)
    
    # Gender choices
    GENERO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("OU", "Prefiro não dizer"),
        ("NI", "Não Informado"),
    )
    
    curso = models.CharField(verbose_name="Nome do Curso", blank=True, max_length=50)
    genero_usuario = models.CharField(verbose_name='Gênero', max_length=2, choices=GENERO_CHOICES, blank=True, default='NI')

    def __str__(self):
        return self.username
