# Generated by Django 4.1.2 on 2022-10-10 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlwenNetworkDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('pobox', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('phone1', models.CharField(max_length=50)),
                ('phone2', models.CharField(max_length=50)),
                ('logo', models.FileField(blank=True, null=True, upload_to='myfiles/')),
            ],
        ),
        migrations.CreateModel(
            name='AlwenNetworkScopeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]