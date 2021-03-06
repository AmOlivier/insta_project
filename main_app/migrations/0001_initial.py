# Generated by Django 2.1.5 on 2019-01-27 12:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 1, 27, 12, 8, 24, 317368))),
            ],
        ),
        migrations.CreateModel(
            name='NewPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('picture', models.ImageField(upload_to='post_pictures')),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 1, 27, 12, 8, 24, 316055))),
                ('liked_by', models.ManyToManyField(blank=True, related_name='likes', to='profile_app.ProfileInfo')),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='profile_app.ProfileInfo')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='main_app.NewPost'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.ProfileInfo'),
        ),
    ]
