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
    list_display = ('idUC', 'nomeUC', 'curso', 'ano', 'semestre', 'creditosUC')
    list_filter = ('curso', 'ano', 'semestre')
    search_fields = ('idUC', 'nomeUC')
    filter_horizontal = ('tecnologias', 'competencias')
    
    fieldsets = (
        ('Informação Geral', {
            'fields': ('idUC', 'nomeUC', 'curso', 'ano', 'semestre', 'creditosUC', 'descricaoUC')
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
    list_display = ('nomeTecnologia', 'tipoTecnologia', 'classificacao')
    list_filter = ('tipoTecnologia', 'classificacao')
    search_fields = ('nomeTecnologia',)

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nomeCurso', 'faculdade')
    search_fields = ('nomeCurso',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nomeProjeto', 'uc', 'anoRealizacao')
    list_filter = ('anoRealizacao', 'uc')
    search_fields = ('nomeProjeto', 'descricaoProjeto')
    filter_horizontal = ('tecnologias', 'competencias')

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('nomeFormacao', 'instituicao')

@admin.register(Interesse)
class InteresseAdmin(admin.ModelAdmin):
    list_display = ('nomeInteresse', 'categoriaInteresse')

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'etapas')