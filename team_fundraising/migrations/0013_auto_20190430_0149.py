# Generated by Django 2.2 on 2019-04-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_fundraising', '0012_auto_20190221_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundraiser',
            name='message',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
