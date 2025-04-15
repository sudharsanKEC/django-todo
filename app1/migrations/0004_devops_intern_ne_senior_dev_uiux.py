# Generated by Django 5.2 on 2025-04-15 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_spm_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='DEVOPS',
            fields=[
                ('dops_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('dops_cto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dops_cto', to='app1.cto')),
                ('dops_spm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dops_spm', to='app1.spm')),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('intern_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('intern_cto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intern_cto', to='app1.cto')),
                ('intern_spm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intern_spm', to='app1.spm')),
            ],
        ),
        migrations.CreateModel(
            name='NE',
            fields=[
                ('ne_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('ne_cto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ne_cto', to='app1.cto')),
                ('ne_spm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ne_spm', to='app1.spm')),
            ],
        ),
        migrations.CreateModel(
            name='Senior_dev',
            fields=[
                ('sde_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('sde_cto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sde_cto', to='app1.cto')),
                ('sde_spm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sde_spm', to='app1.spm')),
            ],
        ),
        migrations.CreateModel(
            name='UIUX',
            fields=[
                ('uiux_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100, null=True)),
                ('uiux_cto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uiux_cto', to='app1.cto')),
                ('uiux_spm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uiux_spm', to='app1.spm')),
            ],
        ),
    ]
