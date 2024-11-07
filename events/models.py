from django.db import models

class Month(models.Model):
    name_en = models.CharField(max_length=50)
    name_am = models.CharField(max_length=50)

    def __str__(self):
        return self.name_en

class Event(models.Model):
    month = models.ForeignKey(Month, related_name='events', on_delete=models.CASCADE)
    date = models.CharField(max_length=10)
    name_en = models.CharField(max_length=100)
    name_am = models.CharField(max_length=100)
    for_content = models.BooleanField(default=False)
    for_event = models.BooleanField(default=False)

    def __str__(self):
        return self.name_en