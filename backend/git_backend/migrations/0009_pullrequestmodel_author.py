# Generated by Django 4.0.1 on 2022-01-14 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('git_backend', '0008_alter_pullrequestmodel_base_branch_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pullrequestmodel',
            name='author',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
