from django.contrib.auth import get_user_model
from rest_framework import serializers

class GardenerSerializer(serializers.ModelSerializer):
    class Meta:
        # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.get_user_model
        model = get_user_model()
        fields = ('id', 'user_name', 'email', 'zipcode')
        extra_kwargs = { 
            'password': { 
                'write_only': True, 'min_length': 5 
                } 
            }

    # This create method will be used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)