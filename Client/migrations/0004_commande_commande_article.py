# Generated by Django 3.1.7 on 2021-03-30 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_auto_20210329_1347'),
        ('Client', '0003_remove_commande_commande_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='Commande_article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Article.article'),
        ),
    ]