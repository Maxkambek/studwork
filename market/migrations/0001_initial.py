# Generated by Django 4.1.2 on 2022-10-29 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
        ('user', '0002_verifyphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=221)),
                ('univer_name', models.CharField(max_length=120)),
                ('course', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=0)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('list_lit', models.TextField()),
                ('is_top', models.BooleanField(default=False)),
                ('views', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.worktype')),
            ],
        ),
        migrations.CreateModel(
            name='MarketFileDone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='market_files/')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_done', to='market.market')),
            ],
        ),
        migrations.CreateModel(
            name='MarketFileDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='market_files/')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_demo', to='market.market')),
            ],
        ),
    ]
