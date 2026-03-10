from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('expedientes', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='codigo_matricula',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
