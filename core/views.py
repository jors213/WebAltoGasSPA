from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .models import Contacto  # <--- IMPORTANTE: Importamos el modelo nuevo

def home(request):
    services = [
        {
            'title': "INSPECCIÓN Y SELLO VERDE",
            'icon': "check-circle-2",
            'desc': "Certificación oficial para edificios, hogares y locales. Realizamos la inspección periódica y gestionamos tu Sello Verde ante la SEC.",
            'border_color': "border-green-600",
            'icon_color': "text-green-600",
            'bg_color': "bg-green-100"
        },
        {
            'title': "DECLARACIÓN Y TRÁMITES SEC",
            'icon': "file-signature",
            'desc': "Regularizamos tus instalaciones. Tramitamos TC2, TC6, TC5 y TC7 encargándonos de toda la burocracia administrativa.",
            'border_color': "border-blue-600",
            'icon_color': "text-blue-600",
            'bg_color': "bg-blue-100"
        },
        {
            'title': "PROYECTOS DE INGENIERÍA",
            'icon': "ruler",
            'desc': "Informes técnicos, Memorias de cálculo y Proyectos de Gas. Dimensionamiento normado de cilindros y estanques.",
            'border_color': "border-orange-500",
            'icon_color': "text-orange-600",
            'bg_color': "bg-orange-100"
        }
    ]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extraemos los datos limpios
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje_cliente = form.cleaned_data['mensaje']

            # 1. GUARDAR EN BASE DE DATOS (NUEVO)
            Contacto.objects.create(
                nombre=nombre,
                email=email,
                telefono=telefono,
                mensaje=mensaje_cliente
            )

            # 2. ENVIAR CORREO (Como antes)
            cuerpo_correo = f"Nuevo contacto de: {nombre}\nTelefono: {telefono}\nEmail: {email}\n\nMensaje:\n{mensaje_cliente}"
            
            send_mail(
                subject=f"Nuevo Lead Web: {nombre}",
                message=cuerpo_correo,
                from_email='web@altogasspa.cl',
                recipient_list=['Altogasspa@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, "¡Solicitud recibida! Te contactaremos a la brevedad para coordinar la inspección.")

            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'title': 'Alto Gas SPA - Certificación y Sello Verde',
        'services': services,
        'form': form,
    }
    return render(request, 'core/home.html', context)