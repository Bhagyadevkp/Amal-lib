import datetime
from pyexpat import model
from django.db import models
from authentication.models import *
from ckeditor_uploader.fields import RichTextUploadingField







# Create your models here.
class question(models.Model):
    question_num = models.AutoField(primary_key=True)
    question_ques = RichTextUploadingField()
    question_answer = RichTextUploadingField()
    question_subject = models.ForeignKey(subjects, on_delete=models.CASCADE)
    question_department = models.ForeignKey(department, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    def __str__(self):
        return self.question_num




