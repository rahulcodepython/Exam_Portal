from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from home.models import Custom_User

# Create your views here


def index(request):
    pass

def login_temp(request):
    return render(request, "login.html")

def login_user(request):
    if request.method=="POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        username = User.objects.get(email=email).username

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return render(request, "exam.html")

def register_temp(request):
    return render(request, "register.html")

def register(request):
    if request.method=='POST':
        name = request.POST.get('name')
        fathername = request.POST.get('fathername')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        password = request.POST.get('password')
        dob = request.POST.get('dob')

        username = name+dob+mobile

        # Django build-in user save
        User.objects.create_user(first_name=name, username=username, email=email, password=password).save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                
                # Custom User save
                custom_username = request.user
                Custom_User(user=custom_username, father=fathername, address=address, dob=dob, mobile=mobile).save()

                return render(request, "exam.html")

def submit(request):
    if request.method=="POST":

        score = request.POST.get('score')

        user = Custom_User.objects.get(user=request.user)

        user.marks = score

        user.save()
    
    return redirect(dashboard)

def dashboard(request):

    user = Custom_User.objects.get(user=request.user)

    context = {
        'data': user,
    }

    # print(user.uername)
    # print(user.father)
    # print(user.marks)

    return render(request, "dashboard.html", context)