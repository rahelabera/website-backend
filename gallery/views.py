from rest_framework import generics
from .models import Slide
from .serializers import SlideSerializer

class SlideListView(generics.ListAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer