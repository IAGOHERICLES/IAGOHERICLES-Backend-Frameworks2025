from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

class Todo(models.Model):
    title = models.CharField(verbose_name="Título" ,max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(verbose_name="Data de Entrega" ,null=False, blank=False)
    finished_at = models.DateTimeField(null=True, blank=True)

    # 1. CLASSE META CORRIGIDA (Indentada para dentro da classe Todo)
    class Meta:
        ordering = ["deadline"]

    # 2. MÉTODO CORRIGIDO (Indentado para dentro da classe Todo)
    def mark_has_complete(self):
        # A lógica do método também é indentada
        if not self.finished_at:
            self.finished_at = timezone.now()
            self.save()

class ContatoComentario(models.Model):
    # O usuário que deixou o comentário (pode ser anônimo)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    
    # O conteúdo do comentário/mensagem
    mensagem = models.TextField()
    
    # Data em que o comentário foi criado
    data_envio = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Comentário de Contato"
        verbose_name_plural = "Comentários de Contato"
        # Ordem: os mais recentes aparecem primeiro
        ordering = ['-data_envio'] 

    def __str__(self):
        return f'Mensagem de {self.nome} ({self.email})'