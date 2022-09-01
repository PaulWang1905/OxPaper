from django import forms

from .models import Post
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'status':_('Publish'),
        }
        help_texts = {
            'abstract': _('Keep the abstract short'),
            }
        widgets = {'abstract': forms.Textarea(attrs={'rows':4})}