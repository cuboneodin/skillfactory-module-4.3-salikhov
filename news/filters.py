import django.forms
from django_filters import FilterSet, DateFilter
from .models import *


class PostFilter(FilterSet):
    time_in = DateFilter(
        lookup_expr='gt',
        widget=django.forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
            'categoryType': ['exact'],

        }