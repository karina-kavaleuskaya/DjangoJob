from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import get_user_model, login

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})
