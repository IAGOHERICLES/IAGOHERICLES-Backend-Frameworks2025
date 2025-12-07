# todos/urls.py
from django.urls import include
from django.urls import path
from .views import (
    TodoListView, 
    TodoCreateView, 
    TodoUpdateView, 
    TodoDeleteView,
    TodoCompleteView,
    DicasListView,
    NoticiasView,
    ContatoView,
    cadastro_view,
    ComentariosListView,
)


urlpatterns = [
    # Autenticação padrão do Django (login, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    path('cadastro/', cadastro_view, name='cadastro'),

    ## Rota de Tarefas (Fila de Banho)
    # Lista de Tarefas (ex: /)
    path("", TodoListView.as_view(), name="todo-list"), 
    # Criação de Tarefas (ex: /create)
    path("create/", TodoCreateView.as_view(), name="todo-create"),
    # Atualização de Tarefas (ex: /update/5)
    path("update/<int:pk>/", TodoUpdateView.as_view(), name="todo-update"),
    # Exclusão de Tarefas (ex: /delete/5)
    path("delete/<int:pk>/", TodoDeleteView.as_view(), name="todo-delete"),
    # Conclusão de Tarefas (ex: /complete/5)
    path("complete/<int:pk>/", TodoCompleteView.as_view(), name="todo-complete"),
    
    ## Rotas do Site (Dicas, Notícias e Contato)
    path("Dicas/", DicasListView.as_view(), name="dicas"),
    path("noticias/", NoticiasView.as_view(), name="noticias"),
    path("contato/", ContatoView.as_view(), name="contato"),

    # Rotas administrativas para comentários e sugestões
    path('comentarios/', ComentariosListView.as_view(), name='admin-comentarios'),
    path('sugestoes/', ComentariosListView.as_view(), name='admin-comentarios'),
]

