from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudAsesoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre',        models.CharField(max_length=100, verbose_name='Nombre del Cliente')),
                ('email',         models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('telefono',      models.CharField(max_length=20,  verbose_name='Teléfono / WhatsApp')),
                ('tipo_asesoria', models.CharField(
                    max_length=20,
                    default='completa',
                    choices=[
                        ('completa', 'Asesoría Completa — 60 min'),
                        ('express',  'Consulta Express — 30 min'),
                    ],
                    verbose_name='Tipo de Asesoría',
                )),
                ('mensaje',         models.TextField(verbose_name='Descripción del Proyecto / Consulta')),
                ('fecha_creacion',  models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Solicitud')),
            ],
            options={
                'verbose_name':        'Solicitud de Asesoría Online',
                'verbose_name_plural': 'Solicitudes de Asesoría Online',
                'ordering':            ['-fecha_creacion'],
            },
        ),
    ]
