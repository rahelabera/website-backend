from django.urls import path
from .views import AwardListCreateView, CertificateListCreateView

urlpatterns = [
    path('awards/', AwardListCreateView.as_view(), name='award-list-create'),
    path('certificates/', CertificateListCreateView.as_view(), name='certificate-list-create'),
]
