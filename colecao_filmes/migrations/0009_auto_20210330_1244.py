# Generated by Django 3.0.3 on 2021-03-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colecao_filmes', '0008_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='capa',
            field=models.ImageField(default='default.jpg', upload_to='capa_pics'),
        ),
    ]
