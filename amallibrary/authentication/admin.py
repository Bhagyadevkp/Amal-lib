from django.contrib import admin

from authentication.models import *

# Register your models here.
admin.site.register(students)
admin.site.register(staffs)
admin.site.register(quesadmin)
admin.site.register(posts)
admin.site.register(department)
admin.site.register(subjects)
admin.site.register(courses)