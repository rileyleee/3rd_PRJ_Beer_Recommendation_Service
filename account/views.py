from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from account.forms import SignupForm
from account.models import User


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            nickname = form.cleaned_data.get('nickname')
            raw_password = form.cleaned_data.get('password1')
            gender = form.cleaned_data.get('gender')
            age = form.cleaned_data.get('age')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username,
                                nickname=nickname,
                                password=raw_password,
                                gender=gender,
                                age=age,
                                email=email,)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/search/')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


@login_required
@require_http_methods(['GET', 'POST'])
def mypage(request):
    user = request.user
    return render(request, 'account/mypage.html',
                  {'person': user})


@login_required
@require_http_methods(['GET', 'POST'])
def mybeer(request):
    return render(request, "account/mybeer.html", {
    })
