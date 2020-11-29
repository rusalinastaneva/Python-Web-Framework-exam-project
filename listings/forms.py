from django import forms

from listings.models import Listing


class ListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control_class_to_all_fields()

    def add_form_control_class_to_all_fields(self):

        for (_, field) in self.fields.items():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] = field.widget.attrs['class'] + 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Listing
        exclude = ('created_by', 'is_published', 'list_date',)
        # widgets = {
        #     'image_url': forms.TextInput(
        #         attrs={
        #             'id': 'img_input',
        #         }
        #     )
        # }
