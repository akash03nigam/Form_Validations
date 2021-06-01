from django import forms
#from django.core import validators
from Forms_app.models import StudentRegister


class Student(forms.ModelForm):
    class Meta:
        model= StudentRegister
        fields='__all__'
    
    
    #UserName= forms.CharField()
    #Email=forms.EmailField()
    #Password=forms.CharField(widget=forms.PasswordInput)
    #rPassword=forms.CharField(label='Password again',widget=forms.PasswordInput)
    #Feedback= forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(50),validators.MinLengthValidator(10)])
    #Bot_handler= forms.CharField(required=False,widget=forms.HiddenInput)


    #def clean(self):
        #print("---Total Form Validations---")
        #cleaned_data=super().clean()
        #inputname=cleaned_data['UserName']
        #if len(inputname)<=4:
                #raise forms.ValidationError("----Username must contain more than 4 letters----")
        #inputemail=cleaned_data['Email']
        #if inputemail[-9]!= 'g':
            #raise forms.ValidationError("---Email must contain 'gmail.com'---")
        #inputpwd=cleaned_data['Password']
        #inputrpwd=cleaned_data['rPassword']
        #if inputpwd!=inputrpwd:
            #raise forms.ValidationError("---Password must be same---")
        #bot_value= cleaned_data['Bot_handler']
        #if len(bot_value)>0:
            #raise forms.ValidationError("----I know who you are----")
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