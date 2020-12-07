from django.contrib import auth, messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms.register_form import RegisterForm
from listings.models import Listing


def signup(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm(),
        }
        return render(request, 'accounts/register.html', context)
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

        context = {
            'form': form,
        }
        return render(request, 'accounts/register.html', context)


@login_required
def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out!')
        return redirect('index')


def user_profile(request):
    user_listings = Listing.objects.order_by('-list_date').filter(created_by_id=request.user.id)
    context = {
        'user_listings': user_listings,
    }
    return render(request, 'accounts/user_profile.html', context)
