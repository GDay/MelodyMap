from rest_framework import serializers
from adverts.models import Advert, Instrument
from back.validators import validate_hcaptcha

class EmailFormSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=1000)
    hcaptcha = serializers.CharField(max_length=4000, validators=[validate_hcaptcha])


class InstrumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instrument
        fields = '__all__'


class AdvertSerializer(serializers.HyperlinkedModelSerializer):
    hover = serializers.BooleanField(default=False, read_only=True)
    instruments = InstrumentSerializer(many=True, read_only=True)

    class Meta:
        model = Advert
        fields = ('id', 'title', 'description', 
                  'lon', 'lat', 'date_added', 'hover',
                  'min_age', 'max_age', 'is_band', 'instruments')


