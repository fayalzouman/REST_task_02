from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from datetime import datetime

from .models import *
from .serializers import *


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer

class BookingDetails(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'

class BookingUpdate(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'	

class BookingDelete(DestroyAPIView):
	queryset = Booking.objects.filter()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'	
