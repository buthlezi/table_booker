from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import UserForm
from .models import Restaurant
# from current directory import models


def home_page(request):
    if not request.user.is_authenticated:
        return redirect('table_booker:login')
# otherwise skip to line 11        
    context = {'restaurants': Restaurant.objects.all()}    
    return render(request, 'home.html', context=context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        # POST contains data
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("table_booker:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    # GET contains no data - empty form
    return render(
        request=request,
        template_name="login.html",
        context={"login_form": form},
    )
 

def signup_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("table_booker:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserForm
    return render(
        request=request,
        template_name="signup.html",
        context={"register_form": form},
    )



def logout_page(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('table_booker:login') 

# no need for a logout template           
