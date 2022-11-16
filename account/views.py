from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from account.forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
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