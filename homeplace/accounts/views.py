from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from homeplace.accounts.forms.signup_form import SignUpForm
from homeplace.listings.models import Listing


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    success_message = 'Great! You are already registered.'

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class SignInView(LoginView):
    pass


class SignOutView(LoginRequiredMixin, SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('index')


def user_profile(request):
    user_listings = Listing.objects.order_by('-list_date').filter(created_by_id=request.user.id)
    context = {
        'user_listings': user_listings,
    }
    return render(request, 'accounts/user_profile.html', context)

# def signup(request):
#     if request.method == 'GET':
#         context = {
#             'form': RegisterForm(),
#         }
#         return render(request, 'accounts/signup.html', context)
#     else:
#         form = RegisterForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#
#         context = {
#             'form': form,
#         }
#         return render(request, 'accounts/signup.html', context)


# @login_required
# def signout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         messages.success(request, 'You are now logged out!')
#         return redirect('index')