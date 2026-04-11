from django.db import models

class Competencia(models.Model):
    nomeCompetencia = models.CharField(max_length=100)
    descricaoCompetencia = models.TextField()
    categoria = models.CharField(max_length=50)
    tfcs = models.ManyToManyField('TFC', related_name='competencias_validas', blank=True)
    formacoes = models.ManyToManyField('Formacao', related_name='competencias_validas', blank=True)
    interesses = models.ManyToManyField('Interesse', related_name='competencias_validas', blank=True)
    tecnologias = models.ManyToManyField('Tecnologia', related_name='competencias_validas', blank=True)

    class Meta:
        verbose_name = "Competência"
        verbose_name_plural = "Competências"

    def __str__(self):
        return self.nomeCompetencia

class Docente(models.Model):
    idDocente = models.CharField(max_length=50, primary_key=True)
    nomeDocente = models.CharField(max_length=150)
    linkPerfilUniversidade = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    ucs_lecionadas = models.ManyToManyField('UnidadeCurricular', related_name='equipa_docente', blank=True)

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return f"{self.idDocente} - {self.nomeDocente}"

class Tecnologia(models.Model):
    nomeTecnologia = models.CharField(max_length=100, primary_key=True)
    descricaoTecnologia = models.TextField()
    logotipo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    linkSite = models.URLField(blank=True, null=True)
    tipoTecnologia = models.CharField(max_length=50)
    classificacao = models.IntegerField()

    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"

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

    class Meta:
        verbose_name = "Licenciatura"
        verbose_name_plural = "Licenciaturas"

    def __str__(self):
        return self.nomeCurso

class UnidadeCurricular(models.Model):
    idUC = models.CharField(max_length=20, primary_key=True)
    nomeUC = models.CharField(max_length=150)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    creditosUC = models.IntegerField()
    descricaoUC = models.TextField(null=True, blank=True)
    objetivos = models.TextField(null=True, blank=True)
    programa = models.TextField(null=True, blank=True)
    metodologia = models.TextField(null=True, blank=True)
    bibliografia = models.TextField(null=True, blank=True)
    metodos_avaliacao = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    linkUC = models.URLField(blank=True, null=True)
    curso = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='unidades_curriculares')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='ucs_onde_usada', blank=True)
    competencias = models.ManyToManyField(Competencia, related_name='ucs_associadas', blank=True)

    class Meta:
        verbose_name = "Unidade Curricular"
        verbose_name_plural = "Unidades Curriculares"

    def __str__(self):
        return f"{self.idUC} - {self.nomeUC}"

class TFC(models.Model):
    tituloTFC = models.CharField(max_length=200)
    descricaoTFC = models.TextField()
    autores = models.CharField(max_length=250)
    anoRealizacao = models.IntegerField()
    classificacaoTFC = models.IntegerField()
    linkTFC = models.URLField(blank=True, null=True)
    orientadores = models.ManyToManyField(Docente, related_name='tfcs_orientados', blank=True)
    curso = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='tfcs')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='tfcs_onde_usada', blank=True)

    class Meta:
        verbose_name = "TFC"
        verbose_name_plural = "TFCs"

    def __str__(self):
        return self.tituloTFC

class Projeto(models.Model):
    nomeProjeto = models.CharField(max_length=150)
    descricaoProjeto = models.TextField()
    anoRealizacao = models.IntegerField()
    linkGitHub = models.URLField(blank=True, null=True)
    fotoProjeto = models.ImageField(upload_to='projetos/', blank=True, null=True)
    linksVideo = models.URLField(blank=True, null=True)
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos_onde_usada', blank=True)
    competencias = models.ManyToManyField(Competencia, related_name='projetos_associados', blank=True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.nomeProjeto

class Formacao(models.Model):
    nomeFormacao = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=150)
    duracaoFormacao = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Formação"
        verbose_name_plural = "Formações"

    def __str__(self):
        return self.nomeFormacao

class Interesse(models.Model):
    nomeInteresse = models.CharField(max_length=100, primary_key=True)
    descricaoInteresse = models.TextField()
    categoriaInteresse = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Interesse"
        verbose_name_plural = "Interesses"

    def __str__(self):
        return self.nomeInteresse

class MakingOf(models.Model):
    etapas = models.CharField(max_length=100)
    registos = models.FileField(upload_to='makingof/', blank=True, null=True)
    descricaoDecisoes = models.TextField()
    justificacaoDecisoes = models.TextField()
    errosEncontrados = models.TextField()
    solucao = models.TextField()
    usoIA = models.TextField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='makingof_logs')

    class Meta:
        verbose_name = "Making Of"
        verbose_name_plural = "Making Ofs"

    def __str__(self):
        return f"MakingOf - {self.projeto.nomeProjeto} ({self.etapas})"