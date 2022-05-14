from django import forms
from .models import Page

class Pageform(forms.ModleForm);

  class Meta;
    model=Page
    fields=['title','content','score']
    title=forms.CharField()
    content=forms.CharField()
    score=forms.IntegerField()