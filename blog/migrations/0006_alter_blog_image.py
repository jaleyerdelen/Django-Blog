# Generated by Django 4.1.2 on 2022-12-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blogs'),
        ),
    ]
