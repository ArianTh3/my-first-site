# Generated by Django 3.2.20 on 2023-08-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_comment_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='comment',
            name='login_required',
            field=models.BooleanField(default=False),
        ),
    ]
