# Generated by Django 3.0.3 on 2020-06-04 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colecao_filmes', '0004_auto_20200604_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filme', to='colecao_filmes.Genero'),
        ),
    ]
