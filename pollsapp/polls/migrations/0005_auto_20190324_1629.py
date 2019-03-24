# Generated by Django 2.1.4 on 2019-03-24 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190324_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='Enter', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='track',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Track'),
        ),
    ]
