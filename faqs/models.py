from django.db import models
from django.utils.translation import gettext_lazy as _

class FAQ(models.Model):
    question_en = models.CharField("Question (English)",max_length=255)
    question_am = models.CharField("Question (Amharic)", max_length=255)
    answer_en = models.TextField("Answer (English)")
    answer_am = models.TextField("Answer (Amharic)")

    def __str__(self):
        return self.question_en
    
    class Meta:
        ordering = ['question_en']
