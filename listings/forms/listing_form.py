from django import forms

from core.BootstrapFormMixin import BootstrapFormMixin
from listings.models import Listing


class ListingForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = Listing
        exclude = ('created_by', 'is_published', 'list_date',)
