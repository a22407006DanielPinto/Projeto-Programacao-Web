from django.db import models

class Competencia(models.Model):
    nomeCompetencia = models.CharField(max_length=100, verbose_name="Competência")
    descricaoCompetencia = models.TextField(verbose_name="Descrição")
    categoria = models.CharField(max_length=50, verbose_name="Categoria")
    tfcs = models.ManyToManyField('TFC', related_name='competencias_validas', blank=True, verbose_name="TFCs Associados")
    formacoes = models.ManyToManyField('Formacao', related_name='competencias_validas', blank=True, verbose_name="Formações Relacionadas")
    interesses = models.ManyToManyField('Interesse', related_name='competencias_validas', blank=True, verbose_name="Interesses Relacionados")
    tecnologias = models.ManyToManyField('Tecnologia', related_name='competencias_validas', blank=True, verbose_name="Tecnologias Utilizadas")

    class Meta:
        verbose_name = "Competência"
        verbose_name_plural = "Competências"

    def __str__(self):
        return self.nomeCompetencia

class Docente(models.Model):
    idDocente = models.CharField(max_length=50, primary_key=True, verbose_name="Docente ID")
    nomeDocente = models.CharField(max_length=150, verbose_name="Nome do Docente")
    linkPerfilUniversidade = models.URLField(blank=True, null=True, verbose_name="Link do Perfil Universitário")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    ucs_lecionadas = models.ManyToManyField('UnidadeCurricular', related_name='equipa_docente', blank=True, verbose_name="UCs Lecionadas")

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return f"{self.idDocente} - {self.nomeDocente}"

class Tecnologia(models.Model):
    nomeTecnologia = models.CharField(max_length=100, primary_key=True, verbose_name="Nome da Tecnologia")
    descricaoTecnologia = models.TextField(verbose_name="Descrição")
    logotipo = models.ImageField(upload_to='tecnologias/', blank=True, null=True, verbose_name="Logotipo")
    linkSite = models.URLField(blank=True, null=True, verbose_name="Link do Site Oficial")
    tipoTecnologia = models.CharField(max_length=50, verbose_name="Tipo de Tecnologia")
    classificacao = models.IntegerField(verbose_name="Classificação")

    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"

    def __str__(self):
        return self.nomeTecnologia

class Licenciatura(models.Model):
    nomeCurso = models.CharField(max_length=200, primary_key=True, verbose_name="Curso")
    descricaoCurso = models.TextField(verbose_name="Descrição do Curso")
    creditosCurso = models.IntegerField(verbose_name="Créditos (ECTS)")
    duracao = models.CharField(max_length=50, verbose_name="Duração")
    formato = models.CharField(max_length=50, verbose_name="Formato de Ensino")
    website = models.URLField(blank=True, null=True, verbose_name="Website do Curso")
    faculdade = models.CharField(max_length=150, verbose_name="Faculdade")

    class Meta:
        verbose_name = "Licenciatura"
        verbose_name_plural = "Licenciaturas"

    def __str__(self):
        return self.nomeCurso

class UnidadeCurricular(models.Model):
    idUC = models.CharField(max_length=20, primary_key=True, verbose_name="Unidade Curricular ID")
    nomeUC = models.CharField(max_length=150, verbose_name="Nome da UC")
    ano = models.IntegerField(verbose_name="Ano Curricular")
    semestre = models.IntegerField(verbose_name="Semestre")
    creditosUC = models.IntegerField(verbose_name="Créditos (ECTS)")
    descricaoUC = models.TextField(null=True, blank=True, verbose_name="Descrição da UC")
    objetivos = models.TextField(null=True, blank=True, verbose_name="Objetivos")
    programa = models.TextField(null=True, blank=True, verbose_name="Programa")
    metodologia = models.TextField(null=True, blank=True, verbose_name="Metodologia")
    bibliografia = models.TextField(null=True, blank=True, verbose_name="Bibliografia")
    metodos_avaliacao = models.TextField(null=True, blank=True, verbose_name="Métodos de Avaliação")
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True, verbose_name="Imagem da UC")
    linkUC = models.URLField(blank=True, null=True, verbose_name="Link da UC")
    cursos = models.ManyToManyField(Licenciatura, related_name='unidades_curriculares', blank=True, verbose_name="Cursos")
    tecnologias = models.ManyToManyField(Tecnologia, related_name='ucs_onde_usada', blank=True, verbose_name="Tecnologias Envolvidas")
    competencias = models.ManyToManyField(Competencia, related_name='ucs_associadas', blank=True, verbose_name="Competências Adquiridas")

    class Meta:
        verbose_name = "Unidade Curricular"
        verbose_name_plural = "Unidades Curriculares"

    def __str__(self):
        return f"{self.idUC} - {self.nomeUC}"

