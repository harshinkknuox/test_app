from django import forms
from web.models import User



class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("name", "place", "email")