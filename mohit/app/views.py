from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students 
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required(login_url="/login")
def hello(request):
    if(request.method == 'POST'):
        data = request.POST
        name = data.get('name') 
        email = data.get('email') 
        age = data.get('age') 
        adress = data.get('address') 
        
        Students.objects.create(
            name = name,
            age  = age,
            email = email,
            adress = adress
        )
        print(" the dATA IS Added Sucessfully")

    stu = Students.objects.all()

    if(request.GET.get('search')):
        stu = Students.objects.filter(name__icontains = request.GET.get('search'))



    con =  {'hell': stu}
    


    return render(request , "hello.html" , con )

def dell(req,id):
    print(id)
    stu = Students.objects.all().get(id = id) 
    stu.delete()
    return redirect('/')

@login_required(login_url='/login')
def upda(request,id):
    record = Students.objects.all().get(id = id)
    if(request.method == 'POST'):
        data = request.POST
        name = data.get('name') 
        email = data.get('email') 
        age = data.get('age') 
        adress = data.get('address') 
        record.name = name
        record.email = email
        record.age = age
        record.adress = adress
        
        record.save()
        print(" the dATA IS Updated Sucessfully")
        return redirect('/')

    
    con =  {'hell': record}
    


    return render(request , "update.html" , con )

def register_pg(req):
    if(req.method == 'POST'):
        data = req.POST
        fname = data.get('fname')
        lname = data.get('lname') 
        username = data.get('username') 
        password = data.get('password') 
         
        user = User.objects.filter(username = username)
        if(user.exists()):
            messages.error(req,"user already exists")
            return redirect('/register/')
        user = User.objects.create(
            first_name  = fname,
            last_name = lname,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.info(req,"user added sucessfully")
        return redirect('/')

    return render(req,"register.html")



def login_pg(req):
    if(req.method == 'POST'):
        data = req.POST
        username = data.get('username') 
        password = data.get('password') 
         
        user = User.objects.filter(username = username)
        if not user.exists():
            messages.error(req,"username is invalid")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(req,user)
            return redirect('/')
        else:
            messages.error(req,"Password is invalid")
            return redirect('/login/')
    return render(req,"login.html")

def logout_pg(req):
    logout(req)
    return redirect('/login/')


