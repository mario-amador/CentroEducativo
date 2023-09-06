# Generated by Django 4.2.2 on 2023-08-05 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TechHive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_factura', models.IntegerField(unique=True)),
                ('fecha_emision', models.DateField(auto_now_add=True)),
                ('CentroEducativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.centroeducativo')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaHoraPago', models.DateTimeField(auto_now_add=True)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.alumno')),
                ('Meses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.meses')),
                ('TipoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.tipopago')),
                ('Tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.tutor')),
            ],
        ),
        migrations.RemoveField(
            model_name='pagos',
            name='Alumno',
        ),
        migrations.RemoveField(
            model_name='pagos',
            name='Meses',
        ),
        migrations.RemoveField(
            model_name='pagos',
            name='TipoPago',
        ),
        migrations.RemoveField(
            model_name='pagos',
            name='Tutor',
        ),
        migrations.AlterField(
            model_name='parametrossar',
            name='RTN',
            field=models.CharField(help_text='No, debe contenes letras, digitos: 14 ', max_length=14),
        ),
        migrations.DeleteModel(
            name='Facturacion',
        ),
        migrations.AddField(
            model_name='factura',
            name='ParametrosSAR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.parametrossar'),
        ),
        migrations.AddField(
            model_name='factura',
            name='pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.pago'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='Pagos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechHive.pago'),
        ),
        migrations.DeleteModel(
            name='Pagos',
        ),
    ]
