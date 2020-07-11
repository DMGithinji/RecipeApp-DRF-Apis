from rest_framework import serializers

from core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_on_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """"Serialize ingredient object"""

    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_on_fields = ('id',)
