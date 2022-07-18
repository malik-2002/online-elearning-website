# Generated by Django 4.0.2 on 2022-06-08 10:43

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('blog_content', ckeditor.fields.RichTextField()),
                ('thumbnail', models.ImageField(upload_to='static/upload/')),
                ('is_show', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=50)),
                ('email', models.EmailField(editable=False, max_length=250)),
                ('subject', models.TextField(editable=False)),
                ('contact_id', models.CharField(editable=False, max_length=50, unique=True)),
                ('receiving_time', models.CharField(editable=False, max_length=85)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(help_text='Enter The Course Title At Least 10 Words', max_length=30)),
                ('course_slug', models.SlugField(unique=True)),
                ('course_about', models.CharField(help_text='Enter The Course Details At Least 20 Words', max_length=100)),
                ('what_we_learn', ckeditor.fields.RichTextField()),
                ('course_thumbnail', models.ImageField(upload_to='static/upload/')),
                ('course_join', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('article', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video_id', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course_detail')),
            ],
        ),
    ]
