from django.shortcuts import render,redirect, HttpResponse, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


from .models import ProfileUser
from .forforms import LoginFrom, SignupForm, UserEditForm, ChangePassForm

def userlogin(request):
    if request.method == "POST":
        form = LoginFrom(request.POST or None)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            user_pass = form.cleaned_data["user_pass"]
            user_auth = authenticate(request,username=user_name, password=user_pass)
            login(request, user_auth)
            return redirect("home")
        context = {'form' : form}
        return render(request, 'login.html', context=context)

    if request.method == "GET":
        form = LoginFrom(request.POST or None)
        context = {'form' : form}
        return render(request, 'login.html', context=context)

@login_required(login_url='userlogin')
def userlogout(request):
    logout(request)
    return redirect("home")


def usersignup(request):
    if request.method == "POST":
        form = SignupForm(request.POST or None)
        if form.is_valid():
            if form.cleaned_data.get("user_pass") == form.cleaned_data.get("user_pass2"):
                u = User.objects.create_user(username=form.cleaned_data.get("user_na"),
                                             password=form.cleaned_data.get("user_pass"))
                u.save()
                profileUser = form.save(commit=False)
                profileUser.user_name = u
                profileUser.save()
                return redirect('home')
            else:
                return redirect('usersignup')


        context = {'form' : form}
        return render(request, 'signup.html', context=context)

    if request.method == "GET":
        form = SignupForm(request.POST or None)
        context = {'form' : form}
        return render(request, 'signup.html', context=context)

@login_required(login_url='userlogin')
def userdetails(request):
    userinfo = ProfileUser.objects.get(user_name = request.user)
    context = {'userinfo': userinfo}
    return render(request, 'userdetails.html', context=context)

@login_required(login_url='userlogin')
def useredit(request):
    if request.method == "GET":
        userinfo = ProfileUser.objects.get(user_name = request.user)
        form = UserEditForm(instance = userinfo)
        context = {'form': form}
        return render(request, 'useredit.html', context=context)
    if request.method == "POST":
        userinfo = ProfileUser.objects.get(user_name = request.user)
        form = UserEditForm(request.POST or None, instance = userinfo)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {'form': form}
        return render(request, 'useredit.html', context=context)


# @login_required(login_url='userlogin')
# def userdelete(request, username):
#     userForDelete = ProfileUser.objects.get(user_name__username__iexact = username)
#     if userForDelete.user_name == request.user:
#         return redirect(reverse("view_all_user"))
#     else:
#         userForDelete.delete()
#         userAuth = User.objects.get(username=username)
#         userAuth.delete()
#         return redirect(reverse("view_all_user"))

@login_required(login_url='userlogin')
def changePass(request):
    u = User.objects.get(username = request.user)
    if request.method == "POST":
        form = ChangePassForm(request.POST or None)
        if form.is_valid():
            if form.cleaned_data.get("user_pass") == form.cleaned_data.get("user_pass2"):
                matchcheck = check_password(form.cleaned_data.get("old_pass"), request.user.password)
                if matchcheck:
                    u.set_password(form.cleaned_data.get("user_pass2"))
                    u.save()
                    return HttpResponse("<h3>password changed</h3>")
                else:
                    return HttpResponse("<h3>Failed to change</h3>")

    if request.method == "GET":
        form = ChangePassForm(request.POST or None)
        context = {'form' : form}
        return render(request, 'changePass.html', context=context)
