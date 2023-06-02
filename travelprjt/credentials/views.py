
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def register(request):
    if request.method == 'post':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)

        user.save()
        print("user created")
    return render(request,"register.html")




