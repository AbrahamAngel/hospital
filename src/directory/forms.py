from django import forms
from directory.models import Profile

class AccountProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'user_type',
            'profile_picture',
            'address_line1',
            'city',
            'state',
            'pincode',
        ]

        widgets = {
            'user_type': forms.Select(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'address_line1': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
        }
