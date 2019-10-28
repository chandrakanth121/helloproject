from django import forms
class feedbackform(forms.Form):
    name=forms.CharField()
    sal=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField()
