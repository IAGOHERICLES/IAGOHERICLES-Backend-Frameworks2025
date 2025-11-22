from django.contrib import admin
from django.urls import path, include  # Adicione 'include'

# Não precisa importar a função 'home' aqui, pois você vai usar o 'include'
# from todos.views import home

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     # Inclui todas as rotas definidas no arquivo todos/urls.py
#     path("", include("todos.urls")),
# ]
