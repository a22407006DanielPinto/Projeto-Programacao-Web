import os
import sys
import json
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DJANGO_DIR = os.path.join(BASE_DIR, "project")

sys.path.append(DJANGO_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolioPessoal.models import TFC, Licenciatura, Docente

ficheiro_json = os.path.join(BASE_DIR, "data", "tfcs_2025.json")

if not os.path.isfile(ficheiro_json):
    print(f"Erro: Ficheiro não encontrado em {ficheiro_json}")
    sys.exit(1)

with open(ficheiro_json, "r", encoding="utf-8") as file:
    registos = json.load(file)

lic, _ = Licenciatura.objects.get_or_create(
    nomeCurso="Engenharia Informática",
    defaults={
        "descricaoCurso": "Licenciatura em Engenharia Informática",
        "creditosCurso": 180,
        "faculdade": "ECATI",
        "duracao": "3 anos",
        "formato": "Presencial"
    }
)

novos = 0

for reg in registos:
    titulo = reg.get("titulo")
    if not titulo:
        continue

    tfc_obj, is_new = TFC.objects.get_or_create(
        tituloTFC=titulo,
        defaults={
            "autores": reg.get("autor", "Desconhecido"),
            "descricaoTFC": reg.get("resumo", "Sem resumo"),
            "anoRealizacao": 2025,
            "classificacaoTFC": reg.get("rating", 0),
            "linkTFC": reg.get("email", ""),
            "curso": lic
        }
    )

    orientadores_raw = reg.get("orientador", "")
    if orientadores_raw:
        lista_nomes = [n.strip() for n in orientadores_raw.split(";") if n.strip()]

        for nome_doc in lista_nomes:
            docente_obj, _ = Docente.objects.get_or_create(
                nomeDocente=nome_doc
            )
            docente_obj.tfcs_orientados.add(tfc_obj)

    if is_new:
        novos += 1
        print(f"[NOVO] {titulo}")
    else:
        print(f"[EXISTENTE] {titulo}")

print(f"\nFeito! Adicionados {novos} novos registos à base de dados.")