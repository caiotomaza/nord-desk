from django.db import models
from django.contrib.auth.models import User

class Chamado(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('em_andamento', 'Em Andamento'),
        ('fechado', 'Fechado'),
    ]
    
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    # Quem abriu o chamado
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chamados_criados')
    # Técnico responsável (pode ser nulo se ninguém pegou ainda)
    tecnico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='chamados_atribuidos')
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE_CHOICES, default='media')
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} - {self.titulo}"