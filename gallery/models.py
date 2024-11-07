from django.db import models

class Slide(models.Model):
    text_en = models.TextField("Text (English)")
    text_am = models.TextField("Text (Amharic)")

    def __str__(self):
        return self.text_en[:50]

class SlideImage(models.Model):
    slide = models.ForeignKey(Slide, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='slides/')

    def __str__(self):
        return f"Image for slide: {self.slide.text_en[:50]}"
