# Generated by Django 3.2.20 on 2023-11-06 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anganwadi_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anganwadiname', models.CharField(max_length=90)),
                ('photo', models.FileField(upload_to='')),
                ('place', models.CharField(max_length=90)),
                ('post', models.CharField(max_length=90)),
                ('pin', models.BigIntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='fooditems_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fooditem', models.CharField(max_length=90)),
                ('time', models.TimeField(max_length=90)),
                ('day', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='login_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=90)),
                ('password', models.CharField(max_length=90)),
                ('type', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='staff_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=90)),
                ('lastname', models.CharField(max_length=90)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=90)),
                ('post', models.CharField(max_length=90)),
                ('pin', models.BigIntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=90)),
                ('photo', models.FileField(upload_to='')),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eanaganavadiapp.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='syllabus_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=90)),
                ('syllabus', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='workingtime_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromtime', models.TimeField()),
                ('totime', models.TimeField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='studymaterials_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studymaterials', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=90)),
                ('STAFF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eanaganavadiapp.staff_table')),
            ],
        ),
        migrations.CreateModel(
            name='student_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=90)),
                ('lastname', models.CharField(max_length=90)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=90)),
                ('post', models.CharField(max_length=90)),
                ('parentname', models.CharField(max_length=90)),
                ('pin', models.BigIntegerField()),
                ('phone', models.BigIntegerField()),
                ('photo', models.FileField(upload_to='')),
                ('email', models.CharField(max_length=90)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eanaganavadiapp.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='leaverequest_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levedate', models.DateField()),
                ('request', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('STUDENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eanaganavadiapp.student_table')),
            ],
        ),
        migrations.CreateModel(
            name='feedback_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('rating', models.IntegerField()),
                ('STUDENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eanaganavadiapp.student_table')),
            ],
        ),
        migrations.CreateModel(
            name='complaints_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('reply', models.CharField(max_length=90)),
                ('STUDENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eanaganavadiapp.student_table')),
            ],
        ),
        migrations.CreateModel(
            name='chat_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('FROM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a', to='Eanaganavadiapp.login_table')),
                ('TO_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b', to='Eanaganavadiapp.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='assign_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('ANGANWADI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eanaganavadiapp.anganwadi_table')),
                ('STAFF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eanaganavadiapp.staff_table')),
            ],
        ),
    ]
