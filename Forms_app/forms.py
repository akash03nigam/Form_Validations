from django import forms

class StudentRegister(forms.Form):
    UserName= forms.CharField()
    Password=forms.IntegerField()
    Feedback= forms.CharField(widget=forms.Textarea)