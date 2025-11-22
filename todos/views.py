from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render ,get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.urls import reverse_lazy
from .models import Todo
from .forms import CustomUserCreationForm,TodoForm,ComentarioForm
from django.contrib import messages
from django.urls import reverse
from .models import ContatoComentario


class TodoListView(LoginRequiredMixin,ListView):
    model = Todo
     

class TodoCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo-list")
    labels = {
        'title': 'Nome e Raça do Pet',
        'deadline': 'Data do Banho',}
   

class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = Todo
    fields = ["title","deadline"]
    success_url = reverse_lazy("todo-list")

class TodoDeleteView(LoginRequiredMixin,DeleteView):
    model = Todo
    success_url = reverse_lazy("todo-list")


class TodoCompleteView(LoginRequiredMixin,View):
    def post (self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo-list")

class DicasView(LoginRequiredMixin,TemplateView):
    template_name = "todos/dicas.html"

class NoticiasView(LoginRequiredMixin,TemplateView):
    template_name = "todos/noticias.html"

class ContatoView(LoginRequiredMixin,TemplateView):
    template_name = "todos/contato.html"    


def cadastro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Salva o novo usuário no banco de dados
            user = form.save()
            
            # Opcional: Logar o usuário automaticamente após o cadastro (opcional)
            # from django.contrib.auth import login
            # login(request, user) 

            messages.success(request, "Cadastro realizado com sucesso! Você já pode entrar.")
            # Redireciona para a página de login
            return redirect(reverse('login')) 
        else:
            # Se houver erro (ex: nome de usuário já existe)
            messages.error(request, "Erro no cadastro. Verifique os campos e tente novamente.")
    else:
        # Se for um GET, exibe o formulário vazio
        form = CustomUserCreationForm()
        
    context = {'form': form, 'page_title': 'Cadastro'}
    return render(request, 'registration/cadastro.html', context)

def cadastro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Cadastro realizado com sucesso! Você já pode entrar.")
            return redirect(reverse('login'))
        else:
            messages.error(request, "Erro no cadastro. Verifique os campos e tente novamente.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/cadastro.html', {'form': form, 'page_title': 'Cadastro'})

class AdminOnlyMixin(UserPassesTestMixin):
    """Mixin que permite acesso apenas a usuários que são staff (admin)."""
    def test_func(self):
        # Retorna True apenas se o usuário for superusuário OU membro da equipe
        return self.request.user.is_staff



class AdminOnlyMixin(UserPassesTestMixin):
    """Mixin que permite acesso apenas a usuários que são staff (admin)."""
    def test_func(self):
        # O critério é ser um usuário 'is_staff' (membro da equipe/admin)
        return self.request.user.is_staff

class ComentariosListView(AdminOnlyMixin, LoginRequiredMixin, ListView):
    model = ContatoComentario
    template_name = 'todos/admin_comentarios_list.html'
    context_object_name = 'comentarios'

    # Opcional: Ordenar os comentários por data de envio (do mais recente para o mais antigo)
    def get_queryset(self):
        # Assumindo que o seu modelo ContatoComentario tem um campo 'data_envio'
        return ContatoComentario.objects.all().order_by('-data_envio')
    


