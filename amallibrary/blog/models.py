import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


# BLOGPOSTS RELATED MODELS STARTS HERE

class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Blogpostcomment(models.Model):
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    author = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.comment


# BLOGPOSTS RELATED MODELS ENDS HERE

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
