#import forms module as it is having Form class and formfileds
from django import forms

class New_Form(forms.Form):
    name=forms.CharField(max_length=20)