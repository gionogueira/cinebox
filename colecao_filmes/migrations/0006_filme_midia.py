# Generated by Django 3.0.3 on 2020-02-24 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colecao_filmes', '0005_remove_filme_midia'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='midia',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
