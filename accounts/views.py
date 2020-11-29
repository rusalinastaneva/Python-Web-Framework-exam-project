from django.contrib import auth, messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms.register_form import RegisterForm


# def user_profile(request, pk=None):
#     user = request.user if pk is None else User.objects.get(pk=pk)
#     if request.method == 'GET':
#         context = {
#             'profile_user': user,
#             'profile': user.userprofile,
#             'listings': user.listing_set.all(),
#             'form': UserProfileForm()
#         }
#         return render(request, 'accounts/user_profile.html', context)
#     else:
#         form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
#         if form.is_valid():
#             form.save()
#             return redirect('current user profile')
#         return redirect('current user profile')


def signup(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm(),
        }
        return render(request, 'accounts/register.html', context)
    else:
        # GET form values
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
    pass
# Filter by the current logged in user

# user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
#
# context = {
#     'contacts': user_contacts
# }
#
# return render(request, 'accounts/dashboard.html', context)
