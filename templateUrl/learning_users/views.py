from django.shortcuts import render
from learning_users.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):

    registered = False

    if request.method == "POST":
        signup_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(signup_form.errors, profile_form.errors)
    else:
        signup_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, "learning_app/signUp.html",
                                context = {'registered' : registered,
                                           'signup_form' : signup_form,
                                           'profile_form' : profile_form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # built-in function to authenticate
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, "learning_app/login.html", {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice")