class TFC(models.Model):
    tituloTFC = models.CharField(max_length=200, verbose_name="Título do TFC")
    descricaoTFC = models.TextField(verbose_name="Descrição do Trabalho")
    autores = models.CharField(max_length=250, verbose_name="Autores")
    anoRealizacao = models.IntegerField(verbose_name="Ano de Realização")
    classificacaoTFC = models.IntegerField(verbose_name="Classificação Final")
    linkTFC = models.URLField(blank=True, null=True, verbose_name="Link do Trabalho")
    orientadores = models.ManyToManyField(Docente, related_name='tfcs_orientados', blank=True, verbose_name="Orientadores")
    curso = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='tfcs', verbose_name="Curso")
    tecnologias = models.ManyToManyField(Tecnologia, related_name='tfcs_onde_usada', blank=True, verbose_name="Tecnologias Utilizadas")

    class Meta:
        verbose_name = "TFC"
        verbose_name_plural = "TFCs"

    def __str__(self):
        return self.tituloTFC

class Projeto(models.Model):
    nomeProjeto = models.CharField(max_length=150, verbose_name="Nome do Projeto")
    descricaoProjeto = models.TextField(verbose_name="Descrição")
    anoRealizacao = models.IntegerField(verbose_name="Ano de Realização")
    linkGitHub = models.URLField(blank=True, null=True, verbose_name="Link do GitHub")
    fotoProjeto = models.ImageField(upload_to='projetos/', blank=True, null=True, verbose_name="Foto do Projeto")
    linksVideo = models.URLField(blank=True, null=True, verbose_name="Link do Vídeo")
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos', verbose_name="Unidade Curricular")
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos_onde_usada', blank=True, verbose_name="Tecnologias Aplicadas")
    competencias = models.ManyToManyField(Competencia, related_name='projetos_associados', blank=True, verbose_name="Competências Demonstradas")

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.nomeProjeto

class Formacao(models.Model):
    nomeFormacao = models.CharField(max_length=150, verbose_name="Nome da Formação")
    instituicao = models.CharField(max_length=150, verbose_name="Instituição")
    duracaoFormacao = models.CharField(max_length=50, verbose_name="Duração")

    class Meta:
        verbose_name = "Formação"
        verbose_name_plural = "Formações"

    def __str__(self):
        return self.nomeFormacao

class Interesse(models.Model):
    nomeInteresse = models.CharField(max_length=100, primary_key=True, verbose_name="Nome do Interesse")
    descricaoInteresse = models.TextField(verbose_name="Descrição")
    categoriaInteresse = models.CharField(max_length=50, verbose_name="Categoria")

    class Meta:
        verbose_name = "Interesse"
        verbose_name_plural = "Interesses"

    def __str__(self):
        return self.nomeInteresse

class MakingOf(models.Model):
    etapas = models.CharField(max_length=100, verbose_name="Etapas do Processo")
    registos = models.FileField(upload_to='makingof/', blank=True, null=True, verbose_name="Ficheiros de Registo")
    descricaoDecisoes = models.TextField(verbose_name="Descrição das Decisões")
    justificacaoDecisoes = models.TextField(verbose_name="Justificação das Decisões")
    errosEncontrados = models.TextField(verbose_name="Erros Encontrados")
    solucao = models.TextField(verbose_name="Solução Aplicada")
    usoIA = models.TextField(verbose_name="Uso de Inteligência Artificial")
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='makingof_logs', verbose_name="Projeto Relacionado")

    class Meta:
        verbose_name = "Making Of"
        verbose_name_plural = "Making Ofs"

    def __str__(self):
        return f"MakingOf - {self.projeto.nomeProjeto} ({self.etapas})"