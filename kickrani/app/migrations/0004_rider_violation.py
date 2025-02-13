# Generated by Django 3.2.3 on 2021-06-02 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210527_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('riderId', models.AutoField(primary_key=True, serialize=False)),
                ('riderLocation', models.CharField(max_length=250, null=True)),
                ('riderPercentage', models.IntegerField(default=0, null=True)),
                ('kickId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kickrani')),
            ],
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('violationId', models.AutoField(primary_key=True, serialize=False)),
                ('helmetLocation', models.CharField(max_length=250, null=True)),
                ('personLocation', models.CharField(max_length=250, null=True)),
                ('personPercentage', models.CharField(max_length=250, null=True)),
                ('riderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rider')),
            ],
        ),
    ]
