# Generated by Django 4.0.6 on 2022-08-10 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('receitas', '0003_alter_livroreceitas_nome_receita'),
    ]

    operations = [
        migrations.AddField(
            model_name='livroreceitas',
            name='pessoa',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
            preserve_default=False,
        ),
    ]
