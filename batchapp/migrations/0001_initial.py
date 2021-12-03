# Generated by Django 3.1 on 2021-12-03 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batch_id', models.AutoField(primary_key=True, serialize=False)),
                ('batch_name', models.CharField(max_length=20)),
                ('number_of_code', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('code_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='batchapp.batch')),
            ],
        ),
    ]
