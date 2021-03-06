# Generated by Django 3.1.7 on 2021-04-13 16:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Article', '0010_auto_20210413_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=50)),
                ('Date_naissance', models.DateField()),
                ('rue', models.CharField(max_length=50)),
                ('code_postal', models.DecimalField(decimal_places=0, default='', max_digits=5)),
                ('Ville', models.CharField(max_length=100)),
                ('Categorie_socioPro', models.CharField(choices=[('Etudiant', 'Etudiant'), ('Cadre', 'Cadre'), ('Professeur', 'Professeur')], max_length=100)),
                ('Numero_Telephone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('Email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantite', models.IntegerField()),
                ('Montant', models.FloatField()),
                ('Commande_article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Article.article')),
                ('client', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='Client.client')),
            ],
        ),
    ]
