from django.contrib import admin
from .models import Arquivos
from django.contrib.auth import admin as auth_admin

# Register Arquivos model
admin.site.register(Arquivos)

# Custom User admin registration
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Informações Pessoais", {"fields": ('genero_usuario','matricula','curso','perfil',)}),
    )
    list_display = ["email", "username",]

admin.site.register(CustomUser, CustomUserAdmin)
