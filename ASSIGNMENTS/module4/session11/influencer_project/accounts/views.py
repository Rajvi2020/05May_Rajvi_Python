from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import InfluencerProfile
from .forms import InfluencerProfileForm
from django.contrib.auth import authenticate, login
# Create your views here.


def home(request):
    return render(request, "home.html")
def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("edit_profile")

        else:
            return render(
                request,
                "login.html",
                {"error": "Invalid username or password"}
            )

    return render(request, "login.html")

@login_required
def profile(request):
    profile = InfluencerProfile.objects.get(user=request.user)

    return render(
        request,
        "profile.html",
        {"profile": profile}
    )

@login_required
def edit_profile(request):

    profile, created = InfluencerProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = InfluencerProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = InfluencerProfileForm(instance=profile)

    return render(request, "edit_profile.html", {"form": form})