# Generated by Django 4.0.2 on 2022-02-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_description', models.TextField()),
            ],
            options={
                'db_table': 'Task',
            },
        ),
    ]
