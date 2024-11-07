from django.db import models

class Committee(models.Model):
    name_en = models.CharField("Name (English)", max_length=255)
    name_am = models.CharField("Name (Amharic)", max_length=255)

    def __str__(self):
        return self.name_en

class LeadershipMember(models.Model):
    committee = models.ForeignKey(Committee, related_name='members', on_delete=models.CASCADE)
    name_en = models.CharField("Name (English)", max_length=255)
    name_am = models.CharField("Name (Amharic)", max_length=255)
    title_en = models.CharField("Title (English)", max_length=255)
    title_am = models.CharField("Title (Amharic)", max_length=255)
    image = models.ImageField(upload_to='leadership/')

    def __str__(self):
        return self.name_en

    class Meta:
        ordering = ['name_en']