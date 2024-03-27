from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UploadedDataForm
from .models import UploadedData
import os
from django.conf import settings

def index(request):
    return redirect("dashboard")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    user_data = UploadedData.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'user_data': user_data})


@login_required
def upload_data(request):
    if request.method == 'POST':
        form = UploadedDataForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_data = form.save(commit=False)
            uploaded_data.user = request.user

            # Save the uploaded image
            uploaded_image = uploaded_data.image
            uploaded_data.save()

            # Create an empty text file and save its path
            uploaded_text_file = f"{uploaded_data.id}.txt"
            text_file_path = os.path.join(settings.MEDIA_ROOT, uploaded_text_file)
            with open(text_file_path, 'w') as text_file:
                text_file.write(f"Text 1: {uploaded_data.text1}\n")
                text_file.write(f"Text 2: {uploaded_data.text2}\n")
                text_file.write(f"Text 3: {uploaded_data.text3}\n")

            # Save the path to the text file in the database
            uploaded_data.text_file = uploaded_text_file
            uploaded_data.save()

            return redirect('dashboard')
    else:
        form = UploadedDataForm()
    return render(request, 'upload_data.html', {'form': form})