def gestor_context(request):
    is_gestor = (
        request.user.is_authenticated and
        request.user.groups.filter(name='gestor-portfolio').exists()
    )
    return {'is_gestor_global': is_gestor}