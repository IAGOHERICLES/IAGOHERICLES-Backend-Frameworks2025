from django.contrib import admin
from .models import Todo, GuiaDica, ContatoComentario # Importe Guia e dicas
# Register your models here.

#Registra o novo modelo de Guia/Dica
@admin.register(GuiaDica)
class GuiaDicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'criado_em')
    search_fields = ('titulo', 'descricao')
    list_filter = ('tipo', 'criado_em')
