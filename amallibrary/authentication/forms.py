import json
from django import forms
from .models import *
from django.forms import NumberInput, TextInput,Select


class Depform(forms.ModelForm):
    department_name = forms.CharField(max_length=30,widget=TextInput(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Department'}))
    class Meta:
        model = department
        fields = ['department_name']


class Postform(forms.ModelForm):
    post_name = forms.CharField(max_length=30,widget=TextInput(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Post'}))
    class Meta:
        model = posts
        fields = ['post_name']

class Courseform(forms.ModelForm):
    course_name = forms.CharField(max_length=30,widget=TextInput(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Course'}))
    class Meta:
        model = courses
        fields = ['course_name']

class Subjectform(forms.ModelForm):
    subject_name = forms.CharField(max_length=30,widget=TextInput(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Subject'}))
    class Meta:
        model = subject
        fields = ['subject_name']

        