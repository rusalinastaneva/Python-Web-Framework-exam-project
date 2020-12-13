from django import forms

from homeplace.listings.choices import STATE_CHOICES, STATUS_CHOICES, TYPE_HOME_CHOICES, BEDROOM_CHOICES, PRICE_CHOICES


class SearchListingForm(forms.Form):
    keywords = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Keyword (Pool, Garage, etc)'}),
                               required=False)

    city = forms.CharField(max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'City'}),
                           required=False)

    state = forms.ChoiceField(
        choices=STATE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'State (All)'}),
        required=False)

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status (All)'}),
        required=False)

    type_home = forms.ChoiceField(
        choices=TYPE_HOME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Type of home (All)'}),
        required=False)

    bedrooms = forms.ChoiceField(
        choices=BEDROOM_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Type of home (All)'}),
        required=False)

    price = forms.ChoiceField(
        choices=PRICE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Max Price (Any)'}),
        required=False)
