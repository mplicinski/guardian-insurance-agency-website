from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy

# Create your views here.
def staff_home_view(request):
    return render(request, "staff/home.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "staff/login.html", context=context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        #return redirect(url('', staff_home_view))
        return redirect('/staff')
    return render(request, "staff/logout.html", {})