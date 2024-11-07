from django.db import models

class Award(models.Model):
    name_en = models.CharField("Name (English)",max_length=255)
    name_am = models.CharField("Name (Amharic)", max_length=255)
    date_received = models.DateField("Date Received")
    awarding_body_en = models.CharField("Awarding Body (English)",max_length=255)
    awarding_body_am = models.CharField("Awarding Body (Amharic)",max_length=255)
    description_en = models.TextField("Description (English)") 
    description_am = models.TextField("Description (Amharic)")
    photo = models.ImageField(upload_to='awards/')

    def __str__(self):
        return f"{self.name_en} ({self.name_am})"

class Certificate(models.Model):
    name_en = models.CharField("Name (English)",max_length=255)
    name_am = models.CharField("Name (Amharic)",max_length=255)
    date_issued = models.DateField("Date Issued")
    issuing_organization_en = models.CharField("Issuing Organization (English)", max_length=255)
    issuing_organization_am = models.CharField("Issuing Organization (Amharic)", max_length=255,)
    description_en = models.TextField("Description (English)")
    description_am = models.TextField("Description (Amharic)")
    photo = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return f"{self.name_en} ({self.name_am})"
    class Meta:
        ordering = ['name_en']
