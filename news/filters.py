from django_filters import FilterSet, DateFilter
from .models import Post
from django.forms import DateInput

class PostFilter(FilterSet):
    time_in = DateFilter(
        field_name='time_in',
        widget=DateInput(attrs={'type': 'date'}),
        lookup_expr='date__gte',
        label='Поиск по дате'
    )
    class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'author': ['exact'],
           'time_in': ['gt'],
       }