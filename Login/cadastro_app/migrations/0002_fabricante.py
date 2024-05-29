# Generated by Django 5.0.2 on 2024-05-19 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fabricante', models.CharField(max_length=100)),
                ('razao_social', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('vendedor', models.CharField(max_length=100)),
            ],
        ),
    ]
