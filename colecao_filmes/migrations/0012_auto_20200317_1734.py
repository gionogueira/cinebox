# Generated by Django 3.0.3 on 2020-03-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colecao_filmes', '0011_auto_20200317_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='capa',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
