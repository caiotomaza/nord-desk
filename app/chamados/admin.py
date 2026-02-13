from django.contrib import admin
from .models import Chamado

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    # Colunas que aparecem na lista
    list_display = ('id', 'titulo', 'solicitante', 'status', 'prioridade', 'criado_em')
    
    # Filtros laterais (barra direita)
    list_filter = ('status', 'prioridade', 'criado_em')
    
    # Campo de busca (topo da página)
    search_fields = ('titulo', 'descricao')
    
    # Campos que não podem ser editados (apenas leitura)
    readonly_fields = ('criado_em', 'atualizado_em')