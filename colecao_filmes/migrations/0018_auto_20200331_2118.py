# Generated by Django 3.0.3 on 2020-04-01 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colecao_filmes', '0017_auto_20200331_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='sinopse',
            field=models.TextField(blank=True, null=True),
        ),
    ]
