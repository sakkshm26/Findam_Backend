from rest_framework import serializers
from .models import Cs,Blockchain,Electronics,Entrepreneurship,Web3

class CsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cs
        fields = '__all__'

class BlockchainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blockchain
        fields = '__all__'

class ElectronicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electronics
        fields = '__all__'

class EntrepreneurshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneurship
        fields = '__all__'

class Web3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Web3
        fields = '__all__'