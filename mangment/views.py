from django.shortcuts import render,get_object_or_404,redirect
from django.views import View   
from django.contrib.auth import get_user_model
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from .form import loginmodel
from .models import Admin
from user.models import UsersData,UsersInfo
from django.http import HttpResponse
def get(request):
    # Get all items and send it to front-end
    data = Admin.objects.all()
    context = {'data':data}
    template_name = "homePage.html"
    return render(request, template_name,context)

def register(request,*args,**kwargs):
    form = loginmodel(request.POST or None)
    if request.method == 'POST':
        form = loginmodel(request.POST)
        print(form)
        if form.is_valid():
            user_obj = form.save()
            print(user_obj,"Created")
            return redirect("/admin-managment/login")

    return render(request, "register.html",{'form':form})


def login_view(request):
    try:
        context= {}
        if request.method == 'POST':
            # print(form)
            email = request.POST["username"]
            password = request.POST["password"]
            form = authenticate(request,username=email,password=password)
            print(form)

            if form is not None: 
                login(request,form)
                return redirect('Indexing')
        
        form = AuthenticationForm(data=request.POST or None)
        context =  {
        'message':"Error","form":form
        }
                
        return render(request, 'login.html',context)
    except (Exception):
        return render(request, 'login.html',{"message":"الرمز او اسم المستخدم خطأ الرجال اعد المحاولة"})


# @staff_member_required(login_url='Login')
def user_logout(request):
    print(request.method)
    if request.method == 'POST':
        logout(request)
        return redirect('login_user')
    


def get_all_requested(request):
    context = {}
    if request.method == 'GET':
        data = UsersInfo.objects.all()
        print(data)
        if len(data) == 0:
            context = {"msg":"Sorry there is no data available",'data':[]}
            return render(request, 'get_element.html',context)
        context['data'] = data
        return render(request, 'get_element.html',context)

    return render(request, 'get_element.html',context)




def get_all_users(request):
    context = {}
    if request.method == 'GET':
        data = UsersData.objects.all()
        print(data)
        if len(data) == 0:
            context = {"msg":"Sorry there is no data available",'data':[]}
            return render(request, 'get_users.html',context)
        context['data'] = data
        return render(request, 'get_users.html',context)

    return render(request, 'get_users.html',context)


def update(request,email):
    # Get all items and send it to front-end
    print(email)

    data = UsersInfo.objects.get(users=email)
    if request.method == 'GET':
        data.request_status = 'تم القبول'
        data.save()
        context = {'data':data}
    return HttpResponse({"message":"تمت العملية بنجاح"})


def reject(request,email):
    # Get all items and send it to front-end
    print(id)
    data = UsersInfo.objects.get(users=email)
    if request.method == 'GET':
        data.request_status = 'تم رفض الطلب'
        data.save()
        context = {'data':data}
    return HttpResponse({"message":"تمت العملية بنجاح"})
    