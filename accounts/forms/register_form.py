from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core.BootstrapFormMixin import BootstrapFormMixin


class RegisterForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)
