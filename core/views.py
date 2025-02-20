from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import OrcamentoForm,RegistroForm


class HomeView(FormView):
    template_name = "home.html"
    form_class = OrcamentoForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Orçamento enviado com sucesso!")
        return redirect("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["spotify_link"] = 'https://open.spotify.com/intl-pt/artist/6A4lS9s8nXm3dQZNjBDe24?si=JkB3BxcHQRKiKDxSQMh2Lw'
        return context

# Tela de Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('vlog')  # Redireciona se já estiver logado
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Página dos Vlogs (Apenas para usuários logados)
@method_decorator(login_required, name='dispatch')
class VlogView(TemplateView):
    template_name = 'vlog.html'


class RegistroView(FormView):
    template_name = "registro.html"
    form_class = RegistroForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        login(self.request, user)
        return redirect("home")  # Redireciona para a página inicial após o registro