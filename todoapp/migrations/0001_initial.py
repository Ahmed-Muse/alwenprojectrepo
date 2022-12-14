# Generated by Django 4.1.2 on 2022-10-09 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('complete', 'complete'), ('incomplete', 'incomplete')], default='incomplete', max_length=10)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('dueDate', models.DateTimeField(blank=True, null=True)),
                ('taskDay', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=10)),
                ('assignedto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taskassignrelname', to='logistics.alwendriversmodel')),
            ],
        ),
    ]
