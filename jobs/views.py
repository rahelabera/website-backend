from rest_framework import viewsets
from .models import JobPost
from .serializers import JobPostSerializer

class JobPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
