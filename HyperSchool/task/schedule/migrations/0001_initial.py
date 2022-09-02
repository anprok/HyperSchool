# Generated by Django 2.2 on 2022-08-31 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('info', models.CharField(max_length=1024)),
                ('duration_months', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('about', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('course', models.ManyToManyField(to='schedule.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(to='schedule.Teacher'),
        ),
    ]