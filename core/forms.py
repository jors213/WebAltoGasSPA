from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre Completo",
        max_length=100,
        widget=forms.TextInput(attrs={
            # Agregamos 'text-slate-900' aquí al principio
            'class': 'text-slate-900 w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-300 focus:border-orange-500 focus:bg-white focus:outline-none transition duration-200',
            'placeholder': 'Ej: David Torres'
        })
    )
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'text-slate-900 w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-300 focus:border-orange-500 focus:bg-white focus:outline-none transition duration-200',
            'placeholder': 'tu@correo.com'
        })
    )
    telefono = forms.CharField(
        label="Teléfono",
        widget=forms.TextInput(attrs={
            'class': 'text-slate-900 w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-300 focus:border-orange-500 focus:bg-white focus:outline-none transition duration-200',
            'placeholder': '+56 9 ...'
        })
    )
    mensaje = forms.CharField(
        label="¿En qué podemos ayudarte?",
        widget=forms.Textarea(attrs={
            'class': 'text-slate-900 w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-300 focus:border-orange-500 focus:bg-white focus:outline-none transition duration-200',
            'rows': 4,
            'placeholder': 'Necesito certificación Sello Verde para mi edificio...'
        })
    )