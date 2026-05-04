from django.db import models

# Modelo para guardar los Leads (Clientes Potenciales)
class Contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    email = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    mensaje = models.TextField(verbose_name="Mensaje / Consulta")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Contacto")

    class Meta:
        verbose_name = "Lead Web"
        verbose_name_plural = "Leads Web (Consultas)"
        ordering = ['-fecha_creacion'] # Ordenar del más nuevo al más antiguo

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"


# ──────────────────────────────────────────────────────────
# Modelo para Solicitudes de Asesoría Online
# Separado de Contacto para poder gestionarlo de forma
# independiente en el admin y en reportes futuros.
# ──────────────────────────────────────────────────────────
class SolicitudAsesoria(models.Model):
    TIPO_CHOICES = [
        ('completa', 'Asesoría Completa — 60 min'),
        ('express',  'Consulta Express — 30 min'),
    ]
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente de Pago'),
        ('PAGADO', 'Pagado'),
        ('CANCELADO', 'Cancelado'),
    ]

    nombre       = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    email        = models.EmailField(verbose_name="Correo Electrónico")
    telefono     = models.CharField(max_length=20,  verbose_name="Teléfono / WhatsApp")
    tipo_asesoria = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='completa',
        verbose_name="Tipo de Asesoría"
    )
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    monto = models.DecimalField(max_digits=10, decimal_places=0, default=60000)
    gateway = models.CharField(max_length=20, blank=True)
    token_transaccion = models.UUIDField(blank=True, null=True)
    fecha_pago = models.DateTimeField(blank=True, null=True)
    mensaje      = models.TextField(verbose_name="Descripción del Proyecto / Consulta")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")

    class Meta:
        verbose_name        = "Solicitud de Asesoría Online"
        verbose_name_plural = "Solicitudes de Asesoría Online"
        ordering            = ['-fecha_creacion']

    def __str__(self):
        return f"{self.get_tipo_asesoria_display()} | {self.nombre} - {self.telefono}"
