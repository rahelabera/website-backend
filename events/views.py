from rest_framework import viewsets
from .models import Month, Event
from .serializers import MonthSerializer, EventSerializer

class MonthViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer