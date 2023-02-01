from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Note

class NoteForm(forms.ModelForm):    
    class Meta:
        model = Note
        fields = ("__all__")  # все поля
        widgets = {
            'text_content': forms.Textarea(attrs={'cols': 20, 'rows': 3}),
        }
        labels = {"text_content": _('')}
