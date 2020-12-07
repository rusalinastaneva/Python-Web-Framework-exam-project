from django.core.exceptions import ValidationError


def city_start_with_uppercase_letter(value):
    if value.islower():
        raise ValidationError('Please correct the value. City should start with a capital letter!')


def us_zipcode_consists_of_five_digits(value):
    if len(value) != 5:
        raise ValidationError('Please correct the value. Zipcode consists of 5 digits!')


def validate_price_is_negative_or_zero(value):
    if value <= 0:
        raise ValidationError('Please insert a positive value. Price cannot be negative or zero!')


def validate_bedrooms_is_negative_or_zero(value):
    if value <= 0:
        raise ValidationError('Please insert a positive value. Bedrooms cannot be negative or zero!')


def validate_bathrooms_is_negative_or_zero(value):
    if value <= 0:
        raise ValidationError('Please insert a positive value. Bedrooms cannot be negative or zero!')


def validate_garage_is_negative(value):
    if value < 0:
        raise ValidationError('Please insert a positive value. Garage cannot be negative!')


def validate_sqft_is_negative_or_zero(value):
    if value <= 0:
        raise ValidationError('Please insert a positive value. SQFT cannot be negative or zero!')


def validate_lot_size_is_negative_or_zero(value):
    if value <= 0:
        raise ValidationError('Please insert a positive value. Lot size cannot be negative or zero!')
