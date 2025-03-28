# Generated by Django 2.2.28 on 2025-03-11 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('CourseID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('UserID', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=200)),
                ('YearEnrolled', models.IntegerField()),
                ('CurrentYearStudent', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('DateUploaded', models.DateTimeField(auto_now_add=True)),
                ('Topics', models.CharField(max_length=200)),
                ('NoteID', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='Documents/')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Courses')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Students')),
            ],
        ),
        migrations.CreateModel(
            name='Enrolls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Courses')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Students')),
            ],
        ),
        migrations.CreateModel(
            name='EditedNotes',
            fields=[
                ('EditedID', models.AutoField(primary_key=True, serialize=False)),
                ('DateUploaded', models.DateField(auto_now_add=True)),
                ('file', models.FileField(null=True, upload_to='Edited_Note/')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Courses')),
                ('NoteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Note')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Students')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Question')),
            ],
        ),
    ]
