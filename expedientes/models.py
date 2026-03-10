from django.db import models
from django.contrib.auth.models import User
import os


ESCUELAS = [
    ('medicina_humana', 'Medicina Humana'),
    ('odontologia', 'Odontología'),
    ('farmacia_bioquimica', 'Farmacia y Bioquímica'),
    ('enfermeria', 'Enfermería'),
    ('obstetricia', 'Obstetricia'),
    ('psicologia', 'Psicología'),
    ('nutricion_humana', 'Nutrición Humana'),
    ('medicina_veterinaria', 'Medicina Veterinaria y Zootecnia'),
    ('tecnologia_medica', 'Tecnología Médica'),
    ('ingenieria_civil', 'Ingeniería Civil'),
    ('ingenieria_industrial', 'Ingeniería Industrial'),
    ('ingenieria_sistemas', 'Ingeniería de Sistemas y Computación'),
    ('arquitectura', 'Arquitectura'),
    ('administracion_sistemas', 'Administración y Sistemas'),
    ('contabilidad_finanzas', 'Contabilidad y Finanzas'),
    ('admin_talento_humano', 'Administración y Gestión del Talento Humano'),
    ('admin_inteligencia_negocios', 'Administración e Inteligencia de Negocios'),
    ('admin_negocios_globales', 'Administración y Negocios Globales'),
    ('derecho', 'Derecho'),
    ('educacion_inicial', 'Educación Inicial'),
    ('educacion_primaria', 'Educación Primaria'),
]


def upload_expediente1(instance, filename):
    dni = instance.estudiante.dni or 'sin_dni'
    return f'expedientes/{dni}/exp1/{filename}'


def upload_expediente2(instance, filename):
    dni = instance.estudiante.dni or 'sin_dni'
    return f'expedientes/{dni}/exp2/{filename}'


def upload_resolucion(instance, filename):
    dni = instance.estudiante.dni or 'sin_dni'
    return f'expedientes/{dni}/resoluciones/{filename}'


class Estudiante(models.Model):
    # Datos personales
    apellidos_nombres = models.CharField(max_length=200, blank=True, default='')
    dni = models.CharField(max_length=8, blank=True, default='')
    n_expediente = models.CharField(max_length=50, blank=True, default='')
    proveido = models.CharField(max_length=200, blank=True, default='')
    escuela = models.CharField(max_length=50, choices=ESCUELAS, blank=True, default='')
    celular = models.CharField(max_length=15, blank=True, default='')
    correo = models.EmailField(blank=True, default='')
    codigo_matricula = models.CharField(max_length=20, blank=True, default='')

    # Control
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return self.apellidos_nombres or f'Estudiante #{self.pk}'

    def get_nombre_display(self):
        return self.apellidos_nombres or 'Sin nombre'

    def tiene_expediente1_completo(self):
        exp = self.expediente1_set.first()
        if not exp:
            return False
        return all([exp.dni_pdf, exp.solicitud_pdf, exp.foto, exp.recibo_pdf, exp.registro_graduados_pdf])

    def tiene_expediente2_completo(self):
        exp = self.expediente2_set.first()
        if not exp:
            return False
        return all([exp.certificado_notas, exp.constancia_proyeccion, exp.constancia_no_adeudo])

    def estado_semaforo(self):
        exp1_ok = self.tiene_expediente1_completo()
        exp2_ok = self.tiene_expediente2_completo()
        if exp1_ok and exp2_ok:
            return 'verde'
        return 'rojo'

    def archivos_estado(self):
        """Retorna dict con estado de cada archivo"""
        exp1 = self.expediente1_set.first()
        exp2 = self.expediente2_set.first()
        return {
            'exp1': {
                'dni_pdf': bool(exp1 and exp1.dni_pdf),
                'solicitud_pdf': bool(exp1 and exp1.solicitud_pdf),
                'foto': bool(exp1 and exp1.foto),
                'recibo_pdf': bool(exp1 and exp1.recibo_pdf),
                'registro_graduados_pdf': bool(exp1 and exp1.registro_graduados_pdf),
            },
            'exp2': {
                'certificado_notas': bool(exp2 and exp2.certificado_notas),
                'constancia_proyeccion': bool(exp2 and exp2.constancia_proyeccion),
                'constancia_no_adeudo': bool(exp2 and exp2.constancia_no_adeudo),
            }
        }


class Expediente1(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    dni_pdf = models.FileField(upload_to=upload_expediente1, blank=True, null=True)
    solicitud_pdf = models.FileField(upload_to=upload_expediente1, blank=True, null=True)
    foto = models.FileField(upload_to=upload_expediente1, blank=True, null=True)
    recibo_pdf = models.FileField(upload_to=upload_expediente1, blank=True, null=True)
    registro_graduados_pdf = models.FileField(upload_to=upload_expediente1, blank=True, null=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Expediente 1'

    def __str__(self):
        return f'Exp1 - {self.estudiante}'


class Expediente2(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    certificado_notas = models.FileField(upload_to=upload_expediente2, blank=True, null=True)
    constancia_proyeccion = models.FileField(upload_to=upload_expediente2, blank=True, null=True)
    constancia_no_adeudo = models.FileField(upload_to=upload_expediente2, blank=True, null=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Expediente 2'

    def __str__(self):
        return f'Exp2 - {self.estudiante}'


class Resolucion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='resoluciones')
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to=upload_resolucion)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Resolución'
        verbose_name_plural = 'Resoluciones'

    def __str__(self):
        return f'{self.nombre} - {self.estudiante}'
