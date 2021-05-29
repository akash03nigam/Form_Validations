from django.shortcuts import render
from . import forms
# Create your views here.
def Register(request):

    #form= forms.StudentRegister()
    if request.method=='POST':
        form= forms.StudentRegister(request.POST)
        if form.is_valid():
            print("Student Details Are Validated Successfully:")
            print("Student Name:",form.cleaned_data['UserName'])
            print("Student Email ID:",form.cleaned_data['Email'])
            print("Student Feedback:",form.cleaned_data['Feedback'])
            return render(request, 'testapp/thankyou.html',{'name':form.cleaned_data['UserName']})
    return render(request, 'testapp/results.html',{'form': form})