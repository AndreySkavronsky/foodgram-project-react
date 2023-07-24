from django_filters.rest_framework import filters, FilterSet

from recipes.models import Recipe, Tag


class RecipeFilter(FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all()
    )
    is_favorited = filters.BooleanFilter(method='get_is_favorited')
    is_in_shopping_cart = filters.BooleanFilter(
        method='get_is_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author', 'is_favorited', 'is_in_shopping_cart',)

    def get_is_favorited(self, queryset, name, value):
        user = self.request.user
        return queryset.filter(favorite_recipe__user=user) \
            if user.is_authenticated else queryset

    def get_is_in_shopping_cart(self, queryset, name, value):
        user = self.request.user
        return queryset.filter(shopping_recipe__user=user) \
            if user.is_authenticated else queryset
