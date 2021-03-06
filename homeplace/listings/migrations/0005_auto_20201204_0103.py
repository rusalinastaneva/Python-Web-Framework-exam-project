# Generated by Django 3.1.3 on 2020-12-04 07:03

from django.db import migrations, models

from homeplace.listings import validators


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20201204_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(validators=[validators.validate_bathrooms_is_negative_or_zero]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=100, validators=[
                validators.city_start_with_uppercase_letter]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(validators=[validators.validate_garage_is_negative]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, max_digits=5, validators=[
                validators.validate_lot_size_is_negative_or_zero], verbose_name='Lot size (Acres)'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(validators=[validators.validate_price_is_negative_or_zero]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(validators=[validators.validate_sqft_is_negative_or_zero]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(max_length=20, validators=[
                validators.us_zipcode_consists_of_five_digits]),
        ),
    ]
