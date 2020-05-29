# Generated by Django 3.0.6 on 2020-05-28 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_auto_20200528_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=250, verbose_name='')),
                ('company', models.CharField(max_length=250, verbose_name='')),
                ('description', models.TextField(verbose_name='')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.City', verbose_name='')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.Language', verbose_name='')),
            ],
        ),
    ]