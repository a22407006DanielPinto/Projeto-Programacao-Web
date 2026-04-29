from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao, TFC, Interesse

# FORMULÁRIO DE PROJETO
class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = [
            'nomeProjeto', 'descricaoProjeto', 'anoRealizacao', 
            'linkGitHub', 'fotoProjeto', 'linksVideo', 
            'uc', 'tecnologias', 'competencias'
        ]
        widgets = {
            'descricaoProjeto': forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),
            'anoRealizacao': forms.NumberInput(attrs={'class': 'form-input'}),
            # Estes campos vão ser transformados em dropdowns com tags
            'tecnologias': forms.CheckboxSelectMultiple(),
            'competencias': forms.CheckboxSelectMultiple(),
        }

# FORMULÁRIO DE TECNOLOGIA (Corrigido e único)
class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'
        widgets = {
            'nomeTecnologia': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Django'}),
            'descricaoTecnologia': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'linkSite': forms.URLInput(attrs={'class': 'form-input'}),
            'tipoTecnologia': forms.TextInput(attrs={'class': 'form-input'}),
            'classificacao': forms.NumberInput(attrs={
                'class': 'form-input', 
                'min': '0', 
                'max': '5', 
                'step': '1',
            }),
        }

# FORMULÁRIO DE COMPETÊNCIA
class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'
        widgets = {
            'nomeCompetencia': forms.TextInput(attrs={'class': 'form-input'}),
            'descricaoCompetencia': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            # Transformar as listas gigantes (TFCs, etc) em dropdowns com tags
            'tfcs': forms.CheckboxSelectMultiple(),
            'formacoes': forms.CheckboxSelectMultiple(),
            'interesses': forms.CheckboxSelectMultiple(),
            'tecnologias': forms.CheckboxSelectMultiple(),
        }

# FORMULÁRIO DE FORMAÇÃO
class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'
        widgets = {
            'curso': forms.TextInput(attrs={'class': 'form-input'}),
            'instituicao': forms.TextInput(attrs={'class': 'form-input'}),
            'ano_conclusao': forms.NumberInput(attrs={'class': 'form-input'}),
            'descricao': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }