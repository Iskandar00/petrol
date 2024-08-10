from django.core.validators import RegexValidator


class CarNumberValidator(RegexValidator):
    regex = r'^[(01)|(\d{1}0)|(25)|(75)|(95)]\s\d{3}\s{2}$ | ^[(01)|(\d{1}0)|(25)|(75)|(95)]\d{3}\s{3}$'
    message = 'Car Number was mistake.'
