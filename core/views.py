from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from django.views.decorators.cache import cache_page, never_cache
from .forms import ContactForm
from .models import Contacto, SolicitudAsesoria

# Home: cacheable solo en GET. Los POST (formulario) invalidan la caché
# automáticamente porque Django no cachea respuestas con cookies de mensajes.
@cache_page(60 * 15)  # 15 minutos
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
        'title': 'Alto Gas SPA - Sello Verde SEC | Ingeniería de Gas Chile',
        'services': services,
        'form': form,
    }
    return render(request, 'core/home.html', context)


# ──────────────────────────────────────────────────────────
# Vista: Asesoría y Revisión de Proyectos de Gas Online
# ──────────────────────────────────────────────────────────
def asesoria_online(request):
    expertise_areas = [
        {
            'title': 'Trazado y Recorrido de Tuberías',
            'desc':  'Validación del layout, distancias mínimas, soportería y paso por muros según NCh 2.h.',
            'icon':  'git-branch',
            'color': 'text-blue-600',
            'bg':    'bg-blue-100',
        },
        {
            'title': 'Dimensionamiento de Redes',
            'desc':  'Cálculo de diámetros, pérdidas de presión, caudales y selección de reguladores.',
            'icon':  'calculator',
            'color': 'text-orange-600',
            'bg':    'bg-orange-100',
        },
        {
            'title': 'Ventilaciones y Evacuación de Gases',
            'desc':  'Verificación de shunts, ductos, rejillas y tiraje natural/forzado para artefactos.',
            'icon':  'wind',
            'color': 'text-green-600',
            'bg':    'bg-green-100',
        },
        {
            'title': 'Materiales y Uniones',
            'desc':  'Revisión de accesorios, tipos de unión (roscada, soldada, PE) y compatibilidad normativa.',
            'icon':  'wrench',
            'color': 'text-slate-600',
            'bg':    'bg-slate-100',
        },
        {
            'title': 'Revisión Pre-Certificación SEC',
            'desc':  'Checklist final antes de presentar el proyecto ante la SEC, para garantizar aprobación.',
            'icon':  'clipboard-check',
            'color': 'text-purple-600',
            'bg':    'bg-purple-100',
        },
        {
            'title': 'Sala de Máquinas y Recintos de Gas',
            'desc':  'Superficies mínimas, distancias de seguridad, accesos y señalética obligatoria.',
            'icon':  'building-2',
            'color': 'text-red-600',
            'bg':    'bg-red-100',
        },
    ]

    if request.method == 'POST':
        nombre         = request.POST.get('nombre', '').strip()
        email          = request.POST.get('email', '').strip()
        telefono       = request.POST.get('telefono', '').strip()
        tipo_asesoria  = request.POST.get('tipo_asesoria', 'completa')
        mensaje_cliente = request.POST.get('mensaje', '').strip()

        if nombre and email and telefono and mensaje_cliente:
            # 1. Guardar en base de datos
            SolicitudAsesoria.objects.create(
                nombre=nombre,
                email=email,
                telefono=telefono,
                tipo_asesoria=tipo_asesoria,
                mensaje=mensaje_cliente,
            )

            # 2. Enviar correo de notificación
            tipo_label = dict(SolicitudAsesoria.TIPO_CHOICES).get(tipo_asesoria, tipo_asesoria)
            cuerpo = (
                f"Nueva solicitud de ASESORÍA ONLINE\n\n"
                f"Tipo: {tipo_label}\n"
                f"Nombre: {nombre}\n"
                f"Teléfono: {telefono}\n"
                f"Email: {email}\n\n"
                f"Proyecto / Consulta:\n{mensaje_cliente}"
            )
            send_mail(
                subject=f"[Asesoría Online] Nueva solicitud: {nombre}",
                message=cuerpo,
                from_email='web@altogasspa.cl',
                recipient_list=['Altogasspa@gmail.com'],
                fail_silently=False,
            )

            messages.success(
                request,
                "¡Solicitud recibida! Te contactaremos en menos de 24h hábiles para coordinar tu sesión."
            )
            if request.POST.get('source') == 'home':
                return HttpResponseRedirect('/#asesoria-online')
            return redirect('asesoria_online')

    context = {
        'title': 'Asesoría Online de Proyectos de Gas | Alto Gas SPA',
        'expertise_areas': expertise_areas,
    }
    return render(request, 'core/asesoria_online.html', context)


