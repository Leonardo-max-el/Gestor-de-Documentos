from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('expedientes', '0002_estudiante_codigo_matricula'),
    ]
    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='n_informe',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
