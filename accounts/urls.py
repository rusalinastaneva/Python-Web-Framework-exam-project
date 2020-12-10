from django.urls import path, include

from accounts.views import user_profile, SignUpView, SignOutView, SignInView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup user'),
    path('signin/', SignInView.as_view(), name='signin user'),
    path('signout/', SignOutView.as_view(), name='signout user'),
    path('profile/', user_profile, name='user profile'),
]
