# Generated by Django 4.0.1 on 2022-02-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gf', '0008_user_cur_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='needs_parsing',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddConstraint(
            model_name='follower',
            constraint=models.UniqueConstraint(fields=('target_user', 'user'), name='follower-target-user'),
        ),
        migrations.AddConstraint(
            model_name='following',
            constraint=models.UniqueConstraint(fields=('target_user', 'user'), name='following-target-user'),
        ),
    ]
