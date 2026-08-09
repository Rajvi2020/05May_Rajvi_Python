from django.shortcuts import render

# Create your views here.
import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Profile
from .forms import ProfileForm


def profile_list(request):
    profiles = Profile.objects.all()

    return render(
        request,
        'profiles/profile_list.html',
        {
            'profiles': profiles
        }
    )


def profile_create(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('profile_list')

    else:
        form = ProfileForm()

    return render(
        request,
        'profiles/profile_form.html',
        {
            'form': form
        }
    )


def export_profiles(request):

    profiles = Profile.objects.all()

    with open('profiles_export.csv', 'w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)

        writer.writerow([
            'Name',
            'Email',
            'Age',
            'Bio',
            'City',
            'Public',
            'Created At'
        ])

        for profile in profiles:
            writer.writerow([
                profile.name,
                profile.email,
                profile.age,
                profile.bio,
                profile.city,
                profile.is_public,
                profile.created_at,
            ])

    with open('profiles_export.csv', 'rb') as file:

        response = HttpResponse(
            file.read(),
            content_type='text/csv'
        )

    response['Content-Disposition'] = (
        'attachment; filename="profiles.csv"'
    )

    return response