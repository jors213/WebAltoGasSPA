from django import forms

INPUT_CLASSES = (
    'w-full px-4 py-3.5 rounded-md bg-white border border-slate-200 text-slate-900 '
    'placeholder-slate-400 text-sm transition duration-200 '
    'focus:border-orange-500 focus:outline-none'
)


class ContactForm(forms.Form):
    SERVICIO_CHOICES = [
        ('Sello Verde', 'Sello Verde'),
        ('Trámite SEC', 'Trámite SEC'),
        ('Proyecto', 'Proyecto'),
        ('Fuga / urgencia', 'Fuga / urgencia'),
        ('Asesoría online', 'Asesoría online'),
    ]

    nombre = forms.CharField(
        label="Nombre completo",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Ej: David Torres'
        })
    )
    telefono = forms.CharField(
        label="Teléfono",
        widget=forms.TextInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': '+56 9 ...'
        })
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'tu@correo.com'
        })
    )
    # Sólo sirve para calificar el lead: se antepone al mensaje que se guarda
    # y se envía por correo, así no requiere migración del modelo Contacto.
    servicio = forms.ChoiceField(
        label="¿Qué necesitas?",
        choices=SERVICIO_CHOICES,
        required=False,
        initial='Sello Verde',
        widget=forms.RadioSelect
    )
    mensaje = forms.CharField(
        label="Cuéntanos brevemente",
        widget=forms.Textarea(attrs={
            'class': INPUT_CLASSES + ' resize-none',
            'rows': 4,
            'placeholder': 'Tipo de inmueble, comuna y si ya tienes un sello asignado…'
        })
    )
