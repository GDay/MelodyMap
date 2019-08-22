from rest_framework import serializers
from users.models import User
from back.validators import validate_hcaptcha

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    hcaptcha = serializers.CharField(max_length=4000, read_only=True, validators=[validate_hcaptcha])

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'hcaptcha')