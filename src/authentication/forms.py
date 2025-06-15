from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

USER_TYPE_CHOICES = (
    ('patient', 'Patient'),
    ('doctor', 'Doctor'),
)

class RegistrationForm(UserCreationForm):
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)
    profile_picture = forms.ImageField(required=True)
    address_line1 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    pincode = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'email', 'user_type', 'profile_picture', 
                  'address_line1', 'city', 'state', 'pincode', 'password1', 'password2']
