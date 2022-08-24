from django import forms

'''
I can use Form for an API if I don't want connect a sql table to
an API
'''
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()