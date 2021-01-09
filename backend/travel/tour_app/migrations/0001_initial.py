# Generated by Django 3.0.5 on 2020-12-26 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_title', models.CharField(max_length=255)),
                ('tour_overview', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TourIncludesAndExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('is_included', models.BooleanField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_includes_excludes', to='tour_app.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('reviews_user', models.CharField(max_length=25)),
                ('comment', models.TextField(blank=True)),
                ('review_date', models.DateField(auto_now_add=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_review', to='tour_app.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=25)),
                ('longitude', models.CharField(max_length=25)),
                ('location_name', models.CharField(max_length=15)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_map', to='tour_app.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourJourney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journey_title', models.CharField(max_length=150)),
                ('journey_details', models.TextField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_journey', to='tour_app.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_file', models.FileField(null=True, upload_to='gallery/')),
                ('media_file_name', models.CharField(max_length=40)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_gallery', to='tour_app.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_details', to='tour_app.Tour')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tour', to='tour_app.TourCategory'),
        ),
    ]