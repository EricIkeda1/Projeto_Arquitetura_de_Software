# Generated by Django 5.0.2 on 2024-07-28 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_app', '0005_remove_venda_produto_remove_venda_quantidade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedeSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
    ]
