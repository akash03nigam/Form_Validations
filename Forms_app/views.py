from django.shortcuts import render
from . import forms
# Create your views here.
def Register(request):

    form= forms.StudentRegister()
    return render(request, 'testapp/results.html',{'form': form})