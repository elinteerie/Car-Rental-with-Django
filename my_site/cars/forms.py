from django import forms 
from .models import Review

from django.forms import ModelForm


# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name' ,max_length=50)
#     last_name = forms.CharField(label='Last Name' ,max_length=50)
#     email = forms.EmailField(label='Email Address')
#     review = forms.CharField(label='Please Leave Your Review', widget=forms.Textarea(attrs={'class':'myform'}))
    
    
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
       # ['first_name', 'last_name', 'stars']
        labels = {
           
           'first_name': 'YOUR FIRST NAME',
           'last_name': 'YOUR LAST NAME',
           'stars': 'RATING'
       }
        
        
        error_messages = {
            'stars':{
                'min_value': 'Min Value is 1',
                'max_value': 'Max Value is 5'
            }
            
        }
    