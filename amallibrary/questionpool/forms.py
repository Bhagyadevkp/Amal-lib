import json
from tkinter import Widget
from django import forms
from .models import *
from django.forms import NumberInput, TextInput,Select

class Qform(forms.ModelForm):
    question_subject = forms.ModelChoiceField(queryset=subjects.objects.all(),empty_label="Subject",widget=Select(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Subject',}))
    question_department = forms.ModelChoiceField(queryset=department.objects.all(),empty_label="Department",widget=Select(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Department'}))
    class Meta:
        model = question
        fields = ['question_ques','question_answer','question_subject','question_department']





class Qviewform(forms.Form):
    dsubjects = {}
    dsubjid = {}
    list_subjects = []
    list_subjid = []
    for subject in subjects.objects.all():
        if subject.department.department in dsubjects:
            dsubjects[subject.department.department].append(subject.subject)
        else:
            dsubjects[subject.department.department]=[subject.subject]
        list_subjects.append((subject.subject,subject.subject))

        if subject.department.department in dsubjid:
            dsubjid[subject.department.department].append(subject.id)
        else:
            dsubjid[subject.department.department]=[subject.id]
        list_subjid.append((subject.id,subject.id))
    departments = [str(department) for department in department.objects.all()]
    departmentsid=[str(department.id) for department in department.objects.all()]

    subject_select = forms.ChoiceField(widget=Select(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Subject'}))
    department_select = forms.ChoiceField(widget=Select(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Department'}))

    departments = json.dumps(departments)
    subjects = json.dumps(dsubjects)
    subjid= json.dumps(dsubjid)


    class Meta:
        fields = ['subject','department']
        dsubjects = {}
        dsubjid = {}
        list_subjects = []
        list_subjid = []
        for subject in subjects.objects.all():
            if subject.department.department in dsubjects:
                dsubjects[subject.department.department].append(subject.subject)
            else:
                dsubjects[subject.department.department]=[subject.subject]
            list_subjects.append((subject.subject,subject.subject))

            if subject.department.department in dsubjid:
                dsubjid[subject.department.department].append(subject.id)
            else:
                dsubjid[subject.department.department]=[subject.id]
            list_subjid.append((subject.id,subject.id))
        departments = [str(department) for department in department.objects.all()]
        departmentsid=[str(department.id) for department in department.objects.all()]

        widgets = {
            'department_select': Select(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Subject'},choices=([(department, department) for department in departments])),
            'subject_select': Select(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Subject'},choices=list_subjects),
        }