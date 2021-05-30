from django import forms
from django.core import validators

class StudentRegister(forms.Form):
    UserName= forms.CharField()
    Email=forms.EmailField()
    Password=forms.CharField(widget=forms.PasswordInput)
    Confirm_Password=forms.CharField(widget=forms.PasswordInput)
    Feedback= forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(50),validators.MinLengthValidator(10)])

    def clean(self):
        print("---Total Form Validations---")
        cleaned_data=super().clean()
        inputname=cleaned_data['UserName']
        if len(inputname)<=4:
                raise forms.ValidationError("----Username must contain more than 4 letters----")
        inputemail=cleaned_data['Email']
        if inputemail[-9]!= 'g':
            raise forms.ValidationError("---Email must contain 'gmail.com'---")
        inputpwd=cleaned_data['Password']
        inputrpwd=cleaned_data['Confirm_Password']
        if inputpwd!=inputrpwd:
            raise forms.ValidationError("---Password must be same---")

#Impicit_Validators
#def All_Upercase(x):
    #if x.isalpha() is not True:
        #raise forms.ValidationError("-----Username must have alphabets only-----")
#Impicit_Validators
#def Only_Gmail(y):
    #if y[-9]!= 'g':
        #raise forms.ValidationError("---Email must contain 'gmail.com'---")


    #Explicit_Validators
    #def clean_UserName(self):
        #inputname= self.cleaned_data['UserName']
        #if len(inputname)<4:
            #raise forms.ValidationError("Kya Karte Ho Chutiyape Wala Kaam")
        #return inputname  