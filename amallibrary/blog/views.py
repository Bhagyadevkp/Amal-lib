import os
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from blog.forms import BlogForm

from blog.models import *

# from questionpool.models import question

# Create your views here.



def Adminblog(request):
    if request.user.is_authenticated:
        user=User.objects.get(pk=request.user.id)
        if user.is_superuser:
            if request.method == 'POST':
                form=BlogForm(request.POST, request.FILES)
                newpost = form.save(commit=False)
                newpost.save()
                return HttpResponseRedirect('Adminblog')

            else:
                postblog=BlogForm()
                posts = Blogpost.objects.all().order_by('-id')
                cmnt = Blogpostcomment.objects.all().order_by('-id')
                return render(request, 'adminblog.html', {
                    'posts': posts,
                    'postblog': postblog,
                    'cmnt': cmnt,
                    })
            
        else:
            return redirect('/')
            #u r notan admin "Alert"
    else:
        return redirect('Login')
        #u r not an admin or not logged in "Alert"

def Deleteblog(request,id):

        book=Blogpost.objects.get(id=id)
        cmnt=Blogpostcomment.objects.filter(post=id)
        cmnt.delete()
        book.delete()
        return redirect('Adminblog')

def Deletecomment(request,id):
        cmnt=Blogpostcomment.objects.get(id=id)
        cmnt.delete()
        return redirect('Adminblog')
    











def Bloglist(request):
    post = Blogpost.objects.all().order_by('-id')
    return render(request, 'bloglist.html',{
        'post': post,
    })


def Blogview(request,id):
            if request.method == 'POST':
                comment = request.POST.get('comment')
                author = request.POST.get('author')
                rating = request.POST.get('rating')
                id = request.POST.get('postid')
                newcomment = Blogpostcomment(post_id=id, comment=comment, author=author, rating=rating)
                newcomment.save()
                posts = Blogpost.objects.get(id=id)
                comments = Blogpostcomment.objects.filter(post_id=id).order_by('-id')
                return HttpResponseRedirect(str(id))
            else:
                posts = Blogpost.objects.get(id=id)
                comments = Blogpostcomment.objects.filter(post_id=id).order_by('-id')
                return render(request, 'blog.html', {
                    'posts': posts,
                    'comments': comments,
                    })



def Addfeedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        newfeedback = Feedback(name=name, email=email, message=message)
        newfeedback.save()
        return redirect('/')
    else:
        return render(request, 'feedback.html')

def Addnotice(request):
    if request.user.is_authenticated:
        user=User.objects.get(pk=request.user.id)
        if user.is_superuser:
            if request.method == 'POST':
                title = request.POST.get('title')
                body = request.POST.get('body')
                newnotice = Notice(title=title, body=body)
                newnotice.save()
                return redirect('/')
            else:
                return render(request, 'notice.html')
        else:
            return redirect('/')
            #u r notan admin "Alert"
    else:
        return redirect('Login')
        #u r not an admin or not logged in "Alert"





def Shownotice(request,id):
    notice = Notice.objects.get(pk=id)
    return render(request, 'notice.html', {
        'notice': notice,
        })


def Showfeedback(request):
    feedback = Feedback.objects.all()
    return render(request, 'feedback.html', {
        'feedback': feedback,
        })



    
