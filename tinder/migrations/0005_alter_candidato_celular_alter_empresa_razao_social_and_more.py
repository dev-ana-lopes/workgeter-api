# Generated by Django 4.1.1 on 2022-09-28 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinder', '0004_formulario_alter_candidato_nome_completo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='celular',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='razao_social',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='atividade_vaga',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='beneficios_vagas',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='descricao_participacao_vagas',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='requisitos_vagas',
            field=models.CharField(max_length=1000),
        ),
    ]
