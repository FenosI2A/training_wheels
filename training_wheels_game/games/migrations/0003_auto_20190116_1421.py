# Generated by Django 2.1.5 on 2019-01-16 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20190116_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='active_player',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_is_active', to=settings.AUTH_USER_MODEL),
        ),
    ]
