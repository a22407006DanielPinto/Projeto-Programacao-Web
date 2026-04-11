from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Competencia, Tecnologia, Docente, Licenciatura, 
    Formacao, Interesse, UnidadeCurricular, TFC, 
    Projeto, MakingOf
)

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('idDocente', 'nomeDocente', 'email')
    search_fields = ('idDocente', 'nomeDocente', 'email')
    filter_horizontal = ('ucs_lecionadas',)

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('tituloTFC', 'curso', 'anoRealizacao')
    list_filter = ('curso', 'anoRealizacao')
    search_fields = ('tituloTFC', 'autores')
    filter_horizontal = ('tecnologias', 'orientadores')

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('exibir_imagem', 'idUC', 'nomeUC', 'get_cursos', 'ano', 'semestre', 'creditosUC')
    list_filter = ('cursos', 'ano', 'semestre')
    search_fields = ('idUC', 'nomeUC')
    filter_horizontal = ('cursos', 'tecnologias', 'competencias')

    def exibir_imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="height: 45px; width: auto; border-radius: 4px;" />', obj.imagem.url)
        return "Sem imagem"
    exibir_imagem.short_description = 'Imagem'

    def get_cursos(self, obj):
        return ", ".join([c.nomeCurso for c in obj.cursos.all()])
    get_cursos.short_description = 'Cursos'
    
    fieldsets = (
        ('Informação Geral', {
            'fields': ('idUC', 'nomeUC', 'cursos', 'ano', 'semestre', 'creditosUC', 'descricaoUC')
        }),
        ('Detalhes Académicos (API)', {
            'fields': ('objetivos', 'programa', 'metodologia', 'bibliografia', 'metodos_avaliacao'),
            'classes': ('collapse',),
        }),
        ('Media, Tecnologias e Competências', {
            'fields': ('imagem', 'linkUC', 'tecnologias', 'competencias')
        }),
    )

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nomeCompetencia', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nomeCompetencia',)
    filter_horizontal = ('tfcs', 'formacoes', 'interesses', 'tecnologias')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('exibir_logotipo', 'nomeTecnologia', 'tipoTecnologia', 'classificacao')
    list_filter = ('tipoTecnologia', 'classificacao')
    search_fields = ('nomeTecnologia',)

    def exibir_logotipo(self, obj):
        if obj.logotipo:
            return format_html('<img src="{}" style="height: 35px; width: auto; border-radius: 4px;" />', obj.logotipo.url)
        return "Sem logo"
    exibir_logotipo.short_description = 'Logo'

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nomeCurso', 'faculdade')
    search_fields = ('nomeCurso',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('exibir_foto', 'nomeProjeto', 'uc', 'anoRealizacao')
    filter_horizontal = ('tecnologias', 'competencias')

    def exibir_foto(self, obj):
        if obj.fotoProjeto:
            return format_html(
                '<img src="{}" style="height: 50px; width: auto; border-radius: 4px;" />', 
                obj.fotoProjeto.url
            )
        return "Sem imagem"
    
    exibir_foto.short_description = 'Imagem'

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('nomeFormacao', 'instituicao')

@admin.register(Interesse)
class InteresseAdmin(admin.ModelAdmin):
    list_display = ('nomeInteresse', 'categoriaInteresse')

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    fields = (
        'projeto', 
        'etapas', 
        'registos', 
        'descricaoDecisoes',  
        'errosEncontrados', 
        'solucao', 
        'justificacaoDecisoes',
        'usoIA'
    )
    
    list_display = ('projeto', 'etapas')
    list_filter = ('projeto',)