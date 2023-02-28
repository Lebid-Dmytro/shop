from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm

from myshop.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'id': 'textid'}),
            'photo_comments': forms.FileInput(attrs={'id': 'photo_commentsid'}),
            'file_comments': forms.FileInput(attrs={'id': 'file_commentsid'})

        }
