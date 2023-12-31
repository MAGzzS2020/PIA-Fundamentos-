# Generated by Django 4.2.6 on 2023-10-31 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.PositiveSmallIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('creditos', models.PositiveBigIntegerField()),
                ('docente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('apellidopaterno', models.CharField(max_length=35)),
                ('apellidomaterno', models.CharField(max_length=35)),
                ('nombres', models.CharField(max_length=35)),
                ('fechanacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('Vigencia', models.BooleanField(default=True)),
                ('Carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('FechaMatricula', models.DateTimeField(auto_now_add=True)),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.estudiante')),
            ],
        ),
    ]
