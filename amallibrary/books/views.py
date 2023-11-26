from django.views import View
from django.views.generic import TemplateView
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from books.models import *



# Create your views here.




def Bookstall(request):
    book=books.objects.all()
    takenbook=takenbooks.objects.all()
    var=[]
    for i in book:
        for j in takenbook:
            if i.id==j.book.id:
                var.append(j.book.id)
                # print(j.book.id)
    return render(request,'books.html',{
        'book':book,
        'takenbook':takenbook,
        'var':var
        })


def Adminbook(request):
    if request.user.is_authenticated:
        user=User.objects.get(pk=request.user.id)
        if user.is_superuser:
            if request.method == 'POST':
                formname=request.POST.get('formname')
                if formname=='addbook':
                    name = request.POST.get('name')
                    author = request.POST.get('author')
                    pub_date = request.POST.get('pub_date')
                    category = request.POST.get('category')
                    description = request.POST.get('description')
                    booknumber = request.POST.get('booknumber')
                    image = request.FILES.get('image')
                    newbook = books(name=name, author=author, pub_date=pub_date, category=category, description=description, booknumber=booknumber, image=image)
                    newbook.save()
                    book=books.objects.all()
                    takenbook=takenbooks.objects.all()
                    var=[]
                    return HttpResponseRedirect('Adminbook')
                elif formname=='broughtbook':
                    booknumber = request.POST.get('booknumber')
                    bookid=books.objects.get(booknumber=booknumber)
                    username = request.POST.get('username')
                    userid=User.objects.get(username=username)
                    if books.objects.filter(id=bookid.id).exists() and User.objects.filter(id=userid.id).exists():
                        add=takenbooks(book_id=bookid.id,user_id=userid.id,renewaldate=timezone.now()+datetime.timedelta(days=14),returndate=timezone.now()+datetime.timedelta(days=14))
                        add.save()
                        book=books.objects.all()
                        takenbook=takenbooks.objects.all()
                        var=[]
                        return HttpResponseRedirect('Adminbook')
                    else:
                        messages.error(request, 'invalid details,try again')
                        return HttpResponseRedirect('Adminbook')
                else:
                    return HttpResponseRedirect('Adminbook')
            else:
                book=books.objects.all().order_by('booknumber')
                takenbook=takenbooks.objects.all().order_by('book')
                var=[]
                for i in book:
                            for j in takenbook:
                                if i.id==j.book.id:
                                    var.append(j.book.id)
                return render(request,'adminbook.html',{
                            'book':book,
                            'takenbook':takenbook,
                            
                            'var':var
                            })







def Renewbook(request,id):
    takenbook=takenbooks.objects.get(book=id)
    takenbook.renewalstatus=True
    takenbook.returndate = takenbook.returndate + datetime.timedelta(days=14)
    takenbook.save()
    return redirect('Adminbook')


def Returnbook(request,id):
    takenbook=takenbooks.objects.get(book=id)

    track = booktakingdatabase(booknumber=takenbook.book.booknumber,username=takenbook.user.username,takendate=takenbook.date,returndate=takenbook.returndate)
    track.save()
    takenbook.delete()
    
    return redirect('Adminbook')




# def Blockbooks(request,id):
#         book = books.objects.get(pk=id)
#         user = User.objects.get(pk=request.user.id)
#         newbook = takenbooks(book=book,user=user)
#         newbook.save()
#         return redirect('Viewbook')
    
def Editbook(request,id):
        if request.method == 'POST':
            name = request.POST.get('name')
            author = request.POST.get('author')
            pub_date = request.POST.get('pub_date')
            category = request.POST.get('category')
            description = request.POST.get('description')
            booknumber = request.POST.get('booknumber')
            image = request.FILES.get('image')
            book=books.objects.get(id=id)
            book.name=name
            book.author=author
            book.pub_date=pub_date
            book.category=category
            book.description=description
            book.booknumber=booknumber
            book.image=image
            book.save()
            return redirect('Adminbook')
        else:
            book=books.objects.get(id=id)
            return render(request,'editbook.html',{
                'book':book
                })


def Deletebook(request,id):
        book=books.objects.get(id=id)
        book.delete()
        return redirect('Adminbook')
