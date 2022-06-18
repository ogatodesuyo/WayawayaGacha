from django import forms


class BudgetInputForm():
    budget = forms.IntegerField(initial='3000')