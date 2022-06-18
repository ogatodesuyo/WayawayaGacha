from django import forms


class PriceInputForm():
    price = forms.IntegerField(initial='3000')