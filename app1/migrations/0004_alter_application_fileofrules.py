# Generated by Django 4.2.4 on 2023-08-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_application_fileofrules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='fileOfRules',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
