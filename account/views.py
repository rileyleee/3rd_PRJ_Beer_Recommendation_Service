from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from account.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/search/')
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})


@login_required
@require_http_methods(['GET', 'POST'])
def mypage(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/mypage/')
    else:
        form = UserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'account/mypage.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def mybeer(request):
    return render(request, "account/mybeer.html", {
    })

