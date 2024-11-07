from django.db import models
from django.utils.translation import gettext_lazy as _

class JobPost(models.Model):
    title_en = models.CharField( "Title (English)", max_length=255)
    title_am = models.CharField("Title (Amharic)", max_length=255)
    location_en = models.CharField("Location (English) ",max_length=255)
    location_am = models.CharField("Location (Amharic)",max_length=255)
    type = models.CharField(max_length=50)
    posted = models.DateField()
    description_en = models.TextField("Description (English)")
    description_am = models.TextField("Description (Amharic)")
    details_en = models.TextField("Details (English)")
    details_am = models.TextField("Details (Amharic)")

    def __str__(self):
        return self.title_en
    class Meta:
        ordering = ['title_en']