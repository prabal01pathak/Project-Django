from django.shortcuts import render,get_object_or_404
from .models import SignUp,LogIn
from .forms import SignUpForm,LogInForm


def home_view(request):
    return render(request,'home.html',{})
def sign_up_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
           form.save()
           form=SignUpForm              
    context = {
        "form":form
    }
    return render(request,'sign_up.html',context)

def log_in_view(request):
    form = LogInForm(request.POST or None)
    if form.is_valid:
        form = LogInForm

    context = {
        "form":form
    }

    return render(request,'log_in.html',context)
