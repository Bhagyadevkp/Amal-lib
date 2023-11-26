from audioop import add
import datetime
from email.headerregistry import Address
from time import timezone
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import *
from django.views import View
from django.contrib.auth.models import User
from authentication.models import *
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View
from blog.models import *

from books.models import *
from questionpool.models import *

# Create your views here.

# INDEX VIEW STARTS HERE

def index(request):
    post = Blogpost.objects.all().order_by('-id')[:5]
    notice = Notice.objects.all().order_by('-id')
    return render(request, 'index.html',{
        'post': post,
        'notice': notice,
    })

# INDEX VIEW ENDS HERE


# ADMIN PAGES RENDER STARTS HERE
def Admindashboard(request):
    user=User.objects.get(pk=request.user.id)
    if user.is_superuser:
        stud=students.objects.all().order_by('student_username__username')
        staf=staffs.objects.all().order_by('staff_username__username')
        return render(request,'admindashboard.html',{
                'stud':stud,
                'staf':staf,
                })
    else:
        return render(request, 'alert.html',{'type':'Adminerror'})

def Adminsettings(request):
    user=User.objects.get(pk=request.user.id)
    if user.is_superuser:
        return render(request,'Adminsettings.html')
    else:
        return render(request, 'alert.html',{'type':'Adminerror'})

def Adminuserview(request):
    if request.user.is_authenticated:
        user=User.objects.get(pk=request.user.id)
        if user.is_superuser:
            stud=students.objects.all().order_by('student_username__username')
            staf=staffs.objects.all().order_by('staff_username__username')
            return render(request,'adminusers.html',{
                'stud':stud,
                'staf':staf,
                })





# ADMIN PAGES RENDER ENDS HERE


# USER REGISTREATION STARTS HERE

def Registrationtype(request):
    return render(request,"registrationusertype.html")  


def Studentregister(request):
    if request.method == 'POST':
        student_username = request.POST['student_admissionnumber']
        student_password = request.POST['student_password']
        student_password1 = request.POST['student_password1']
        # if student_password1==student_password:
        student_email = request.POST['student_email']
        user=User.objects.create_user(username=student_username,email=student_email,password=student_password)
        user.is_active=False
        user.save()
        student_name = request.POST['student_name']
        student_gender = request.POST['student_gender']
        student_dob = request.POST['student_dob']
        student_address = request.POST['student_address']
        student_phone = request.POST['student_phone']
        student_admissionyear = request.POST['student_admissionyear']
        student_admissionnumber = request.POST['student_admissionnumber']
        student_course = request.POST['student_course']
        student_department = request.POST['student_department']
        svuser = User.objects.get(id=user.id)
        c = courses.objects.get(course=student_course)
        d = department.objects.get(department=student_department)
        
        # student_course = m.id
        # print(student_course)
        add=students(student_name=student_name,student_username=svuser,student_gender=student_gender,student_dob=student_dob,student_address=student_address,student_department_id=d.id,student_course_id=c.id,student_phone=student_phone,student_admissionnumber=student_admissionnumber,student_admissionyear=student_admissionyear)
        add.save()
        return redirect('/')
    else:
        dept=department.objects.all()
        curs=courses.objects.all()
        return render(request, 'registerstudent.html',{
            'dept':dept,
            'curs':curs,
        })
        


def Staffregister(request):
    if request.method == 'POST':
        staff_username = request.POST['staff_username']
        staff_password = request.POST['staff_password']
        staff_password1 = request.POST['staff_password1']
        # if student_password1==student_password:
        staff_email = request.POST['staff_email']
        user=User.objects.create_user(username=staff_username,email=staff_email,password=staff_password)
        user.is_active=False
        user.save()
        staff_name = request.POST['staff_name']
        staff_gender = request.POST['staff_gender']
        staff_dob = request.POST['staff_dob']
        staff_address = request.POST['staff_address']
        staff_phone = request.POST['staff_phone']
        staff_yearofjoin = request.POST['staff_yearofjoin']
        staff_department = request.POST['staff_department']
        staff_post = request.POST['staff_post']
        svuser = User.objects.get(id=user.id)
        d = department.objects.get(department=staff_department)
        p = posts.objects.get(post=staff_post)
        add=staffs(staff_name=staff_name,staff_username=svuser,staff_gender=staff_gender,staff_dob=staff_dob,staff_address=staff_address,staff_phone=staff_phone,staff_yearofjoin=staff_yearofjoin,staff_department_id=d.id,staff_post_id=p.id)
        add.save()
        return redirect('/')
    else:
        dept=department.objects.all()
        pst=posts.objects.all()
        messages.error(request,'account is not active please check ur mail')
        return render(request, 'registerstaff.html',{
            'dept':dept,
            'pst':pst,
        })


    
