from django_filters import FilterSet
from .models import *

class OrderFilterSet(FilterSet):

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer',]
