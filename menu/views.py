from django.db.models import Count, Q
from rest_framework.generics import ListAPIView
from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodCategoryListView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        queryset = FoodCategory.objects.annotate(num_foods=Count('food', filter=Q(food__is_publish=True))).filter(num_foods__gt=0)
        return queryset
