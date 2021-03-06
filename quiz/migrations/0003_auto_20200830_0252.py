# Generated by Django 2.2 on 2020-08-30 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200829_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_minute', models.IntegerField(default=3)),
                ('time_second', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_option',
            field=models.CharField(help_text='Note: It should be a duplicate of an option listed above', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(help_text='option', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(help_text='option', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(help_text='option', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(help_text='option', max_length=200),
        ),
    ]
