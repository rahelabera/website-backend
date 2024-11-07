from django import forms
from .models import Slide

class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['text_en', 'text_am', 'images']  # Include the images field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].widget.attrs.update({'multiple': True})  # Allow multiple file uploads
