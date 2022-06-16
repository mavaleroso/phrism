# Generated by Django 4.0.3 on 2022-03-21 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_employeeappstatus_employeefundsource_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('attachments', models.FileField(upload_to='events/documents')),
                ('event_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.authuser')),
            ],
            options={
                'db_table': 'tbl_events',
            },
        ),
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('attachments', models.FileField(upload_to='announcement/documents')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.authuser')),
            ],
            options={
                'db_table': 'tbl_announcements',
            },
        ),
    ]