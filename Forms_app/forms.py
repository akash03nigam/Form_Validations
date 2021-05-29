from django import forms

class StudentRegister(forms.Form):
    UserName= forms.CharField()
    Email=forms.EmailField()
    Feedback= forms.CharField(widget=forms.Textarea)