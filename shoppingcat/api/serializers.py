from rest_framework import serializers
from cat.models import Clothing, MyClothing, Inspiration, Recommendation

# Serializers to map the Model instance into JSON format

class MyClothingSerializer(serializers.ModelSerializer):

    class Meta: # Meta class to map serializer's fields with the model fields.
        model = MyClothing
        fields = ('name', 'category', 'productURL', 'imageURL', 'price', 'SKUcode', 'user')


class InspirationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inspiration
        fields = ('image', 'user')


class RecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = ('name', 'category', 'productURL', 'imageURL', 'price', 'SKUcode', 'user', 'inspiration')