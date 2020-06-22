from django.shortcuts import render

from app import forms
# Create your views here.
def New_Form(request):
    form=forms.New_Form()
    return render(request,'New_Form.html',context={'form':form})




