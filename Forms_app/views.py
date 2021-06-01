from django.shortcuts import render
from . import forms
# Create your views here.
def Register(request):
    #if request.method=='GET':
    form= forms.Student()
    #return render(request, 'testapp/results.html', {'form': form})    
    if request.method=='POST':
        form= forms.Student(request.POST)
        if form.is_valid():
            form.save()
            #print("Student Details Are Validated Successfully:")
            #print("Student Name:",form.cleaned_data['UserName'])
            #print("Student Email ID:",form.cleaned_data['Email'])
            #print("Student Feedback:",form.cleaned_data['Feedback'])
        return render(request, 'testapp/thankyou.html',{'name':form.cleaned_data['Name']})
    return render(request, 'testapp/results.html',{'form': form})