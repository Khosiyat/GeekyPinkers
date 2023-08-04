# Generated by Django 4.2.2 on 2023-07-01 06:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('worked_fields', models.PositiveIntegerField(choices=[(0, 'Worked_fields'), (1, 'Game_development'), (2, 'Software_Developer'), (3, 'Data_science'), (4, 'Mobile_app_development'), (5, 'Data_analysis'), (6, 'Front_end_web_development'), (7, 'Back_end_web_development'), (8, 'Web_design'), (9, 'Machine_learning'), (10, 'Cloud_computing'), (11, 'User_experience_design'), (12, 'Software_Architect'), (13, 'Computer_network'), (14, 'Network_administrator'), (15, 'User_interface_design'), (16, 'Information_technology_management')], null=True)),
                ('academic_fields', models.PositiveIntegerField(choices=[(0, 'None'), (1, 'Math'), (2, 'biology'), (3, 'chemistry'), (4, 'art'), (5, 'physics'), (6, 'History'), (7, 'literature'), (8, 'Business'), (9, 'Social_Sciences'), (10, 'Psychology'), (11, 'Communication'), (12, 'CS'), (13, 'linguistics')], null=True)),
                ('worked_industry', models.PositiveIntegerField(choices=[(0, 'None'), (1, 'Transport'), (2, 'Electronics'), (3, 'Agriculture'), (4, 'Food'), (5, 'Pharmaceutical'), (6, 'Education'), (7, 'Energy'), (8, 'Media'), (9, 'Healthcare'), (10, 'Computer'), (11, 'Entertainment'), (12, 'Construction'), (13, 'Telecommunication'), (14, 'Manufacturing'), (15, 'Music'), (16, 'Aerospace'), (17, 'Entertainment'), (18, 'Mining'), (19, 'Hospitality')], null=True)),
                ('invested_time', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('predictions', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
