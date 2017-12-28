from django import forms
from .models import *

class SubsciberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = [""]