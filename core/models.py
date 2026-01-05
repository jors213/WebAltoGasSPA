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