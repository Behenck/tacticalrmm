# Generated by Django 3.1.7 on 2021-02-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0011_auto_20201119_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingaction',
            name='action_type',
            field=models.CharField(blank=True, choices=[('schedreboot', 'Scheduled Reboot'), ('taskaction', 'Scheduled Task Action'), ('agentupdate', 'Agent Update'), ('chocoinstall', 'Chocolatey Software Install')], max_length=255, null=True),
        ),
    ]
