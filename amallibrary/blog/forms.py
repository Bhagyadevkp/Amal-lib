from django import forms
from django.shortcuts import redirect, render
from django.views import View
from blog.models import Blogpost
from ckeditor_uploader.fields import RichTextUploadingField




class BlogForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'w-100 outline-none border-2 rounded-full text-center','placeholder':'Enter Title'}))
    image=forms.ImageField(widget=forms.FileInput(attrs={'class':'w-40 outline-none border-2  text-center','placeholder':'Enter Image'}))
    class Meta:
        model = Blogpost
        fields = ['title', 'body', 'image']
        
        
        
