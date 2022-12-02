from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('name','dob','aadhar','mobile','email','password','actype')
        labels={
            'name':'Name',
            'dob':'Date of Birth',
            'aadhar':'Aadharcard No.',
            'mobile':'Mobile No.',
            'email':'Email Id.',
            'password':'Password',
            'actype':'Account Type'
        }
        widgets = {
            'dob': forms.DateInput(attrs={'type':'date'}),
            'email': forms.EmailInput(attrs={'type':'email'})
        }

    def __init__(self,*args, **kwargs):
        super(AccountForm,self).__init__(*args, **kwargs)
        self.fields['actype'].empty_label='Select Account Type'