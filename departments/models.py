from django.db import models

class Department(models.Model):
    name_en = models.CharField(max_length=100, unique=True, verbose_name="Department Name (English)")
    name_am = models.CharField(max_length=100, unique=True, verbose_name="Department Name (Amharic)")
    description_en = models.TextField("Description (English)")
    description_am = models.TextField("Description (Amharic)")
    image = models.ImageField(upload_to='department_images/')
    head_name_en = models.CharField(max_length=100, verbose_name="Head Name (English)")
    head_name_am = models.CharField(max_length=100, verbose_name="Head Name (Amharic)")
    head_email = models.EmailField()
    head_image = models.ImageField(upload_to='department_head_images/')

    def __str__(self):
        return self.name_en  # or conditionally based on language preference

    def get_department_name(self, language='en'):
        """
        Returns the department name based on the selected language.
        """
        if language == 'am':
            return self.name_am
        return self.name_en
