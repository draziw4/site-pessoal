from django import forms
from .models import Orcamento
from django.contrib.auth.models import User

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['nome_completo', 'nome_artistico', 'cidade_estado', 'email', 'instagram', 'whatsapp', 'genero_musical', 'beat_exclusivo', 'composicao', 'captacao_voz', 'mixagem_masterizacao', 'identidade_visual', 'mensagem']

    beat_exclusivo = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-checkbox h-5 w-5 text-green-400'}), required=False)
    composicao = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-checkbox h-5 w-5 text-green-400'}), required=False)
    captacao_voz = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-checkbox h-5 w-5 text-green-400'}), required=False)
    mixagem_masterizacao = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-checkbox h-5 w-5 text-green-400'}), required=False)
    identidade_visual = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-checkbox h-5 w-5 text-green-400'}), required=False)


from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirme a senha")

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "As senhas não coincidem.")

        return cleaned_data
