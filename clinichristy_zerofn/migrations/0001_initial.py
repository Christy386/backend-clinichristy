# Generated by Django 3.2.19 on 2023-06-30 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('typeOf', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('number', models.IntegerField()),
                ('street', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phoneNumber', models.IntegerField()),
                ('instagram', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('workDays', models.JSONField()),
                ('servicesPerDay', models.IntegerField()),
                ('workStartTime', models.TimeField()),
                ('serviceDay', models.DateTimeField()),
                ('patient', models.IntegerField()),
                ('medic', models.IntegerField()),
            ],
        ),
    ]
