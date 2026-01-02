from django.shortcuts import render

def home(request):
    """
    Vista principal del sitio (Home).
    Renderiza la plantilla de inicio.
    """
    context = {
        'title': 'AltoGasSpa - Expertos en Certificacion y Sello Verde',
    }
    return render(request, 'core/home.html', context)
