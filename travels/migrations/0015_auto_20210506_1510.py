# Generated by Django 3.1.7 on 2021-05-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0014_trippicture_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='all_inclusive_description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Opis all inclusive'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='beach_description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Opis Plaży'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='benefits_description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Swiadczenia'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='for_free_description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Gratisy'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='head_description',
            field=models.TextField(max_length=2000, verbose_name='Główny opis'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='hotel_description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Opis Hotelu'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='hotelstars',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='Gwiazdki hotelu'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='location_description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Opis miejsca'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='room_description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Opis pokoju'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='sport_and_entertainment_description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Sport i rozrywka'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_plan_description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Plan wycieczki'),
        ),
    ]
