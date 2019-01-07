from django import forms
from django.contrib.auth.models import User


class RegistrarUsuarioForm(forms.Form):
    nome=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    senha=forms.CharField(required=True)
    telefone=forms.CharField(required=True)
    nome_empresa=forms.CharField(required=True)
    # def is_valid(self):
    #     valid=True
    #     if not super(RegistrarUsuarioForm,self).is_valid():
    #         self.adiciona_erro('Favor,verifique seus dados')
    #         valid=False
    #
    #     user_exists =User.objects.filter(username=self.cleaned_data['nome']).exists()
    #     if user_exists:
    #         self.adiciona_erro('Usuario já existe.')
    #         valid=False
    #
    #     return valid
    # def adiciona_erro(self, message):
    #     errors = self._erros.setdefault(forms.forms.NON_FIELD_ERRORS,
    #                                forms.utils.ErroList())
    #     errors.append(message)
class MudarSenhaForm(forms.Form):
    senha_antiga = forms.CharField(widget=forms.PasswordInput())
    nova_senha = forms.CharField(widget=forms.PasswordInput())
    confirma_senha = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        if self.cleaned_data['nova_senha'] != self.cleaned_data['confirma_senha']:
            raise forms.ValidationError('Senha de confirmacao não são iguais')
        else:
            return self.cleaned_data