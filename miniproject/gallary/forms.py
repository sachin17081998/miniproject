from django import forms
from django.contrib.auth.models import User
from gallary.models import *

class userform(forms.ModelForm):
    # password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
         model=User
         fields=('username','email','password')
         widgets = {
            'username': forms.TextInput(attrs={'class': 'signup-fields','placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'class': 'signup-fields','placeholder': 'Enter Email Id'}),
            'password': forms.PasswordInput(attrs={'class': 'signup-fields','placeholder': 'Enter Password'}),
        }

class profile_form(forms.ModelForm):
   
    class Meta:
        model=user_data
        fields=('address','contact')
        widgets = {
            'address': forms.TextInput(attrs={'class': 'signup-fields','placeholder': 'Enter Address'}),
            'contact': forms.TextInput(attrs={'class': 'signup-fields','placeholder': 'Enter Contact Number'})
        }
        

class imgForm(forms.ModelForm):
        
    class Meta:
        model = image
        fields = ('username','imgname', 'img','category')
        widgets={
            'username': forms.TextInput(attrs={'class': 'upload_fields','placeholder': 'Enter User name'}),
            'imgname': forms.TextInput(attrs={'class': 'upload_fields','placeholder': 'Enter Image name'}),
            'category': forms.TextInput(attrs={'class': 'upload_fields','placeholder': 'Enter Image category:ex-nature,wildlife,natural,etc'})
        }
        
class ContactForm(forms.Form):
    # from_email = forms.EmailField(required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'emailform'}),required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'emailform'}), required=True)
    to = forms.EmailField(widget=forms.TextInput(attrs={'class': 'emailform'}),required=True)

       