def Quesadminregister(request):
    if request.user.is_authenticated:
        user=User.objects.get(pk=request.user.id)
        if user.is_superuser:
            if request.method == 'POST':
                quesadmin_username = request.POST['quesadmin_username']
                quesadmin_password = request.POST['quesadmin_password']
                quesadmin_password1 = request.POST['quesadmin_password1']
                # if student_password1==student_password:
                quesadmin_email = request.POST['quesadmin_email']
                user=User.objects.create_user(username=quesadmin_username,email=quesadmin_email,password=quesadmin_password)
                user.save()
                quesadmin_department = request.POST['quesadmin_department']
                svuser = User.objects.get(id=user.id)
                d = department.objects.get(department=quesadmin_department)
                add=quesadmin(quesadmin_username=svuser,quesadmin_department_id=d.id)
                add.save()
                return redirect('Admindashboard')
            else:
                dept=department.objects.all()
                return render(request, 'registerquesadmin.html',{
                    'dept':dept,
                })
        else:
            return render(request, 'alert.html',{'type':'Adminerror'})
    else:
        return render(request, 'alert.html',{'type':'Loginerror'})


def Deletequesadmin(request,id):
        book=quesadmin.objects.get(id=id)
        book.delete()
        return redirect('Adminquestion')

def Deletestaff(request,id):
        useracc=User.objects.get(id=id)
        userdetail=staffs.objects.get(staff_username=id)
        userdetail.delete()
        useracc.delete()
        return redirect('Adminuserview')

def Deletestudent(request,id):
        useracc=User.objects.get(id=id)
        userdetail=students.objects.get(student_username=id)
        userdetail.delete()
        useracc.delete()
        return redirect('Adminuserview')
    
    

# USER REGISTREATION ENDS HERE

# LOGIN LOGOUT STARTS HERE

class Login(View):
    def get(self,request):
        return render(request,"login.html")      

    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']

        if request.user.is_authenticated:
            messages.error(request,'Already Logged In')
            return render(request,"profile.html")
        else:
            if username and password:
                user=auth.authenticate(username=username,password=password)
                if user:
                    if user.is_active:
                        if user.is_superuser:
                            auth.login(request,user)
                            return redirect('Admindashboard')
                        else:
                            auth.login(request,user)
                            c=request.user.id
                            if students.objects.filter(student_username=c).exists():
                                return redirect('/')
                            elif staffs.objects.filter(staff_username=c).exists():
                                return redirect('/')
                        
                    messages.error(request,'account is not active please check ur mail')
                    return render(request,'login.html')
                messages.error(request, 'invalid details,try again')
                return render(request, 'login.html')
            messages.error(request, 'please fill fields')
            return render(request, 'login.html')  



def Logout(request):
    auth.logout(request)
    return  redirect('/')

# LOGIN LOGOUT ENDS HERE

#PROFILE STARTS HERE

def Profile(request):
    if request.user.is_authenticated:
        user=User.objects.get(pk=request.user.id)
        if students.objects.filter(student_username=user).exists():
            student=students.objects.get(student_username=request.user.id)
            takenbook=takenbooks.objects.filter(user=request.user.id)
            tkbook=books.objects.all()
            return render(request,'profile.html',{
                'student':student,
                'takenbook':takenbook,
                'tkbook':tkbook,
                })
        
        elif staffs.objects.filter(staff_username=user).exists():
            staff=staffs.objects.get(staff_username=request.user.id)
            takenbook=takenbooks.objects.filter(user=request.user.id)
            tkbook=books.objects.all()

            return render(request,'profile.html',{
                'staff':staff,
                'takenbook':takenbook,
                'tkbook':tkbook,
                })

        elif quesadmin.objects.filter(quesadmin_username=user).exists():

            return redirect('Addquestion')

        elif user.is_superuser:
            return redirect('Admindashboard')

        else:
            return render(request, 'alert.html',{'type':'NoUser'})
    else:
        return render(request, 'alert.html',{'type':'Loginerror'})

#PROFILE ENDS HERE
        
 
# ADMIN DASHBOARD STARTS HERE





# ADMIN DASHBOARD ENDS HERE










