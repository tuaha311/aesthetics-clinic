from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=100)
    booking = forms.BooleanField(required=False)

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-3'),
                Column('last_name', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-3'),
                Column('phone', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            'message',
            Submit('submit', 'Send Message', css_class='btn btn-primary mt-4')
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Combine first and last name
        instance.name = f"{self.cleaned_data['first_name']} {self.cleaned_data['last_name']}"
        if commit:
            instance.save()
        return instance