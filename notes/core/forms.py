from django import forms
from .models import Note
from ckeditor.widgets import CKEditorWidget


class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    COLOR_CHOICES = (
        ('default', 'Padrão'),
        ('blue', 'Azul'),
        ('red', 'Vermelho'),
        ('yellow', 'Amarelo'),
    )
    color = forms.ChoiceField(widget=forms.RadioSelect ,choices=COLOR_CHOICES)
    class Meta:
        model = Note
        fields = ('author', 'title', 'content', 'color')
