from django.db import models

class Testimonial(models.Model):
    name_en = models.CharField("Name (English)",max_length=255)
    name_am = models.CharField("Name (Amharic)",max_length=255)
    role_en = models.CharField("Role (English)",max_length=255)
    role_am = models.CharField("Role (Amharic)",max_length=255)
    quote_en = models.TextField("Quote (English)")
    quote_am = models.TextField("Quote (Amharic)")
    photo = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.name_en
