from django.core.exceptions import ValidationError
from django import forms
from .models import *
import re


class VisitForm(forms.ModelForm):
    visit_first_name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-input firstname',
        'placeholder': 'Имя',
        'autofocus': True
    }))
    visit_last_name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-input lastname',
        'placeholder': 'Фамилия'
    }))
    visit_patronymic = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-input patronymic',
        'placeholder': 'Отчество'
    }))
    visit_email = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-input email',
        'placeholder': 'Почта'
    }))
    visit_phone = forms.CharField(label='', widget=forms.NumberInput(attrs={
        'class': 'form-input',
        'placeholder': 'Номер телефона'
    }))

    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, *kwargs)
        self.fields['services'].empty_label = "Услуга не выбрана"
        self.fields['addresses'].empty_label = "Адрес не выбран"

    def clean_visit_phone(self):
        phone = self.cleaned_data['visit_phone']
        re_phone = r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$"
        if not re.match(re_phone, phone):
            raise ValidationError('Неправильно набран номер')
        return phone

    class Meta:
        model = Visit
        fields = ('visit_first_name', 'visit_last_name', 'visit_patronymic', 'visit_email', 'visit_phone', 'services', 'addresses')



