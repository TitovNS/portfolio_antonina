# Generated by Django 4.0.4 on 2022-04-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_image', models.ImageField(upload_to='works/images')),
                ('video', models.FileField(upload_to='works/video')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(null=True),
        ),
    ]