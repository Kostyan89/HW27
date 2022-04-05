from rest_framework import serializers

from ads.models import Ad, Compilation


class NotTrueValidator:
    def __call__(self, value):
        if value:
            raise serializers.ValidationError("New Ad can not be published")


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


class AdCreateSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(validators=[NotTrueValidator()])

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



        
