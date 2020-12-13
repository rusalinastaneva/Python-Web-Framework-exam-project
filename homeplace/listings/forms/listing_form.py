from django import forms

from homeplace.core.BootstrapFormMixin import BootstrapFormMixin
from homeplace.listings.models import Listing


class ListingForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = Listing
        exclude = ('created_by', 'is_published', 'list_date',)