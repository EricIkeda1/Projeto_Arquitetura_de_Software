# Generated by Django 5.0.2 on 2024-05-23 21:27

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_app', '0003_grupo_subgrupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_hora_venda', models.DateTimeField(default=django.utils.timezone.now)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro_app.produto')),
            ],
        ),
    ]
