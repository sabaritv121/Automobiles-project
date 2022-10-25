import django_filters
from django import forms
from django_filters import CharFilter

from auto_app.models import Request


# class StatusFilter(django_filters.FilterSet):
#         name= CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
#         'placeholder': 'search customer name', 'class': 'form-control'}))
#            class Meta:
#              model = Request
#              fields = ('name',)
#
class StatusFilter(django_filters.FilterSet):
    customer__name = CharFilter(field_name='customer__name', label="", lookup_expr='icontains',
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'Search Customer Name', 'class': 'form-control'}))

    class Meta:
        model = Request
        fields = ('customer__name',)