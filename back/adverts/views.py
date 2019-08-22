from rest_framework.response import Response
from rest_framework.views import APIView
from adverts.models import Advert, Instrument
from adverts.serializers import AdvertSerializer, InstrumentSerializer, EmailFormSerializer
from rest_framework.generics import ListAPIView
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import action
from rest_framework import permissions
from django.core.mail import EmailMessage
from django.conf import settings


class AdvertView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    def perform_create(self, serializer):
        obj = serializer.save(user=self.request.user)
        for i in serializer.initial_data['instrument']:
            instrument = Instrument.objects.get(id=i['id'])
            obj.instruments.add(instrument)

    
    @action(detail=False, methods=['post'])
    def search(self, request):
        adverts = Advert.objects.filter(
            lat__range=(request.data['_southWest']['lat'], request.data['_northEast']['lat']),
            lon__range=(request.data['_southWest']['lng'], request.data['_northEast']['lng'])
        )
        return Response(AdvertSerializer(adverts, many=True).data)
    
    @action(detail=True, methods=['post'])
    def email(self, request, pk):
        advert = self.get_object()
        serializer = EmailFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            msg = EmailMessage(
                'RE: ' + advert.title + ' - ' + serializer.data['name'],
                serializer.data['message'] + '\n\nFrom: ' + serializer.data['name'],
                to=[advert.user.email],
                reply_to=[serializer.data['email']]
            )
            msg.send()
        return Response()
    

class InstrumentView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
