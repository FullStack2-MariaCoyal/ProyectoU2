from django import forms
from .models import PostMonster, PostSurvivor


class UploadImage(forms.ModelForm):

    class Meta:
        model = PostMonster
        fields = ['image']
