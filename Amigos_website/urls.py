from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Amigos Website Admin"
admin.site.index_title = "Admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gallery.urls')),
    path('api/', include('membership.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/', include('announcements.urls')),
    path('api/', include('events.urls')),
    path('api/', include('jobs.urls')),
    path('api/', include('faqs.urls')),
    path('api/', include('testimonial.urls')),
    path('api/', include('awardsAndCertificates.urls')),
    path('api/', include('departments.urls')),
    path('api/', include('leadership.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
