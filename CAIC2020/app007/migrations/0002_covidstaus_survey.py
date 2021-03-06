# Generated by Django 3.1.7 on 2021-03-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app007', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidStaus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('User is Safe', 'User is Safe'), ('User is in Qurantine', 'User is in Qurantine'), ('User is Infected', 'User is Infected')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
