# Generated by Django 4.2.4 on 2024-01-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='gender',
            field=models.CharField(choices=[('man', 'Мужчинам'), ('woman', 'Женщинам'), ('boy', 'Мальчикам'), ('girl', 'Девочкам')], max_length=5, verbose_name='Пол'),
        ),
    ]
