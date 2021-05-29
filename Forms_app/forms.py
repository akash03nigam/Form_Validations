from django import forms

class StudentRegister(forms.Form):
    Name= forms.CharField()
    Marks=forms.IntegerField()