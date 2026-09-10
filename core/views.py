from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.views.decorators.cache import cache_page, never_cache
from django.urls import reverse
from .forms import ContactForm
from .models import Contacto, SolicitudAsesoria

def home(request):
    services = [
        {
            'code': "S-01",
            'title': "INSPECCIÓN Y SELLO VERDE",
            'icon': "check-circle-2",
            'desc': "Certificación oficial para edificios, hogares y locales. Realizamos la inspección periódica y gestionamos tu Sello Verde ante la SEC.",
            'bullets': ["Prueba de hermeticidad", "Detección de fugas", "Inscripción del certificado"],
            'url_name': "servicio_sello_verde",
            'border_color': "border-green-600",
            'icon_color': "text-green-600",
            'bg_color': "bg-green-100",
            'dot_color': "bg-green-600"
        },
        {
            'code': "S-02",
            'title': "DECLARACIÓN Y TRÁMITES SEC",
            'icon': "file-signature",
            'desc': "Regularizamos tus instalaciones. Tramitamos TC2, TC6, TC5 y TC7 encargándonos de toda la burocracia administrativa.",
            'bullets': ["Formularios TC2 y TC6", "Formularios TC5 y TC7", "Regularización de obras antiguas"],
            'url_name': "servicio_tramites_sec",
            'border_color': "border-blue-600",
            'icon_color': "text-blue-600",
            'bg_color': "bg-blue-100",
            'dot_color': "bg-blue-600"
        },
        {
            'code': "S-03",
            'title': "PROYECTOS DE INGENIERÍA",
            'icon': "ruler",
            'desc': "Informes técnicos, Memorias de cálculo y Proyectos de Gas. Dimensionamiento normado de cilindros y estanques.",
            'bullets': ["Memorias de cálculo", "Planos de red interior", "Dimensionamiento de estanques"],
            'url_name': "servicio_proyectos",
            'border_color': "border-orange-500",
            'icon_color': "text-orange-600",
            'bg_color': "bg-orange-100",
            'dot_color': "bg-orange-500"
        }
    ]

    # Reseñas reales publicadas en el perfil de Google Business de Alto Gas SPA.
    # Para actualizarlas basta editar esta lista. `google_reviews` refleja el
    # total y el promedio que muestra Google (revisar de vez en cuando).
    google_rating = "5,0"
    google_reviews = 24
    # Pega aquí el enlace público a las reseñas de Google para activar el
    # botón "Ver las opiniones en Google" (si queda vacío, el botón no se muestra).
    google_reviews_url = ""

    # Las mejores primero: el carrusel de la home las muestra en este orden.
    testimonials = [
        {
            'name': "Camilo Venegas Gotelli",
            'meta': "Sello Verde y TC6",
            'text': "Muy agradecidos, me costó mucho confiar porque anteriormente me habían estafado, "
                    "lo recomiendo totalmente. Tramitó sello verde y TC6.",
        },
        {
            'name': "Lucas Espinoza",
            'meta': "Revisión de instalación",
            'text': "Excelente servicio. Los contacté para una revisión y me respondieron rapidísimo. "
                    "Muy buena atención, súper claros para explicar los detalles técnicos y resolvieron "
                    "todo a tiempo. 100% recomendados.",
        },
        {
            'name': "Diego Urzúa",
            'meta': "Trabajo ejecutado en terreno",
            'text': "Excelente servicio, 100% recomendado. Se puede ver la experiencia en el servicio "
                    "otorgado. Adicionalmente quiero agregar que tiene la paciencia de explicar con "
                    "detalle el trabajo ejecutado.",
        },
        {
            'name': "Eyleen Andrea Canchig",
            'meta': "Instalación",
            'text': "100% recomendado. El trabajo de David un 7, muy simpático, me ayudó con la "
                    "instalación, me explicó todo. Así que lo recomiendo a ojos cerrados.",
        },
        {
            'name': "Nicol Andrea Londoño",
            'meta': "Asesoría de proyectos",
            'text': "Me contacté con David para ver unos proyectos y quedé muy conforme con la atención "
                    "y la asesoría. Recomendadísimo.",
        },
        {
            'name': "Rebeca Badilla",
            'meta': "Cliente",
            'text': "Buen servicio, siempre atento a las consultas y para agilizar proceso. Recomendable.",
        },
        {
            'name': "Mauro Robles",
            'meta': "Ejecución de trabajos",
            'text': "Profesionalismo en la ejecución de los trabajos, totalmente recomendable.",
        },
        {
            'name': "Fernando Armijo",
            'meta': "Cliente",
            'text': "Excelente servicio, profesional y comprometido.",
        },
        {
            'name': "Brallan Cea",
            'meta': "Cliente",
            'text': "Excelente servicio, muy profesional.",
        },
        {
            'name': "Braulio Miranda",
            'meta': "Cliente",
            'text': "Perfecto el servicio, buena atención. ¡Recomendado!",
        },
        {
            'name': "Yordan Sáez",
            'meta': "Cliente",
            'text': "Buen trabajo, buen profesional. Recomendado.",
        },
        {
            'name': "Cecilia Canchig",
            'meta': "Cliente",
            'text': "Excelente servicio, recomendado 100%.",
        },
    ]

    faqs = [
        {
            'q': "¿Cada cuánto debo renovar la inspección de gas?",
            'a': "La periodicidad la fija la normativa SEC según el tipo de inmueble y de instalación. "
                 "En la inspección te dejamos indicada la fecha de vencimiento en el certificado y te "
                 "avisamos antes de que expire para que no se te pase.",
        },
        {
            'q': "Mi edificio quedó con sello rojo. ¿Qué significa y qué hago?",
            'a': "El sello rojo indica que la instalación fue rechazada y no puede seguir operando en esas "
                 "condiciones: la distribuidora puede suspender el suministro hasta que se regularice. "
                 "Lo primero es un diagnóstico en terreno para saber qué se debe corregir; nosotros hacemos "
                 "la reparación y la tramitación posterior ante la SEC.",
        },
        {
            'q': "¿Trabajan con Gas Natural y Gas Licuado?",
            'a': "Sí, con ambos. Atendemos instalaciones de red de gas natural y de gas licuado, tanto en "
                 "cilindros como en estanques.",
        },
        {
            'q': "¿Cuánto cuesta certificar un departamento, una casa o un edificio?",
            'a': "Depende del tipo de inmueble, la cantidad de artefactos y el estado de la instalación. "
                 "Cuéntanos esos datos por WhatsApp o por el formulario y te enviamos una cotización clara, "
                 "sin costo y sin letra chica, en menos de 24 horas hábiles.",
        },
        {
            'q': "¿Atienden fuera de la Región Metropolitana?",
            'a': "Sí. Estamos en Santiago y trabajamos en regiones. Para la revisión de proyectos y planos "
                 "también tenemos asesoría por videollamada, que funciona desde cualquier parte de Chile.",
        },
        {
            'q': "¿Qué diferencia hay entre el TC6 y el Sello Verde?",
            'a': "El TC6 es la declaración de los artefactos de gas ante la SEC. El Sello Verde es el "
                 "resultado de la inspección periódica que acredita que la instalación cumple la norma. "
                 "Van de la mano: sin los artefactos correctamente declarados no se obtiene el sello.",
        },
    ]

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje_cliente = form.cleaned_data['mensaje']
            servicio = form.cleaned_data.get('servicio') or ''

            # El servicio elegido viaja como prefijo del mensaje: califica el
            # lead sin necesidad de migrar el modelo Contacto.
            mensaje_guardado = f"[{servicio}] {mensaje_cliente}" if servicio else mensaje_cliente

            Contacto.objects.create(
                nombre=nombre,
                email=email,
                telefono=telefono,
                mensaje=mensaje_guardado
            )

            cuerpo_correo = (
                f"Nuevo contacto de: {nombre}\n"
                f"Servicio: {servicio or 'No indicado'}\n"
                f"Telefono: {telefono}\nEmail: {email}\n\n"
                f"Mensaje:\n{mensaje_cliente}"
            )
            try:
                send_mail(
                    subject=f"Nuevo Lead Web ({servicio or 'General'}): {nombre}",
                    message=cuerpo_correo,
                    from_email=None,
                    recipient_list=['Altogasspa@gmail.com'],
                    fail_silently=True,
                )
            except BaseException:
                pass

            messages.success(request, "¡Solicitud recibida! Te contactaremos a la brevedad para coordinar la inspección.")
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'title': 'Alto Gas SPA - Sello Verde SEC | Ingeniería de Gas Chile',
        'services': services,
        'testimonials': testimonials,
        'faqs': faqs,
        'google_rating': google_rating,
        'google_reviews': google_reviews,
        'google_reviews_url': google_reviews_url,
        'form': form,
    }
    return render(request, 'core/home.html', context)


