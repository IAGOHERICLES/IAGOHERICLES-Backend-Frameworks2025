

from django import forms
from django.contrib.auth.forms import UserCreationForm # Importa o formulário padrão
from django.contrib.auth.models import User
from .models import Todo, ContatoComentario


# O formulário que será usado para o cadastro
class CustomUserCreationForm(UserCreationForm):
    # Campos que você quer incluir no cadastro, além dos padrões (username, password)
    # Por exemplo, você pode adicionar o campo de e-mail como obrigatório
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        # Usa o modelo de usuário padrão do Django
        model = User
        # Define a ordem dos campos no formulário
        fields = ('username', 'email') + UserCreationForm.Meta.fields[2:]
        # O UserCreationForm.Meta.fields[2:] garante que os campos de senha apareçam no final.

# 2. Formulário de Tarefas (Para a TodoCreateView)
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'deadline']
        
        # DEFINIMOS OS RÓTULOS (labels) CORRETOS AQUI
        labels = {
            'title': 'Nome e Raça', # <-- Alteração solicitada
            'deadline': 'Data e Hora da Entrega',
        }
        
        # Adicionar classes Bootstrap (se necessário)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }



class ComentarioForm(forms.ModelForm):
    class Meta:
        model = ContatoComentario
        # Inclui todos os campos necessários para o formulário de contato
        fields = ['nome', 'email', 'mensagem'] 
        
        # Define os widgets e as classes CSS do Bootstrap
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Iago'
                # **GARANTIA:** Não há 'disabled=True' ou 'readonly=True' aqui
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu.email@exemplo.com'
                # **GARANTIA:** Não há 'disabled=True' ou 'readonly=True' aqui
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4, 
                'placeholder': 'Digite sua sugestão ou reclamação aqui...'
                # **GARANTIA:** Não há 'disabled=True' ou 'readonly=True' aqui
            }),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = ContatoComentario
        fields = ['nome', 'email', 'mensagem'] 
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Iago'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu.email@exemplo.com'
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4, 
                'placeholder': 'Digite sua sugestão ou reclamação aqui...'
            }),
            # IMPORTANTE: Se você tiver um '__init__' no forms.py, remova qualquer
            # código que defina 'self.fields['campo'].widget.attrs['readonly'] = True'
        }