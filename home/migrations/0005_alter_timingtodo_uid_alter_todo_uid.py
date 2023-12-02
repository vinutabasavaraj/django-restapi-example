# Generated by Django 4.2.5 on 2023-12-02 10:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_todo_user_alter_timingtodo_uid_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('f2cd5441-950a-44e6-b617-5412977772ec'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('f2cd5441-950a-44e6-b617-5412977772ec'), editable=False, primary_key=True, serialize=False),
        ),
    ]