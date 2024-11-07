from rest_framework import generics
from .models import Award, Certificate
from .serializers import AwardSerializer, CertificateSerializer

class AwardListCreateView(generics.ListCreateAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class CertificateListCreateView(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
