from django.urls import path, include

from accounts.views import signup, signout, user_profile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup user'),
    # path('profile/<int:pk>/', user_profile, name='user profile'),
    path('signout/', signout, name='signout user'),
    path('profile/', user_profile, name='user profile'),
]