from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView


login = LoginView.as_view(
    template_name="account/login.html",
)


logout = LogoutView.as_view(
    next_page="/account/login/",
)


@login_required
def mypage(request):
    return render(request, "account/mypage.html")

def mybeer(request):
    return render(request, "account/mybeer.html")


signup = CreateView.as_view(
    form_class=UserCreationForm,
    success_url="/account/login/",
    template_name="account/signup.html"
)