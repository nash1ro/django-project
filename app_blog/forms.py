# В forms.py

from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    class Meta:
        model = ArticleImage
        fields = '__all__'
    
    # В цьому випадку ми не будемо використовувати multiple в віджетах
    image = forms.FileField()
