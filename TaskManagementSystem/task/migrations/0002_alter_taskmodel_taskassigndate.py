# Generated by Django 4.2.7 on 2023-12-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='taskAssignDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
