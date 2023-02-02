# Generated by Django 3.2.6 on 2021-09-01 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20210721_0424'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=100, null=True)),
                ('modified_time', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=25, unique=True)),
                ('key', models.CharField(blank=True, max_length=48, unique=True)),
                ('expiration', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='role',
            name='can_manage_api_keys',
            field=models.BooleanField(default=False),
        ),
    ]
