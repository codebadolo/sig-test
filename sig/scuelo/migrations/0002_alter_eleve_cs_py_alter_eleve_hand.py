# Generated by Django 4.2.11 on 2024-03-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scuelo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='cs_py',
            field=models.CharField(choices=[('CS', 'CS'), ('Extra', 'EXTRA'), ('PY', 'PY')], max_length=34),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='hand',
            field=models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=34),
        ),
    ]