from rest_framework import serializers

from ads.models import Ad, Compilation


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id", "name"]


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class CompilationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compilation
        fields = ["id", "name"]


class CompilationDetailSerializer(serializers.ModelSerializer):
    items = AdListSerializer(many=True)

    class Meta:
        model = Compilation
        fields = '__all__'


class CompilationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compilation
        fields = '__all__'



        
