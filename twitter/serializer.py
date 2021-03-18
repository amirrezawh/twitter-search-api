from rest_framework import serializers
from .models import TweetModel

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetModel
        #fields = '__all__'
        fields = ('SearchKeys', 'TweetNumber')

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetModel
        fields = '__all__'