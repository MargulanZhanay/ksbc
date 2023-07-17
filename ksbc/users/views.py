from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreationForm


# def login_user(request):
#     if request.POST


# class SignUp(CreateView):
#     form_class = CreationForm
#     success_url = reverse_lazy('about:index')
#     template_name = 'users/signup.html'


def signup_user(request):
    if request.POST == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            company_name = form.cleaned_data['company_name']
            password = form.cleaned_data['password1']
            user = authenticate(
                email=email, first_name=first_name,
                last_name=last_name, company_name=company_name,
                password=password
                )
            login(request, user)
            messages.success(request, ('Registration Successfull!'))
            return redirect('about:index')
    else:
        form = CreationForm()

    return render(request, 'users/signup.html', {
        'form': form,
    })
