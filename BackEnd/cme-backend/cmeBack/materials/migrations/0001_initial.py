# Generated by Django 5.0.6 on 2024-06-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materiais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('data', models.DateField(blank=True)),
                ('type_material', models.CharField(blank=True, choices=[('CIR', 'Cirugico'), ('DESC', 'descartavel')], max_length=10)),
                ('stage', models.CharField(blank=True, max_length=100)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
    ]