# ──────────────────────────────────────────────────────────
# Páginas de servicio individuales (indexables por Google)
# Cacheadas 1 hora: contenido estático que cambia poco.
# ──────────────────────────────────────────────────────────

@cache_page(60 * 60)
def servicio_sello_verde(request):
    steps = [
        {'icon': 'phone-call',    'title': 'Coordinación',          'desc': 'Nos contactas y coordinamos fecha y hora en tu domicilio o edificio.'},
        {'icon': 'clipboard-list','title': 'Inspección en terreno',  'desc': 'Realizamos prueba de hermeticidad y revisión visual de la instalación.'},
        {'icon': 'wrench',        'title': 'Reparación (si aplica)', 'desc': 'Corregimos fugas o deficiencias en la misma visita sin costo extra.'},
        {'icon': 'shield-check',  'title': 'Tramitación Sello Verde','desc': 'Inscribimos el TC6 y gestionamos el Sello Verde SEC ante la distribuidora.'},
    ]
    return render(request, 'core/servicio_sello_verde.html', {'steps': steps})


@cache_page(60 * 60)
def servicio_tramites_sec(request):
    sec_forms = [
        {
            'code': 'TC2',
            'title': 'Declaración de Instalación Nueva',
            'desc': 'Para instalaciones de gas nuevas que nunca han sido declaradas ante la SEC. Incluye planos y memoria de cálculo.',
        },
        {
            'code': 'TC5',
            'title': 'Declaración de Modificación',
            'desc': 'Para modificaciones o ampliaciones a una instalación existente ya declarada. Actualiza el expediente SEC.',
        },
        {
            'code': 'TC6',
            'title': 'Inscripción de Artefactos',
            'desc': 'Declaración de artefactos de gas (calderas, calefones, cocinas industriales). Requerido para el Sello Verde.',
        },
        {
            'code': 'TC7',
            'title': 'Regularización de Instalación',
            'desc': 'Para instalaciones existentes sin declaración previa. Permite regularizar y obtener documentación oficial.',
        },
    ]
    return render(request, 'core/servicio_tramites_sec.html', {'sec_forms': sec_forms})


@cache_page(60 * 60)
def servicio_proyectos(request):
    deliverables = [
        {
            'icon': 'file-text',
            'title': 'Memoria de Cálculo',
            'desc': 'Documento técnico con el dimensionamiento completo de la red: caudales, presiones, diámetros y pérdidas.',
        },
        {
            'icon': 'map',
            'title': 'Planos de Instalación',
            'desc': 'Planos isométricos y de planta con el trazado de tuberías, ubicación de artefactos y elementos de corte.',
        },
        {
            'icon': 'clipboard-check',
            'title': 'Informe Técnico SEC',
            'desc': 'Informe con normativa aplicada (NCh 2.h, NSEG), materiales a usar y especificaciones de instalación.',
        },
        {
            'icon': 'package',
            'title': 'Especificaciones de Materiales',
            'desc': 'Lista detallada de tuberías, accesorios, reguladores y materiales requeridos con sus normas de calidad.',
        },
        {
            'icon': 'calculator',
            'title': 'Dimensionamiento de Estanques',
            'desc': 'Cálculo de capacidad y selección de cilindros o estanques GLP según consumo y normativa vigente.',
        },
        {
            'icon': 'file-check-2',
            'title': 'Documentación para SEC',
            'desc': 'Formularios y declaraciones listas para presentar ante la SEC o distribuidora de gas.',
        },
    ]
    return render(request, 'core/servicio_proyectos.html', {'deliverables': deliverables})