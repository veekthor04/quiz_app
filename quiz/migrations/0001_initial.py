# Generated by Django 2.2 on 2020-08-28 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passage_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(help_text='Correct option', max_length=200)),
                ('option2', models.CharField(help_text='Incorrect option', max_length=200)),
                ('option3', models.CharField(help_text='Incorrect option', max_length=200)),
                ('option4', models.CharField(help_text='Incorrect option', max_length=200)),
                ('passage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Passage')),
            ],
        ),
    ]