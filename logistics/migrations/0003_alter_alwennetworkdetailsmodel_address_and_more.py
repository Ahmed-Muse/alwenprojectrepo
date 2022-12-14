# Generated by Django 4.1.2 on 2022-10-10 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0002_alwennetworkdetailsmodel_alwennetworkscopemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alwennetworkdetailsmodel',
            name='address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alwennetworkdetailsmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alwennetworkdetailsmodel',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alwennetworkdetailsmodel',
            name='phone1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alwennetworkdetailsmodel',
            name='phone2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alwennetworkdetailsmodel',
            name='pobox',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alwennetworkdetailsmodel',
            name='website',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alwennetworkscopemodel',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
