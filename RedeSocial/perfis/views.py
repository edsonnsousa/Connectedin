from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from perfis.models import Perfil, Convite
from django.shortcuts import redirect
from django.views.generic.base import View
# Create your views here.
from usuarios.forms import MudarSenhaForm


@login_required
def index(request):
	return render(request, 'index.html',{'perfis' : Perfil.objects.all(),
										 'perfil_logado' : get_perfil_logado(request)})

def exibir_perfil(request, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)

	return render(request, 'perfil.html',
		          {'perfil' : perfil, 
				   'perfil_logado' : get_perfil_logado(request)})

def convidar(request,perfil_id):

	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	
	if(perfil_logado.pode_convidar(perfil_a_convidar)):
		perfil_logado.convidar(perfil_a_convidar)
	
	return  redirect('index')

def get_perfil_logado(request):
	return Perfil.objects.get(usuario=request.user)

def aceitar(request, convite_id):
	convite = Convite.objects.get(id = convite_id)
	convite.aceitar()
	return redirect('index')

def recusar(request, convite_id):
	convite = Convite.objects.get(id = convite_id)
	convite.recusar()
	return redirect('index')

def desfazer_amizade(request, perfil_id):
	perfil = get_perfil_logado(request)
	perfil.desfazer_amizade(perfil_id)
	return redirect('index')

from django.shortcuts import render

@login_required
def mudar_senha(request):

	form = MudarSenhaForm(request.POST or None)
	if form.is_valid():
		if request.user.check_password(form.cleaned_data['senha_antiga']):
			request.user.set_password(form.cleaned_data['nova_senha'])
			request.user.save()
		return redirect('index')
	return render(request, 'mudar_senha.html', {'form':form})