def asesoria_online(request):
    # Tarjetas del bloque "¿Qué podemos revisar?" de asesoria_online.html.
    # Vivian en la vista home, que ya no las usa: la plantilla de esta pagina
    # las recorria siempre vacias.
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
        nombre          = request.POST.get('nombre', '').strip()
        email           = request.POST.get('email', '').strip()
        telefono        = request.POST.get('telefono', '').strip()
        tipo_asesoria   = request.POST.get('tipo_asesoria', 'completa')
        mensaje_cliente = request.POST.get('mensaje', '').strip()

        if nombre and email and telefono and mensaje_cliente:
            solicitud = SolicitudAsesoria.objects.create(
                nombre=nombre,
                email=email,
                telefono=telefono,
                gateway='transferencia',
                tipo_asesoria=tipo_asesoria,
                mensaje=mensaje_cliente,
                estado='PENDIENTE'
            )

            monto = 60000 if tipo_asesoria == 'completa' else 30000
            tipo_label = dict(SolicitudAsesoria.TIPO_CHOICES).get(tipo_asesoria, tipo_asesoria)
            monto_fmt = f"${monto:,}".replace(",", ".")

            email_context = {
                'solicitud': solicitud,
                'nombre': nombre,
                'monto': monto,
                'monto_fmt': monto_fmt,
                'tipo_label': tipo_label,
                'telefono': telefono,
                'email': email,
            }
            html_content = render_to_string('core/email_asesoria.html', email_context)
            text_content = strip_tags(html_content)
            try:
                send_mail(
                    subject=f"Solicitud #{solicitud.pk} confirmada - Alto Gas SPA",
                    message=text_content,
                    from_email=None,
                    recipient_list=[email],
                    html_message=html_content,
                    fail_silently=True,
                )
            except BaseException:
                pass

            cuerpo_admin = (
                f"Nueva solicitud de ASESORÍA ONLINE #{solicitud.pk}\n\n"
                f"Gateway: TRANSFERENCIA\n"
                f"Tipo: {tipo_label}\n"
                f"Nombre: {nombre}\n"
                f"Teléfono: {telefono}\n"
                f"Email: {email}\n\n"
                f"Proyecto / Consulta:\n{mensaje_cliente}"
            )
            try:
                send_mail(
                    subject=f"[Asesoría Online] #{solicitud.pk} TRANSFERENCIA: {nombre}",
                    message=cuerpo_admin,
                    from_email=None,
                    recipient_list=['Altogasspa@gmail.com'],
                    fail_silently=True,
                )
            except BaseException:
                pass

            return render(request, 'core/asesoria_online.html', {
                'expertise_areas': expertise_areas,
                'mostrar_modal': True,
                'solicitud': solicitud,
                'monto': monto,
                'monto_fmt': monto_fmt,
            })

        messages.error(request, "Por favor completa todos los campos correctamente.")
        return redirect('asesoria_online')

    return render(request, 'core/asesoria_online.html', {
        'expertise_areas': expertise_areas,
    })


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


def pago_transferencia(request, pk):
    """
    Vista para Transferencia Bancaria Manual - muestra instrucciones y monto
    """
    solicitud = get_object_or_404(SolicitudAsesoria, pk=pk, estado='PENDIENTE')
    monto = 60000 if solicitud.tipo_asesoria == 'completa' else 30000
    context = {
        'solicitud': solicitud,
        'monto': monto,
        'title': f'Pago Transferencia #{pk} - Alto Gas SPA'
    }
    return render(request, 'core/pago_transferencia.html', context)
