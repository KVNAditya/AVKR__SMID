# Generated by Django 2.0.5 on 2019-04-29 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent/py', '0005_clientposts_model_dislikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='review_Model',
            fields=[

                ('uname', models.CharField(max_length=100)),
                ('ureview', models.CharField(max_length=100)),
                ('tname', models.CharField(max_length=300)),
                ('suggestion', models.CharField(max_length=300)),
                ('dt', models.CharField(max_length=300)),
                ('sanalysis', models.CharField(max_length=300)),
            ],
        ),
    ]
