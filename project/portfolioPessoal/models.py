from django.db import models

class Competencia(models.Model):
    nomeCompetencia = models.CharField(max_length=100)
    descricaoCompetencia = models.TextField()
    categoria = models.CharField(max_length=50)
    ucs = models.ManyToManyField('UnidadeCurricular', related_name='competencias_validas', blank=True)
    projetos = models.ManyToManyField('Projeto', related_name='competencias_validas', blank=True)
    tfcs = models.ManyToManyField('TFC', related_name='competencias_validas', blank=True)
    formacoes = models.ManyToManyField('Formacao', related_name='competencias_validas', blank=True)
    interesses = models.ManyToManyField('Interesse', related_name='competencias_validas', blank=True)
    tecnologias = models.ManyToManyField('Tecnologia', related_name='competencias_validas', blank=True)

    def __str__(self):
        return self.nomeCompetencia


class Docente(models.Model):
    idDocente = models.AutoField(primary_key=True)
    nomeDocente = models.CharField(max_length=150)
    linkPerfilUniversidade = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    tfcs_orientados = models.ManyToManyField('TFC', related_name='orientadores', blank=True)
    ucs_lecionadas = models.ManyToManyField('UnidadeCurricular', related_name='equipa_docente', blank=True)

    def __str__(self):
        return self.nomeDocente

class Tecnologia(models.Model):
    nomeTecnologia = models.CharField(max_length=100, primary_key=True)
    descricaoTecnologia = models.TextField()
    logotipo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    linkSite = models.URLField(blank=True, null=True)
    tipoTecnologia = models.CharField(max_length=50)
    classificacao = models.IntegerField()

    def __str__(self):
        return self.nomeTecnologia


class Licenciatura(models.Model):
    nomeCurso = models.CharField(max_length=200, primary_key=True)
    descricaoCurso = models.TextField()
    creditosCurso = models.IntegerField()
    duracao = models.CharField(max_length=50)
    formato = models.CharField(max_length=50)
    website = models.URLField(blank=True, null=True)
    faculdade = models.CharField(max_length=150)

    def __str__(self):
        return self.nomeCurso


class Formacao(models.Model):
    nomeFormacao = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=150)
    duracaoFormacao = models.CharField(max_length=50)

    def __str__(self):
        return self.nomeFormacao


class Interesse(models.Model):
    nomeInteresse = models.CharField(max_length=100, primary_key=True)
    descricaoInteresse = models.TextField()
    categoriaInteresse = models.CharField(max_length=50)

    def __str__(self):
        return self.nomeInteresse

class UnidadeCurricular(models.Model):
    idUC = models.CharField(max_length=20, primary_key=True)
    nomeUC = models.CharField(max_length=150)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    creditosUC = models.IntegerField()
    descricaoUC = models.TextField()
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    linkUC = models.URLField(blank=True, null=True)
    curso = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='ucs_onde_usada', blank=True)

    def __str__(self):
        return self.nomeUC


class TFC(models.Model):
    tituloTFC = models.CharField(max_length=200)
    descricaoTFC = models.TextField()
    autores = models.CharField(max_length=250)
    anoRealizacao = models.IntegerField()
    classificacaoTFC = models.IntegerField()
    linkTFC = models.URLField(blank=True, null=True)
    curso = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='tfcs')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='tfcs_onde_usada', blank=True)

    def __str__(self):
        return self.tituloTFC


class Projeto(models.Model):
    nomeProjeto = models.CharField(max_length=150)
    descricaoProjeto = models.TextField()
    anoRealizacao = models.IntegerField()
    linkGitHub = models.URLField(blank=True, null=True)
    fotoProjeto = models.ImageField(upload_to='projetos/', blank=True, null=True)
    linksVideo = models.URLField(blank=True, null=True) # Nome corrigido conforme fotos
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos_onde_usada', blank=True)

    def __str__(self):
        return self.nomeProjeto

class MakingOf(models.Model):
    etapas = models.CharField(max_length=100)
    registos = models.ImageField(upload_to='makingof/', blank=True, null=True)
    descricaoDecisoes = models.TextField()
    justificacaoDecisoes = models.TextField()
    errosEncontrados = models.TextField()
    solucao = models.TextField()
    usoIA = models.TextField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='makingof_logs')

    def __str__(self):
        return f"MakingOf - {self.projeto.nomeProjeto} ({self.etapas})"