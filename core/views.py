from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def home(request):
    services = [
        {
            'title': "Certificación Sello Verde",
            'icon': "flame", # Nombre del icono de Lucide
            'desc': "Gestión independiente para edificios y hogares. Detección de fugas con ultrasonido y reparación inmediata.",
            'border_color': "border-orange-500",
            'icon_color': "text-orange-600",
            'bg_color': "bg-orange-100"
        },
        {
            'title': "Trámites SEC (TC6)",
            'icon': "file-text",
            'desc': "Recepción final, declaraciones TC5, TC2 y TC7. Nos encargamos de toda la burocracia administrativa.",
            'border_color': "border-blue-600",
            'icon_color': "text-blue-600",
            'bg_color': "bg-blue-100"
        },
        {
            'title': "Proyectos de Ingeniería",
            'icon': "ruler",
            'desc': "Memorias de cálculo para cañerías, dimensionamiento de cilindros y estanques. Planos GN y GL.",
            'border_color': "border-slate-700",
            'icon_color': "text-slate-700",
            'bg_color': "bg-slate-100"
        }
    ]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje_cliente = form.cleaned_data['mensaje']

            cuerpo_correo = f"Nuevo contacto de: {nombre}\nTelefono: {telefono}\nEmail: {email}\n\nMensaje:\n{mensaje_cliente}"
            
            send_mail(
                subject="Nuevo Lead Web: {nombre}",
                message=cuerpo_correo,
                from_email='web@altogasspa.cl',
                recipient_list=['Altogasspa@gmail.com'],
                fail_silently=False,
            )

            message_success = "¡Gracias por contactarnos! Nos pondremos en contacto contigo pronto."

            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'title': 'Alto Gas SPA - Expertos en Certificación',
        'services': services,
        'form': form,
    }
    return render(request, 'core/home.html', context)