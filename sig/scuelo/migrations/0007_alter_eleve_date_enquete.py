# Generated by Django 4.2.11 on 2024-04-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scuelo', '0006_alter_paiement_options_alter_eleve_annee_inscr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='date_enquete',
            field=models.DateTimeField(blank=True),
        ),
    ]
