# Generated by Django 4.0.4 on 2022-05-05 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='rest.team'),
            preserve_default=False,
        ),
    ]
