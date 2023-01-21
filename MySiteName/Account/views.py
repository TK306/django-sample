from django.shortcuts import render, redirect
from Account.models import LoginUser
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup_view(request):
    if request.method != "POST":
        return render(request, "account/signup.html")

    username = request.POST["username"]
    email = request.POST["email"]
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]
    try:
        LoginUser.objects.get(email=email)
        messages.error(request, "このメールアドレスは既に登録されています")
        return render(request, "account/signup.html")
    except:
        if password1 != password2:
            messages.error(request, "パスワードが一致しません")
            return render(request, "account/signup.html")
        LoginUser.objects.create_user(
            email=email, username=username, password=password1
        )
        user = LoginUser.objects.get(email=email)
        user.username = username

    return redirect("index")


def login_view(request):
    if request.method != "POST":
        return render(request, "account/login.html")
    email = request.POST["email"]
    password = request.POST["password"]
    try:
        user = LoginUser.objects.get(email=email)
    except:
        messages.error(request, "このメールアドレスは登録されていません")
        return render(request, "account/login.html")
    if not user.check_password(password):
        messages.error(request, "パスワードが違います")
        return render(request, "account/login.html")
    login(request, user)
    return redirect("index")


@login_required
def logout_view(request):
    logout(request)
    return redirect("index")


@login_required
def account_info_view(request):
    return render(request, "account/info.html")


@login_required
def change_password_view(request):
    file = "account/change_password.html"
    if request.method != "POST":
        return render(request, file)

    password1 = request.POST["password1"]
    password2 = request.POST["password2"]
    password3 = request.POST["password3"]
    if not request.user.check_password(password1):
        messages.error(request, "パスワードが違います")
        return render(request, file)

    if password1 == password2:
        messages.error(request, "同じパスワードです")
        return render(request, file)

    if password2 != password3:
        messages.error(request, "新しいパスワードが一致しません")
        return render(request, file)
    user = request.user
    user.set_password(password2)
    user.save()

    messages.success(request, "パスワードを変更しました")
    return render(request, file)


@login_required
def change_username_view(request):
    file = "account/change_username.html"
    if request.method != "POST":
        return render(request, file)

    username = request.POST["username"]

    if request.user.username == username:
        messages.error(request, "同じユーザー名です")
        return render(request, file)

    user = request.user
    user.username = username
    user.save()

    messages.success(request, "ユーザー名を変更しました")
    return render(request, file)


@login_required
def delete_account_view(request):
    file = "account/delete_account.html"
    if request.method != "POST":
        return render(request, file)

    email = request.POST["email"]
    password = request.POST["password"]

    if request.user.email != email:
        messages.error(request, "メールアドレスが違います")
        return render(request, file)

    if not request.user.check_password(password):
        messages.error(request, "パスワードが違います")
        return render(request, file)

    request.user.delete()
    return redirect("index")
