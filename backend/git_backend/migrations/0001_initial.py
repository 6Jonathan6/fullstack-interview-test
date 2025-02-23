# Generated by Django 4.0.1 on 2022-01-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('OP', 'OPEN'), ('CL', 'CLOSED'), ('MR', 'MERGED')], default='OP', max_length=2)),
                ('base_branch_name', models.CharField(max_length=200)),
                ('compare_branch_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
