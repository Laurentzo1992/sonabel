# Generated by Django 5.0.1 on 2024-05-06 09:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Devises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=200, null=True)),
                ('symbole', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dossiers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planitem_id', models.IntegerField(blank=True, null=True)),
                ('numero_doss', models.CharField(blank=True, max_length=200, null=True)),
                ('intitule_doss', models.TextField(blank=True, null=True)),
                ('date_trans_sign', models.DateField(blank=True, null=True)),
                ('date_retour_sign', models.DateField(blank=True, null=True)),
                ('date_trans_dgcmef', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dossier_id', models.IntegerField(blank=True, null=True)),
                ('num_lot', models.CharField(blank=True, max_length=200, null=True)),
                ('intitule_lot', models.TextField(blank=True, null=True)),
                ('montant_lot', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.IntegerField(blank=True, null=True)),
                ('date_plan', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Planitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_ordre', models.CharField(blank=True, max_length=200, null=True)),
                ('budget', models.CharField(blank=True, max_length=200, null=True)),
                ('typcredit', models.CharField(blank=True, max_length=200, null=True)),
                ('immobilisation', models.CharField(blank=True, max_length=200, null=True)),
                ('credit', models.CharField(blank=True, max_length=200, null=True)),
                ('centre_cout', models.CharField(blank=True, max_length=200, null=True)),
                ('projet', models.CharField(blank=True, max_length=200, null=True)),
                ('localisation', models.CharField(blank=True, max_length=200, null=True)),
                ('montant_estime', models.CharField(blank=True, max_length=200, null=True)),
                ('composante', models.CharField(blank=True, max_length=200, null=True)),
                ('montant_dispo', models.CharField(blank=True, max_length=200, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('mode', models.CharField(blank=True, max_length=200, null=True)),
                ('nbr_lot', models.CharField(blank=True, max_length=200, null=True)),
                ('date_tech', models.CharField(blank=True, max_length=200, null=True)),
                ('date_tech_reel', models.CharField(blank=True, max_length=200, null=True)),
                ('date_dgcmef', models.CharField(blank=True, max_length=200, null=True)),
                ('date_dgcmef_reel', models.CharField(blank=True, max_length=200, null=True)),
                ('date_off', models.CharField(blank=True, max_length=200, null=True)),
                ('date_off_reel', models.CharField(blank=True, max_length=200, null=True)),
                ('temp', models.IntegerField(blank=True, null=True)),
                ('temp_reel', models.IntegerField(blank=True, null=True)),
                ('date_resultat', models.CharField(blank=True, max_length=200, null=True)),
                ('resultat', models.CharField(blank=True, max_length=200, null=True)),
                ('date_visite_site', models.CharField(blank=True, max_length=200, null=True)),
                ('date_demarrage', models.CharField(blank=True, max_length=200, null=True)),
                ('date_reel_demarrage', models.CharField(blank=True, max_length=200, null=True)),
                ('delai_exe', models.IntegerField(blank=True, null=True)),
                ('delai_reel_exe', models.IntegerField(blank=True, null=True)),
                ('date_butoir', models.CharField(blank=True, max_length=200, null=True)),
                ('date_reel_fin', models.CharField(blank=True, max_length=200, null=True)),
                ('budget_travaux', models.CharField(blank=True, max_length=200, null=True)),
                ('observation', models.CharField(blank=True, max_length=200, null=True)),
                ('statut', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('agent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Agent en charge')),
                ('plan_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suivi.plans', verbose_name='PPM')),
            ],
        ),
        migrations.AddField(
            model_name='plans',
            name='statut',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suivi.status'),
        ),
    ]
