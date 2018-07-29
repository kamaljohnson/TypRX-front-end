# Generated by Django 2.0.7 on 2018-07-29 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lobby', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.AddField(
            model_name='chatmessages',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Thread'),
        ),
        migrations.AddField(
            model_name='chatmessages',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lobby.Player'),
        ),
    ]