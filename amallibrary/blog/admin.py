from django.contrib import admin
from blog.models import *

# Register your models here.

admin.site.register(Blogpost)
admin.site.register(Blogpostcomment)
admin.site.register(Feedback)
admin.site.register(Notice)