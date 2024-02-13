# Generated by Django 4.2.6 on 2024-02-09 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_rename_is_delete_category_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_deleted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_app.category')),
            ],
        ),
    ]