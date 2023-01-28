from django.shortcuts import render,get_object_or_404,redirect
from django.views import View   
from django.contrib.auth import get_user_model
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .form import loginmodel
from .models import UsersData, UsersInfo,FilesForms
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login,logout, authenticate


def get(request):
    if not request.user.is_authenticated:
        return redirect("login_local")
    
    template_name = "./registration/home_site.html"
    
    return render(request, template_name,{"msg":"Hello"})


def get_files(request):
    if not request.user.is_authenticated:
        return redirect("login_local")
    
    template_name = "./registration/files_request.html"
    
    return render(request, template_name,{"msg":"Hello"})


@login_required(login_url='login')
def get_my_request(request):
    template_name = "./registration/get_element.html"
    print(type(request.user.username))
    data = UsersData.objects.all().filter(userName=request.user.username)
    usersInformation = []
    for d in data:
        usersInformation.append(UsersInfo.objects.get(users=d))
    print(usersInformation[0].users.email)
    return render(request, template_name,{"data":usersInformation})


def final_view(request):
    template_name = "./registration/success.html"
    return render(request, template_name,{"msg":"Hello"})


def register(request,*args,**kwargs):
    form = {}
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        user = User.objects.create_user(username,email,password)
        user.save()
        return redirect("login_local")

    return render(request, "./registration/register.html",{'form':form})


def login_view(request):
    try:
        context= {}
        form = AuthenticationForm(data=request.POST or None)
        if request.method == 'POST':
            email = request.POST.get("username")
            password = request.POST.get("password")
            form = authenticate(request,username=email,password=password)
            if email != "" and password != "": 
                login(request,form)
                template_name = "./registration/home_site.html"
                return redirect("index_page")
            else:
                context =  {
                'message':"الرمز او اسم المستخدم غير صحيح او لم يتم ادخالهما","form":form
                }
        return render(request, './registration/login.html',context)
    except (Exception):
            return render(request, './registration/login.html',{"message":"الرمز او الاييمل خطأ الرجاء اعد المحاولة"})

# @staff_member_required(login_url='Login')
def user_logout(request):
	if request.method == 'POST':
		logout(request)
		return redirect('login_local')

def make_request(request):
    context = {}
    
    if request.method == 'POST':
        username = request.user.username
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        job_title = request.POST.get("job_title")
        spacificTitle = request.POST.get("spacificTitle")
        department = request.POST.get("department")
        currently_job_title = request.POST.get("currently_job_title")
        date_reviced_title = request.POST.get("date_reviced_title")
        targeted_title = request.POST.get("targeted_title")
        validation_date = request.POST.get("validation_date")
        requested_date = request.POST.get("requested_date")
        if 'edu.iq' not in email:
            return render(request, './registration/request.html',{"message":"Sorry your email is not valid"})

        # Save data to database
        obj_request = UsersData.objects.create(userName=username,email=email,phone=phone)
        obj_request.save()
        
        user_info = UsersInfo.objects.create(job_title=job_title,spacificTitle=spacificTitle,department=department,currently_job_title=currently_job_title,date_reviced_title=date_reviced_title,targeted_title=targeted_title,validation_date=validation_date,users=obj_request)
        user_info.save()
        fss = FileSystemStorage()
        
        uploaded_files = []
        for fileData in request.FILES.getlist('uploads'):
            uploading = fss.save(fileData.name, fileData)
            url_file = fss.url(uploading)
            uploaded_files = FilesForms(title=fileData.name,files_path=url_file,user= user_info)
            uploaded_files.save()
        context["msg"] = "All Good"    
        return redirect('index_page')

    return render(request, './registration/request.html',context)

