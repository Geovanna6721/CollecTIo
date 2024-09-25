from django.shortcuts import get_object_or_404, render 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from apps.projeto.models import*
from django.contrib.auth import logout as django_logout
from django.contrib.auth import get_user_model,authenticate, login as auth_login
#from forms import Aluno

#@login_required(login_url='/auth/login')

def login(request): 
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        
        if email and password:
            # Custom authentication using email and password
            user = authenticate(request, username=email, password=password)
            
            if user:
                if user.is_active:
                    auth_login(request, user)  # Log the user in
                    # Redirect to profile page with the user ID as a URL parameter
                    return redirect(reverse('perfil', kwargs={'id': user.id}))
            else:
                # Add some feedback for invalid login attempt
                return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def perfil(request, id):
    # Obtém o usuário com base no id passado
    usuario = get_object_or_404(CustomUser, id=id)

    # Filtra os arquivos do usuário
    arquivos_user = Arquivos.objects.filter(user=usuario)  # Supondo que 'user' é o campo que relaciona Arquivos ao User

    dados = {
        'arquivos': arquivos_user,
    }
    print(dados)
    return render(request,"perfil.html",dados )    

@login_required(login_url='/login')
def arquivo(request):
    if request.method == 'POST':
        # Obtendo os dados do formulário
        capa = request.FILES.get('capa', None)  # Arquivo enviado via 'FILES'
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        descricao = request.POST.get('descricao')
        area = request.POST.get('area_conhecimento')
        link_arquivo = request.POST.get('link_arquivo')

        # Criando um novo objeto Arquivos
        new_arquivo = Arquivos.objects.create(
            capa=capa,
            titulo=titulo,
            autor=autor,
            descricao=descricao,
            area_de_con=area,  # Atribui a área de conhecimento ao campo `area_de_con`
            upload=link_arquivo,
            user=request.user  # Relaciona o arquivo com o usuário autenticado
        )

        # Salvando o objeto
        new_arquivo.save()

        # Redirecionando após o sucesso
        return HttpResponseRedirect('/')

    # Caso não seja POST, renderizar a página com o formulário
    return render(request, 'arquivo.html')


@login_required (login_url='/login')
def home(request):
    arquivo = Arquivos.objects.all()
    dados = {
        "arquivos": arquivo,
    }
    return render(request, 'home.html', dados)

def usuario(request): 

    if request.method == 'POST':
        print('teste')
        fname = request.POST['name']
        lname = request.POST['sobrenome']
        email = request.POST['email']
        pass1 = request.POST['password']
        matricula = request.POST['number']
        gender = request.POST['gender']
        curso = request.POST['curso']

        # Comando para adicionar um novo usuario
       
        newuser = CustomUser.objects.create_user(email,email,pass1)
        newuser.first_name = fname
        newuser.last_name = lname
        newuser.matricula = matricula
        newuser.genero_usuario = gender
        newuser.curso = curso


        newuser.save()

        return  HttpResponseRedirect('/login')


    return render(request,"usuario.html")

def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('/')

