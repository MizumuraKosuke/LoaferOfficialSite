from django import forms
from .models import LiveContact

class LiveContactForm(forms.ModelForm):

    class Meta:
        model = LiveContact
        fields = ('name', 'mail_address', 'which_live', 'ticket',)