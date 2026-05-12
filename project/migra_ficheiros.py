import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.core.files import File
from portfolioPessoal.models import Projeto, Tecnologia, MakingOf

# Migrar fotos de projetos
for obj in Projeto.objects.all():
    if obj.fotoProjeto and obj.fotoProjeto.name:
        local_path = os.path.join('media', obj.fotoProjeto.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.fotoProjeto.save(os.path.basename(local_path), File(f), save=True)
                print(f"Migrado projeto: {obj.nomeProjeto}")

# Migrar logotipos de tecnologias
for obj in Tecnologia.objects.all():
    if obj.logotipo and obj.logotipo.name:
        local_path = os.path.join('media', obj.logotipo.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.logotipo.save(os.path.basename(local_path), File(f), save=True)
                print(f"Migrado tecnologia: {obj.nomeTecnologia}")

# Migrar imagens de makingof
for obj in MakingOf.objects.all():
    if obj.registos and obj.registos.name:
        local_path = os.path.join('media', obj.registos.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.registos.save(os.path.basename(local_path), File(f), save=True)
                print(f"Migrado makingof: {obj.etapas}")

print("Migração concluída!")