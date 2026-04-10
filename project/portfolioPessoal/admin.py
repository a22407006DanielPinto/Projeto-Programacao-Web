from django.contrib import admin
from .models import (
    Competencia, Tecnologia, Docente, Licenciatura, 
    Formacao, Interesse, UnidadeCurricular, TFC, 
    Projeto, MakingOf
)

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nomeCompetencia', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nomeCompetencia', 'descricaoCompetencia')
    filter_horizontal = ('ucs', 'projetos', 'tfcs', 'formacoes', 'interesses', 'tecnologias')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nomeDocente', 'email', 'linkPerfilUniversidade')
    search_fields = ('nomeDocente', 'email')
    filter_horizontal = ('tfcs_orientados', 'ucs_lecionadas')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nomeTecnologia', 'tipoTecnologia', 'classificacao')
    list_filter = ('tipoTecnologia', 'classificacao')
    search_fields = ('nomeTecnologia',)

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nomeCurso', 'faculdade', 'duracao', 'formato')
    list_filter = ('faculdade', 'formato')
    search_fields = ('nomeCurso',)

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('nomeFormacao', 'instituicao', 'duracaoFormacao')
    search_fields = ('nomeFormacao', 'instituicao')

@admin.register(Interesse)
class InteresseAdmin(admin.ModelAdmin):
    list_display = ('nomeInteresse', 'categoriaInteresse')
    list_filter = ('categoriaInteresse',)
    search_fields = ('nomeInteresse',)

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('idUC', 'nomeUC', 'curso', 'ano', 'semestre', 'creditosUC')
    list_filter = ('curso', 'ano', 'semestre')
    search_fields = ('idUC', 'nomeUC')
    filter_horizontal = ('tecnologias',)
    fieldsets = (
        ('Informação Geral', {
            'fields': ('idUC', 'nomeUC', 'curso', 'ano', 'semestre', 'creditosUC', 'descricaoUC')
        }),
        ('Detalhes Académicos (API)', {
            'fields': ('objetivos', 'programa', 'metodologia', 'bibliografia', 'metodos_avaliacao'),
            'classes': ('collapse',),
        }),
        ('Media e Links', {
            'fields': ('imagem', 'linkUC', 'tecnologias')
        }),
    )

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('tituloTFC', 'curso', 'anoRealizacao', 'classificacaoTFC')
    list_filter = ('curso', 'anoRealizacao')
    search_fields = ('tituloTFC', 'autores')
    filter_horizontal = ('tecnologias',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nomeProjeto', 'uc', 'anoRealizacao')
    list_filter = ('anoRealizacao', 'uc')
    search_fields = ('nomeProjeto', 'descricaoProjeto')
    filter_horizontal = ('tecnologias',)

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'etapas', 'usoIA')
    list_filter = ('projeto',)
    search_fields = ('etapas', 'descricaoDecisoes', 'errosEncontrados')