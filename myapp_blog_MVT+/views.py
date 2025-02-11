from django.shortcuts import render, redirect
from .models import Post, Profile
from .forms import PostForm, ProfileForm, UserRegisterForm, ContactForm, FeedbackForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'myapp/create_post.html', {'form': form})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if request.user != post.author:
            return HttpResponseForbidden()
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'myapp/edit_post.html', {'form': form, 'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return HttpResponseForbidden()
    post.delete()
    return HttpResponseRedirect('/')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'myapp/edit_profile.html', {'form': form})

def home(request):
    posts = Post.objects.all()
    return render(request, 'myapp/home.html', {'posts': posts})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f'Name: {name}, Email: {email}, Message: {message}')
            return render(request, 'myapp/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return render(request, 'myapp/feedback_success.html')
    else:
        form = FeedbackForm()
    return render(request, 'myapp/feedback.html', {'form': form})
