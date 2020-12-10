from django.urls import path, include

from accounts.views import signout, user_profile, SignUpView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup user'),
    path('signout/', signout, name='signout user'),
    path('profile/', user_profile, name='user profile'),
]
