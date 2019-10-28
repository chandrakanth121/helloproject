from django.shortcuts import render
from . import forms

def thanku(request):
    return render (request,'testapp/thanku.html')

# Create your views here.
def feedbackview(request):
    form=forms.feedbackform()
    if request.method=='POST':
        form=forms.feedbackform(request.POST)
        if form.is_valid():
            print('the information is' )
            print('name is',form.cleaned_data['name'])
            print('sal is',form.cleaned_data['sal'])
            print('email is',form.cleaned_data['email'])
            print('feedback is',form.cleaned_data['feedback'])
            return thanku(request)
    return render(request,'testapp/feed.html',{'form':form})
