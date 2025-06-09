from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify


# Make email unique 
User._meta.get_field('email')._unique = True


# Create custom register form with no password for a logout experience
class UserRegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
        # Remove help text from widgets
        widgets = {
            'username': forms.TextInput(attrs=
                                        {'placeholder': 'Enter a username',
                                         "type":"text", 
                                        }),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter a valid email'}),
        }
        
         # Ensure email is unique
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise ValidationError("A user with this email already exists.")
            return email
        
        # Custom save method
        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_unusable_password()  # No password required for login

            if commit:
                user.save()
            return user
