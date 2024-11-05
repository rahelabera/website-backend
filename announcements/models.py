from django.db import models
from django.utils import timezone

class Announcement(models.Model):
    date = models.DateField(default=timezone.now)
    title_en = models.CharField("Title (English)",max_length=255)
    title_am = models.CharField("Title (Amharic)",max_length=255)
    description_en = models.TextField("Description (English)")
    description_am = models.TextField("Description (Amharic)")
    image = models.ImageField(upload_to='images/')

    def str(self):
        return  f"{self.title_en} ({self.title_am})"
    
    class Meta:
        ordering = ['title_en']