from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import expedientes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos_nombres', models.CharField(blank=True, default='', max_length=200)),
                ('dni', models.CharField(blank=True, default='', max_length=8)),
                ('n_expediente', models.CharField(blank=True, default='', max_length=50)),
                ('proveido', models.CharField(blank=True, default='', max_length=200)),
                ('escuela', models.CharField(blank=True, choices=[('medicina_humana', 'Medicina Humana'), ('odontologia', 'Odontología'), ('farmacia_bioquimica', 'Farmacia y Bioquímica'), ('enfermeria', 'Enfermería'), ('obstetricia', 'Obstetricia'), ('psicologia', 'Psicología'), ('nutricion_humana', 'Nutrición Humana'), ('medicina_veterinaria', 'Medicina Veterinaria y Zootecnia'), ('tecnologia_medica', 'Tecnología Médica'), ('ingenieria_civil', 'Ingeniería Civil'), ('ingenieria_industrial', 'Ingeniería Industrial'), ('ingenieria_sistemas', 'Ingeniería de Sistemas y Computación'), ('arquitectura', 'Arquitectura'), ('administracion_sistemas', 'Administración y Sistemas'), ('contabilidad_finanzas', 'Contabilidad y Finanzas'), ('admin_talento_humano', 'Administración y Gestión del Talento Humano'), ('admin_inteligencia_negocios', 'Administración e Inteligencia de Negocios'), ('admin_negocios_globales', 'Administración y Negocios Globales'), ('derecho', 'Derecho'), ('educacion_inicial', 'Educación Inicial'), ('educacion_primaria', 'Educación Primaria')], default='', max_length=50)),
                ('celular', models.CharField(blank=True, default='', max_length=15)),
                ('correo', models.EmailField(blank=True, default='', max_length=254)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('creado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['-fecha_creacion'], 'verbose_name': 'Estudiante', 'verbose_name_plural': 'Estudiantes'},
        ),
        migrations.CreateModel(
            name='Expediente1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_pdf', models.FileField(blank=True, null=True, upload_to=expedientes.models.upload_expediente1)),
                ('solicitud_pdf', models.FileField(blank=True, null=True, upload_to=expedientes.models.upload_expediente1)),
                ('foto', models.FileField(blank=True, null=True, upload_to=expedientes.models.upload_expediente1)),
                ('recibo_pdf', models.FileField(blank=True, null=True, upload_to=expedientes.models.upload_expediente1)),
                ('registro_graduados_pdf', models.FileField(blank=True, null=True, upload_to=expedientes.models.upload_expediente1)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expedientes.estudiante')),
            ],
            options={'verbose_name': 'Expediente 1'},
        ),
        migrations.CreateModel(
            name='Expediente2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificado_notas', models.FileField(blank=True, null=True, upload_to=expedientes.models.upload_expediente2)),
                ('constancia_proyeccion', models.FileField(blank=True, null=True, upload_to=expedientes.models.upload_expediente2)),
                ('constancia_no_adeudo', models.FileField(blank=True, null=True, upload_to=expedientes.models.upload_expediente2)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expedientes.estudiante')),
            ],
            options={'verbose_name': 'Expediente 2'},
        ),
        migrations.CreateModel(
            name='Resolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('archivo', models.FileField(upload_to=expedientes.models.upload_resolucion)),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resoluciones', to='expedientes.estudiante')),
            ],
            options={'verbose_name': 'Resolución', 'verbose_name_plural': 'Resoluciones'},
        ),
    ]
