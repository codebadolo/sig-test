# Generated by Django 4.2.11 on 2024-04-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=34)),
                ('prenom', models.CharField(max_length=34)),
                ('date_enquete', models.DateTimeField(auto_now_add=True)),
                ('condition_eleve', models.CharField(choices=[('CONF', 'CONF'), ('ABAN', 'ABAN'), ('PROP', 'PROP')], max_length=34)),
                ('sex', models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=10)),
                ('date_naissance', models.DateField()),
                ('cs_py', models.CharField(choices=[('CS', 'CS'), ('Extra', 'EXTRA'), ('PY', 'PY')], max_length=34)),
                ('hand', models.CharField(choices=[('DA', 'OUI'), ('DM', 'NON'), ('DM', 'NON'), ('DM', 'NON')], max_length=34)),
                ('annee_inscr', models.DateField()),
                ('parent', models.CharField(max_length=34)),
                ('tel_parent', models.CharField(max_length=12)),
                ('type_ecole', models.CharField(choices=[('MATERNELLE', 'MATERNELLE'), ('PRIMAIRE', 'PRIMAIRE')], max_length=14)),
                ('nom_classe', models.CharField(choices=[('PS', 'PS'), ('MS', 'MS'), ('GS', 'GS'), ('CP1', 'CP1'), ('CP2', 'CP2'), ('CE1', 'CE1'), ('CE2', 'CE2'), ('CM1', 'CM1'), ('CM2', 'CM2')], max_length=34)),
                ('ordre_classe', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('causal', models.CharField(choices=[('insc', 'inscription'), ('sco', 'scolarite'), ('ten', 'tenue'), ('can', 'cantine')], max_length=34)),
                ('montant', models.PositiveBigIntegerField(max_length=34)),
                ('date_paiement', models.DateTimeField(auto_now_add=True)),
                ('note_Paiement', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
