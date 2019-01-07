from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, null= False)
    nome_empresa = models.CharField(max_length=255, null=False)
    #email = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('Perfil')

    usuario = models.OneToOneField(User, related_name="perfil", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    @property
    def email(self):
        return self.usuario.email

    def pode_convidar(self, perfil_convidado):
        if not perfil_convidado==self:
            convite = Convite(solicitante=self,convidado = perfil_convidado)
            convite.save()
            
    def desfazer_amizade(self,perfil_id):
        self.contatos.remove(perfil_id)
            
class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='convites_feitos' )
    convidado = models.ForeignKey(Perfil, on_delete= models.CASCADE, related_name='convites_recebidos')

    def aceitar(self):        
        self.solicitante.contatos.add(self.convidado)
        self.convidado.contatos.add(self.solicitante)
        self.delete()
        
    def recusar(self):
        self.delete()
