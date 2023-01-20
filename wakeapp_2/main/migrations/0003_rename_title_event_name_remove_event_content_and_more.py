# Generated by Django 4.1.5 on 2023-01-19 20:17

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0002_eventvisibility"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="title",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="event",
            name="content",
        ),
        migrations.RemoveField(
            model_name="event",
            name="friends",
        ),
        migrations.RemoveField(
            model_name="event",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="event",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="event",
            name="location",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="event",
            name="visible_to",
            field=models.ManyToManyField(
                related_name="visible_events",
                through="main.EventVisibility",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
